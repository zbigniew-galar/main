# func_comp_01
def compare_files(file1, file2, out_path, skip_rows=None):
	"""
	Compare two files and save the comparison to an Excel file, with 'Global Info' as the first sheet.
	
	Parameters:
	file1 (str): Path to the first file.
	file2 (str): Path to the second file. 
	out_path (str): Output path for the Excel comparison result. 
	skip_rows (int, optional): Number of rows to skip at the start of the files.
	"""
	# Create  a new Excel writer object
	writer = pd.ExcelWriter(out_path, engine='openpyxl')

	# Function to read files, optionally skipping rows, and return DataFrames and sheet names
	def read_file(file, skip_rows):
		if file.endswith('.csv'):
			df = pd.read_csv(file, skiprows=skip_rows)
			return [df], ['CSV']
		elif file.endswith('.xlsx') or file.endswith('.xls'):
			xls = pd.ExcelFile(file)
			dfs = [xls.parse(sheet, skiprows=skip_rows) for sheet in xls.sheet_names]
			return dfs, xls.sheet_names
		else:
			raise ValueError("Unsupported file format")

	# Initialize an empty DataFrame for global information
	global_info_all = pd.DataFrame()
	statistics_all = pd.DataFrame()

	# Read the files, applying the skip_rows parameter
	dfs1, sheet_name1 = read_file(file1, skiprows=skip_rows)
	dfs2, sheet_name1 = read_file(file2, skiprows=skip_rows)

	# Identify common sheets 
	common_sheets = set(sheet_names1) & set(sheet_names2)

	for sheet in common_sheets:
		df1 = dfs1[sheet_names1.index(sheet)]
		df2 = dfs2[sheet_names2.index(sheet)]

		# Compile global information about the DataFrames
		global_info = pd.DataFrame({
			'Statistics': ['Shape', 'Number of Rows', 'Number of Columns', 'Total Unique Values', 'Total Value Count'],
			'File1':[df1.shape, df1.shape[0], df1.shape[1], df1.nunique().sum(), df1.count().sum()],
			'File2':[df2.shape, df2.shape[0], df2.shape[1], df2.nunique().sum(), df2.count().sum()],
			'Sheet': [sheet] * 5
		})
		global_info_all = pd.concat([global_info_all, global_info])

		# Calculate statistics for numerical columns
		if not df1.select_dtypes(include=[np.number]).empty:
			numerical_stats_df1 = df1.describe(include=[np.number]).T
			numerical_stats_df1['Source File'] = os.path.basename(file1)
			numerical_stats_df1['Sheet Name'] = sheet
			statistics_all = pd.concat([statistics_all, numerical_stats_df1])

		if not df2.select_dtypes(include=[np.number]).empty:
			numerical_stats_df2 = df2.describe(include=[np.number]).T
			numerical_stats_df2['Source File'] = os.path.basename(file2)
			numerical_stats_df2['Sheet Name'] = sheet
			statistics_all = pd.concat([statistics_all, numerical_stats_df2])
		
		# Calculate statistics for non-numerical columns:
		if not df1.select_dtypes(include=[object]).empty:
			non_numerical_stats_df1 = df1.describe(include=[object]).T
			non_numerical_stats_df1['Source File'] = os.path.basename(file1)
			non_numerical_stats_df1['Sheet Name'] = sheet
			statistics_all = pd.concat([statistics_all, non_numerical_stats_df1])

		if not df2.select_dtypes(include=[object]).empty:
			non_numerical_stats_df2 = df2.describe(include=[object]).T
			non_numerical_stats_df2['Source File'] = os.path.basename(file2)
			non_numerical_stats_df2['Sheet Name'] = sheet
			statistics_all = pd.concat([statistics_all, non_numerical_stats_df2])
			
	# Sort and rearrange columns in the statistics DataFrame
	if not statistics_all.empty:
		statistics_all = statistics_all.sort_values(by='Source File')
		columns_order = ['Source File', 'Sheet Name'] + [col for col in statistics_all.columns if not in ['Source File', 'Sheet Name']]
		statistics_all = statistics_all[columns_order]

	# Write the 'Global Info' sheet
	global_info_all.to_excel(writer, sheet_name='Global Info', index=False)

	# Write the 'Statistics' sheet
	if not statistics_all.empty:
		statistics_all.to_excel(writer, sheet_name='Statistics', index=True)

	# Process and write unique values after the 'Global Info' sheet
	for sheet in common_sheets:
		df1 = dfs1[sheet_names1.index(sheet)]
		df2 = dfs2[sheet_names2.index(sheet)]

		unique_df1 = pd.DataFrame({col: pd.Series(df1[col].unique()) for col in df1.columns})
		unique_df2 = pd.DataFrame({col: pd.Series(df2[col].unique()) for col in df2.columns})
		pd.concat([unique_df1, unique_df2], axis=1).to_excel(writer, sheet_name=f'Unique Values {sheet}')

		common_cols = list(set(df1.columns) & set(df2.columns))
		unique_values = pd.DataFrame({col: pd.Series(list(set(df1[col].unique()) - set(df1[col].unique()))) for col in common_cols})
		unique_values.to_excel(writer, sheet_name=f'Unique in File1 {sheet}')

	# Save and close the Excel file
	writer.close()
	print('Comparison complete.')

# Example usage:
# path1 = 'Users/Local_user/VS Code projects/Test project/data/Comp1.xlsx'
# path2 = 'Users/Local_user/VS Code projects/Test project/data/Comp2.xlsx'
# out_path = 'Users/Local_user/VS Code projects/Test project/data/Comparison.xlsx'
# skip_rows = 0
# compare_files(path1, path2, out_path, skip_rows)


# func_comp_02
def compare_map_inv_files(file1, file2, column_mapping_file, out_path, skip_rows=None):
	"""
	Compare two files and save the comparison to an Excel file, with 'Global Info', 'Statistics', and 'Mapping' as the first 3 sheets.
	Always check if both input files have the same file extension.
	If any output sheet exceeds 1 million rows, it will be saved as a CSV file instead.

	Parameters:
	file1 (str): Path to the first file. 
	file2 (str): Path to the second file. 
	column_mapping_file (str): Path to the column mapping file.
	out_path (str): Output path for the Excel comparison result. 
	skip_rows (int, optional): Number of rows to skip at the start of the files.
	"""

	def compare_and_export(file1, file2, column_mapping_file, out_path, suffix, sheet_name=None):
		"""
		Internal function to perform the comparison and export the results. 

		Parameters:
		file1 (str): Path to the first file. 
		file2 (str): Path to the second file. 
		column_mapping_file (str): Path to the column mapping file. 
		out_path (str): Output path for the Excel comparison result. 
		suffix (str): Suffix to add to the output file name.
		sheet_name (str, optional): Nam of the sheet to process. None for CSV files. 
		skip_rows (int, optional): Number of rows to skip at the start of the file. 
		"""
		# Create a new Excel writer object with the suffix
		out_path_with_suffix = f"{os.path.splitext(out_path)[0]}_{sheet_name if sheet_name else 'Sheet1'}_{suffix}{os.path.splitext(out_path)[1]}"
		writer = pd.ExcelWriter(out_path_with_suffix, engine='openpyxl')

		# Function to read files, optionally skipping rows, and return DataFrames
		def read_file(file, sheet_name, skip_rows):
			if file.endswith('.csv'):
				df = pd.read_csv(file, skiprows=skip_rows, low_memory=False)
				return df
			elif file.endswith('.xlsx') or file.endswith('.xls'):
				xls = pd.ExceFile(file)
				df = xls.parse(sheet_name, skiprows=skip_rows)
				return df
			else:
				raise ValueError("Unsupported file format")

		# Function to read the column mapping file
		def read_mapping_file(mapping_file, swap_columns=False):
			if mapping_file.endswith('.csv'):
				mapping_df = pd.read_csv(mapping_file, header=None)
			elif mapping_file.endswith('.xlsx') or mapping_file.endswith('.xls'):
				mapping_df = pd.read_excel(mapping_file, header=None)
			else:
				raise ValueError("Unsupported file format")

			if swap_columns:
				mapping_df = mapping_df[[1,0] + ([2] if 2 in mapping_df.columns else [])]

			return mapping_df, dict(zip(mapping_df.iloc[:,1], mapping_df.iloc[:, 0]))

		# Read the column mapping file
		swap_columns = (suffix == "2_to_1")
		mapping_df, column_mapping_dict = read_mapping_file(column_mapping_file, swap_columns)

		# Initialize empty DataFrames for global information and statistics
		global_info_all = pd.DataFrame()
		stats_all = pd.DataFrame()

		# Read the files, applying the skip_rows parameter
		df1 = read_file(file1, sheet_name, skip_rows)
		df2 = read_file(file2, sheet_name, skip_rows)

		# Apply column mapping to the second DataFrame
		df2.rename(columns=column_mapping_dict, inplace=True)

		# Compile global information about the DataFrame
		global_info = pd.DataFrame({
		'Statistic': ['Shape', 'Number of Rows', 'Number of Columns', 'Total Unique Values', 'Total Value Count'],
		'File1': [df1.shape, df1.shape[0], df1.shape[1], df1.nunique().sum(), df1.count().sum()],
		'File2': [df2.shape, df2.shape[0], df2.shape[1], df2.nunique().sum(), df2.count().sum()],
		'Sheet': [sheet_name if sheet_name else 'CSV'] * 5
		})
		global_info_all  = pd.concat([global_info_all, global_info])

		# Compile statistics for each column in each DataFrame
		stats_df1 = df1.describe(include='all').transpose()
		stats_df2 = df2.describe(include='all').transpose()
		stats_df1['Source'] = os.path.basename(file1)
		stats_df2['Source'] = os.path.basename(file2)
		stats_df1['Sheet'] = sheet_name if sheet_name else 'CSV'
		stats_df2['Sheet'] = sheet_name if sheet_name else 'CSV'

		# Add mapped column information
		reverse_column_mapping_dict = {v: k for k, v in column_mapping_dict.items()}
		stats_df1['Mapped Column'] = stats_df1.index.map(reverse_column_mapping_dict)
		stats_df2['Mapped Column'] = stats_df2.index.map(column_mapping_dict)

		# Add original field names
		stats_df1['Original Field Name'] = stats_df1.index
		stats_df2['Original Field Name'] = stats_df2.index

		# Combine statistics DataFrames
		stats_all = pd.concat([stats_df1, stats_df2])

		# Reorder the columns in the stats_all DataFrame
		column_order = ['Source', 'Sheet', 'Original Field Name', 'Mapped Column', 'count', 'unique', 'top', 'freq', 'mean', 'std', 'min', '25%', '50%', '75%', 'max']
		column_oder = [col for col in column_order if col in stats_all.columns] # Ensure only existing columns are included
		stats_all = stats_all[column_order]

		# Add index to the 'Statistics' DataFrame
		stats_all.index.name = 'Field Name'

		# Function to write DataFrame to Excel or CSV based on row count
		def write_df(df, writer, sheet_name, out_path, header=True):
			if len(df) > 1_000_000:
				csv_path = f"{os.path.splitext(out_path)[0]}_{sheet_name}.csv"
				df.to_csv(csv_path, index=False, header=header)
				print(f"DataFrame exceeds 1 million rows. Written to CSV: {csv_path}")
			else:
				df.to_excel(writer, sheet_name=sheet_name, index=False, header=header)

		# Write the 'Global Info', 'Statistics', and 'Mapping' sheets first
		write_df(global_info_all, writer, 'Global Info', out_path)
		write_df(stats_all, writer, 'Statistics', out_path)
		write_df(mappind_df, writer, 'Mapping', out_path, header=False)

		# Process and write unique values after the 'Global Info' and 'Statistics' sheets
		unique_df1 = pd.DataFrame({col: pd.Series(df1[col].unique()) for col in df1.columns})
		unique_df2 = pd.DataFrame({col: pd.Series(df2[col].unique()) for col in df2.columns})
		combined_unique_df = pd.concat([unique_df1, unique_df2], axis=1)
		write_df(combined_unique_df, writer, f'Unique in File1 {sheet_name if sheet_name else "Sheet1"}', out_path)

		# Save and close the Excel file
		writer.close()
		print(f'Comparison complete for {suffix} on sheet {sheet_name if sheet_name else "Sheet1"}.')
	# Ensure both input files have the same file extension
	if os.path.splitext(file1)[1] != os.path.splitext(file2)[1]:
		raise ValueError("Both input files must have the same file extension")

	# Read the column mapping file to ge the sheet names
	if column_mapping_file.endswith('.csv'):
		mapping_df = pd.read_csv(column_mapping_file, header=None)
	elif column_mapping_file.endswith('.xlsx') or column_mapping_file.endswith('.xls'):
		mapping_df = pd.read_excel(column_mapping_file, header=None)
	else:
		raise ValueError("Unsupported file format")

	# Check if the third column exists
	if 2 in mapping_df.columns:
		sheet_names = mapping_df.iloc[:, 2].dropna().unique()
	else:
		sheet_names = []

	# Read the sheet names from the input files
	if file1.endswith('.xlsx') or file1.endswith('.xls'):
		xls1 = pd.ExcelFile(file1)
		sheet_names1 = xls1.sheet_names
	else:
		sheet_names1 = ['Sheet1']

	if file2.endswith('.xlsx') or file2.endswith('.xls'):
		xls2 = pd.ExcelFile(file2)
		sheet_names2 = xls2.sheet_names
	else:
		sheet_names2 = ['Sheet1']

	# Find common sheets
	common_sheets = set(sheet_names1) & set(sheet_names2) & set(sheet_names)

	# If there are no common sheets, use 'CSV' for CSV files
	if not common_sheets and (file1.endswith('.csv') and file2.endswith('.csv')):
		common_sheets = ['CSV']

	# Perform the comparison for each common sheet
	for sheet_name in common_sheets:
		# Perform the first comparison with the suffix "1_to_2"
		compare_and_export(file1, file2, column_mapping_file, out_path, "1_to_2", sheet_name, skip_rows)
		# Perform the first comparison with the suffix "1_to_2"
		compare_and_export(file2, file1, column_mapping_file, out_path, "2_to_1", sheet_name, skip_rows)

# Example usage:
# path1 = '/Users/Local_user/Desktop/VS Code projects/Test project/data/table1.csv'
# path2 = '/Users/Local_user/Desktop/VS Code projects/Test project/data/table2.csv'
# map_path = '/Users/Local_user/Desktop/VS Code projects/Test project/data/mapping_file.csv'
# out_path = '/Users/Local_user/Desktop/VS Code projects/Test project/data/table1 table2 comp.xlsx'
# skip_rows = 0
# compare_map_inv_files(path1, path2, map_path, out_path)


# func_comp_03
def compare_excel_files(file1_path, file2_path, skip_rows=0):
	"""
	Compare Excel files or CSV files and find the percentage of common unique values for common columns in common sheets. 
	File 1 is being the point of reference for how many common unique values are for each common column for each common sheet to show how close the second file is to the first file via what is the percentage of the same unique values for each column-sheet combination. 
	"""
	# Helper function to read Excel or CSV file
	def read_file(file_path, skip_rows):
		if file_path.endswith('.csv'):
			return {'Sheet1': pd.read_csv(file_path, skiprows=skip_rows)}
		elif file_path.endswith(('.xls', '.xlsx', '.xlsm', '.xlsb')):
			return pd.read_excel(file_path, sheet_name=None, skiprows=skip_rows)
		else:
			raise ValueError("Unsupported file format. Pleaser provide a CSV, XLS, XLSX, or XLSB file.")

	# Read both files
	file1_sheets = read_file(file1_path, skip_rows)
	file2_sheets = read_file(file2_path, skip_rows)

	# Find common sheet names
	common_sheets = set(file1_sheets.keys()).intersection(se(file2_sheets.keys()))

	# Initialize results list for the first output table
	results = []

	# Initialize results list for the second output table
	all_columns_results = []

	# Initialize variables for the third output table
	total_common_unique_values = 0
	total_unique_values_file1 = 0

	# Initialize variables for the fourth output table
	sheet_level_results = []

	# Iterate over sheets in the first file
	for sheet in file1_sheets.keys():
		df1 = file1_sheets[sheet]

		# Check if the sheet is also in the second file
		if sheet in file2_sheets:
			df2 = file2_sheets[sheet]
			common_columns = set(df1.columns).intersection(set(df2.columns))
		else:
			common_columns = set()

		# Initialize list to store percentages for the current sheet
		sheet_percentages = []

		# Iterate over columns in the first file's sheet
		for column in df1.columns:
			if column in common_columns:
				unique_values1 = set(df1[column].dropna().unique())
				unique_values2 = set(df2[column].dropna().unique())
				common_unique_values = unique_values1.intersection(unique_values2)

				# Calculate percentage
				if len(unique_values1) > 0:
					percentage_common = (len(common_unique_values) / len(unique_values1)) * 100
				else:
					percentage_common = 0

				# Append result for the first output table
				results.append({
					'Sheet Name': sheet,
					'Column Name': column, 
					'Percentage of Common Unique Values': round(percentage_common)
				})

				# Append result for the second output table
				all_columns_results.append({
					'File Name': os.path.basename(file1_path), 
					'Sheet Name': sheet,
					'Column Name': column, 
					'Percentage of Common Unique Values': round(percentage_common)
				})

				# Update total unique values and common unique values for the third output table
				total_common_unique_values += len(common_unique_values)
				total_unique_values_file1 += len(unique_values1)

				# Append percentage of the sheet percentages list
				sheet_percentages.append(percentage_common)
			else:
				# Append result for the second output table with 0 percentage
				all_columns_results.append({
					'File Name': os.path.basename(file1_path), 
					'Sheet Name': sheet, 
					'Column Name': column, 
					'Percentage of Common Unique Values': 0
				})

				# Append 0 to the sheet percentages list
				sheet_percentages.append(0)

		# Calculate average percentage for the current sheet
		if sheet_percentages:
			average_percentage_common_sheet = sum(sheet_percentages) / len(sheet_percentages)
		else:
			average_percentage_common_sheet = 0

		sheet_level_results.append({
			'Sheet Name': sheet, 
			'Average Percentage of Common Unique Values': round(average_percentage_common_sheet)
		})

	# Calculate overall similarity statistics for the third output table
	if total_unique_values_file1 > 0:
		overall_percentage_common = (total_common_unique_values / total_unique_values_file1) * 100
	else:
		overall_percentage_common = 0

	similarity_stats = {
		'Total Sheets in File 1': len(file1_sheets), 
		'Total Sheets in File 2': len(file2_sheets), 
		'Common Sheets': len(common_sheets), 
		'Percentage of Common Sheets': round((len(common_sheets) / len(file1_sheets)) * 100) if len(file1_sheets) > 0 else 0, 
		'Total Unique Values in Common Sheets (File 1)': total_unique_values_file1, 
		'Total Common Unique Values': total_common_unique_values, 
		'Overall Percentage of Common Unique Values': round(overall_percentage_common)
	}

	# Convert results to DataFrames
	results_df = pd.DataFrame(results)
	all_columns_results_df = pd.DataFrame(all_columns_results)
	similarity_stats_df = pd.DataFrame([similarity_stats])
	sheet_level_results_df = pd.DataFrame(sheet_level_results)

	# Extract file names without extensions
	file1_name = os.path.splitext(os.path.basename(file1_path))[0]
	file2_name = os.path.splitext(os.path.basename(file2_path))[0]

	# Create output file name
	output_file_name = f"comp_{file1_name}_{file2_name}.xlsx"
	output_file_path = os.path.join(os.path.dirname(file1_path), output_file_name)

	# Save results to an Excel file in the same folder as the first input file
	with pd.ExceWriter(output_file_path) as writer:
		similarity_stats_df.to_excel(writer, sheet_name='Similarity Stats', index=False)
		sheet_level_results_df.to_excel(writer, sheet_name='Sheet Level Stats', index=False)
		results_df.to_excel(writer, sheet_name='Common Unique Values', index=False)
		all_columns_results_df.to_excel(writer, sheet_name='All Columns', index=False)

	return similarity_stats_df, sheet_level_results_df, results_df, all_columns_results_df

# Example usage
# path1 = '/Users/Local_user/Desktop/VS Code projects/Test project/data/excel_file.xlsx'
# path2 = '/Users/Local_user/Desktop/VS Code projects/Test project/data/excel_new_file.xlsx'
# result1, result2, result3, result4 = compare_excel_files(path1, path2, skip_rows=1)
# print(result1)


# func_comp_04
def comparison_func(df1: pd.DataFrame, df2: pd.DataFrame, input1_name: str, input2_name: str, comp_level: list) -> pd.DataFrame:
	"""
	Compare two DataFrames based on predefined key columns and indicate the source of each row.
	
	This function merges two DataFrames (join method in Python) using an outer join on the specified key columns and adds indicator column to show the source of each row.

	Parameters:
	df1 (pd.DataFrame): The first DataFrame.
	df2 (pd.DataFrame): The second DataFrame.
	input1_name (str): The name to be used for rows unique to the first DataFrame.
	input2_name (str): The name to be used for rows unique to the second DataFrame.
	comp_level (list): The list of key columns to be used for comparison.

	Returns:
	pd.DataFrame: A DataFrame with the merged data and an indicator column.
	"""
	# Drop duplicates from both DataFrames to compare only unique values
	for df, name in [(df1, "Input_1"), (df2, "Input_2")]:
		print(f"{name} before dropping duplicates: {df.shape}")
		df.drop_duplicates(subset=comp_level, keep='first', inplace=True)
		print(f"{name} after dropping duplicates: {df.shape}")

	# Merge the DataFrames using an outer  join on the key columns
	data = df1[comp_level].merge(df2[comp_level], how='outer', on=comp_level, indicator="Comparison")
	# Update the 'Comparison' column to indicate the source of each row
	data['Comparison'] = np.where(data['Comparison'] == "left_only", input1_name, np.where(data['Comparison'] == "right_only", input2_name, data['Comparison']))

	print(f"{data.shape}\n{data.columns}")

	# Optional: Uncomment the following lines to show only differences
	# data = data[data['Comparison'] != 'both']
	# print(f"{data.shape}\n{data.head(7)}")

	return data


# func_comp_05