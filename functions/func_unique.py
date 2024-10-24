# func_unique_01
def list_unique_all_sheets(file_name: str, data_subfolder: str) -> pd.DataFrame:
	"""
	Number of unique values from every column from every sheet of an Excel file.
	Function reads an Excel file and extracts the number of unique values from every column from every sheet. The results are combined in a single DataFrame. 

	Parameters:
	file_name (str): The name of the Excel file (without extension).
	data_subfolder (str): The path to the folder containing the Excel file. 

	Returns:
	pd.DataFrame: A DataFrame with the number of unique values for each column in each sheet. 
	"""
	file_path = os.path.join(data_subfolder, file_name + '.xlsx')
	df_lisf = []

	def extract_no_unique_all(data: pd.DataFrame) -> pd.DataFrame:
		# Exctract number of unique values from each column in a DataFrame.
		col = []
		val = []
		for i in data.columns:
			val.append(data[i].nunique())
			col.append(i)
		return pd.DataFrame(list(zip(col, val)), columns=['column_name', 'unique_no'])

	# Process each sheet in Excel file
	for sheet in pd.ExcelFile(file_path).sheet_names:
		df = pd.read_excel(file_path, sheet_name=sheet)
		dx = extract_no_unique_all(df)
		dx['Sheet'] = sheet
		dx['File'] = file_name
		df_list.append(dx)

	data = pd.concat(df_list, ignore_index=True, sort=False)

	return data


# func_unique_02
def create_unique_rows_output(file1, file2, output_file, skip_rows=0):
	"""
	Unique rows from two input files table.
	
	Parameters:
	file1 (str): Path to the first input file (Excel or CSV)
	file2 (str): Path to the second input file (Excel or CSV)
	output_file (str): Path to the output Excel file.
	skip_rows (int, optional): Number of rows to skip when reading the input files (default is 0).
	"""
	# Determine file types
	file1_ext = file1.split('.')[-1]
	file2_ext = file2.split('.')[-1]

	# Extract file names from paths
	file1_name = os.path.basename(file1)
	file2_name = os.path.basename(file2)

	# Read input files
	if file1_ext in ['xlsx', 'xlsm', 'xls'] and file2_ext in ['xlsx', 'xlsm', 'xls']:
		# Excel files
		file1_sheets = pd.read_excel(file1, sheet_name=None, skiprows=skip_rows)
		file2_sheets = pd.read_excel(file2, sheet_name=None, skiprows=skip_rows)
	elif file1_ext == 'csv' and file2_ext == 'csv':
		# CSV files
		file1_sheets = {'Sheets1': pd.read_csv(file1, skiprows=skip_rows)}
		file2_sheets = {'Sheets2': pd.read_csv(file2, skiprows=skip_rows)}
	else:
		raise ValueError("Both files must be either Excel or CSV files with the same format.")

	# Create an Excel writer for the output
	with ExcelWriter(output_file) as writer:
		for sheet_name in file1_sheets.keys():
			if sheet_name in file2_sheets:
				df1 = file1_sheets[sheet_name]
				df2 = file2_sheets[sheet_name]

			# Check for common columns
			common_columns = df1.columns.intersection(df2.columns)
			if common_columns.empty:
				# Log the error in the output sheet
				error_df = pd.DataFrame({
					'Error': [f"No common columns to perform merge on for sheet '{sheet_name}'."]
				})
				error_df.to_excel(writer, sheet_name=sheet_name, index=False)
				print(f"No common columns to perform merge on for sheet '{sheet_name}'.")
				continue

				# Find unique rows in each DataFrame
				unique_to_file1 = df1.merge(df2, indicator=True, how='left').loc[lambda x: x['_merge'] == 'left_only'].drop(columns=['_merge'])
				unique_to_file2 = df2.merge(df1, indicator=True, how='left').loc[lambda x: x['_merge'] == 'left_only'].drop(columns=['_merge'])

				# Add Source column
				unique_to_file1['Source'] = file1_name
				unique_to_file2['Source'] = file2_name

				# Combine unique rows
				output_df = pd.concat([unique_to_file1, unique_to_file2], ignore_index=True)

				# Write to the output Excel file
				output_df.to_excel(writer, sheet_name=sheet_name, index=False)
			else:
				print(f"Sheet {sheet_name} not found in both files.")

	print(f"Output saved to {output_file}")

# Example usage:
# path1 = '/Users/Local_user/Downloads/file_1.xlsx'
# path2 = '/Users/Local_user/Downloads/file_2.xlsx'
# out_path = '/Users/Local_user/Downloads/file_1_2_comparison.xlsx'
# skip_rows = 1
# create_unique_rows_output(path1, path2, out_path, skip_rows)


# func_unique_03
def extract_no_unique(data: pd.DataFrame, list_cols: list, df_name: str):
	cols = ['Source','metric']
	col = []
	val = []
	for i in list_cols:
		val.append(data[i].nunique())
		col.append(i)
	data = pd.DataFrame(list(zip(col,val)), columns = ['no','unique']).T
	data.columns = data.iloc[0]
	data = data[1:]
	data[cols[0]] = df_name
	data[cols[1]] = data.index
	data = data[cols + [col for col in data.columns if col not in cols]]
	print(data.columns)
	print(data[:3])
	return data


# func_unique_04
def extract_no_unique_all(data: pd.DataFrame) -> pd.DataFrame:
	"""
	Extract the number of unique values from all columns of a DataFrame. 

	Parameters:
	data (pd.DataFrame): The input DataFrame.

	Returns:
	pd.DataFrame: DataFrame with columns 'column_name' and 'unique_no'
	"""
	col = []
	val = []
	for i in data.columns:
		val.append(data[i].nunique())
		col.append(i)
	data = pd.DataFrame(list(zip(col,val)), columns = ['column_name', 'unique_no'])
	print(f"Columns of the aggregated data: {data.columns}")
	print(data[:3])
	return data


# func_unique_05
def extract_no_unique_col_vals(data: pd.DataFrame, df_name: str):
	col = []
	val = []
	for i in data.columns:
		val.append(data[i].nunique())
		col.append(i)
	data = pd.DataFrame({'col_name': col, 'unique': val})
	data['Source'] = df_name
	print(data[:3])
	return data


# func_unique_06
def extract_unique(data: pd.DataFrame, list_cols: list) -> pd.DataFrame:
	"""
	Extract unique values from a subset of columns of a DataFrame.

	Parameters:
	data (pd.DataFrame): The input DataFrame.
	list_cols (list): List of column names to consider for extracting unique values. 

	Returns:
	pd.DataFrame: DataFrame with unique values based on the subset of columns. 
	"""
	cols = list_cols
	data.drop_duplicates(subset=cols, inplace=True)
	data = data[cols]
	data.reset_index(inplace=True, drop=True)
	print(data.columns)
	print(data.shape)
	print("Unique values are extracted based on the subset of columns without duplicates")
	print(data[:3])
	return data


# func_unique_07
def extract_unique_sep_in(df, cols) -> pd.DataFrame:
	"""
	Extract unique values from each input column separately and sort them. 

	Parameters:
	df (pd.DataFrame): The input DataFrame
	cols (list): List of column names to extract unique values from.

	Returns:
	pd.DataFrame: DataFrame with each column containing unique values sorted in ascending order.
	"""
	unique_data = {col: pd.Series(df[col].unique()) for col in cols}
	result = pd.DataFrame.from_dict(unique_data, orient='index').transpose()
	print("Each column is a separate list of unique values in a column")
	print("Sorting each column separately in ascending order")
	for col in result.columns:
		result[col] = result[col].sort_values(ignore_index=True)
	result = result.fillna('')
	return result


# func_unique_08
def extract_unique_sep_out(df, skip_columns=None):
	"""
	Extract unique values from each column of a DataFrame except specified columns and sort them. 
	
	Parameters:
	df (pd.DataFrame): The input DataFrame.
	skip_columns (list, optional): List of column names to exclude from extraction. Default is None. 
	
	Returns:
	pd.DataFrame: DataFrame with each column containing unique values sorted in ascending order.
	"""
	if skip_columns is None:
		skip_columns = []
	cols = [x for x in df.columns if x not in skip_columns]
	unique_data = {col: pd.Series(df[col].unique()) for col in cols}
	result = pd.DataFrame.from_dict(unique_data, orient='index').transpose()
	print("Each column is a separate list of unique values from an input column")
	print("Sorting each column seaparately in ascending order")
	for col in data.columns:
		result[col] = data[col].sort_values(ignore_index=True)
	result = result.fillna('')
	return result


# func_unique_09
def unique_differences(file1, file2, output_file, skip_rows=0):
	"""
	Extract unique values for every column of every sheet with source file indication. 
	Process two input files (Excel or CSV) to find unique values in common columns and write the results to an output Excel file. 
	
	Parameters:
	file1 (str); Path to the first input file (Excel or CSV). 
	file2 (str): Path to the second input file (Excel or CSV). 
	output_file (str): Path to the output Excel file. 
	skip_rows (int, optional): Number of rows to skip when reading the input files. Default is 0. 
	
	Raises:
	ValueError: If the file format is unsupported or if both files are not of the same type (both Excel or both CSV). 
	"""
	def read_file(file_path, skip_rows):
		"""
		Read an input file (Excel or CSV) into a DataFrame or a dictionary of DataFrames.

		Parameters:
		file_path (str): Path to the input file.
		skip_rows (int): Number of rows to skip when reading the file. 

		Returns:
		dict or pd.DataFrame: Dictionary of DataFrames if Excel file with multiple sheets, or a single DataFrame if Excel file with single sheet or a CSV file. 
		"""
		if file_path.endswith('.csv'):
			return pd.read_csv(file_path, skip_rows=skip_rows)
		elif file_path.endswith('.xlsx'):
			return pd.read_excel(file_path, sheet_name=None, skiprows=skip_rows)
		else:
			raise ValueError("Unsupported file format")

	def get_common_sheets(file1_sheets, file2_sheets):
		"""
		Identify common sheets between two Excel files.

		Parameters:
		file1_sheets (list): List of sheet names from the first Excel file. 
		file2_sheets (list): List of sheet names from the second Excel file. 

		Returns:
		list: List of common sheet names.
		"""
		return list(set(file1_sheets).intersection(set(file2_sheets)))

	def process_sheets(file1_data, file2_data, common_sheets, file1_name, file2_name):
		"""
		Process common sheets to find unique values in common columns.

		Parameters:
		file1_data (dict): Dictionary of DataFrames from the first Excel file. 
		file2_data (dict): Dictionary of DataFrames from the second Excel file. 
		common_sheets (list): List of common sheet names. 
		file1_name (str): Name of the first input file. 
		file2_name (str): Name of the second input file. 

		Returns:
		dict: Dictionary of processed DataFrames. 
		"""
		processed_data={}
		for sheet in common_sheets:
			df1 = file1_data[sheet]
			df2 = file2_data[sheet]

			common_columns = df1.columns.intersection(df2.columns)

			# Skip sheets with no common columns
			if len(common_columns) == 0:
				continue

			unique_data = pd.DataFrame()

			for col in common_columns:
				unique_values_file1 = df1[col][~df1[col].isin(df2[col])].drop_duplicates().reset_index(drop=True)
				unique_values_file2 = df2[col][~df2[col].isin(df1[col])].drop_duplicates().reset_index(drop=True)

				combined_unique_values = pd.concat([unique_values_file1, unique_values_file2], ignore_index=True)
				source_column = [file1_name] * len(unique_values_file1) + [file2_name] * len(unique_values_file2)

				temp_df = pd.DataFrame({col: combined_unique_values, 'Source': source_column})
				unique_data = pd.concat([unique_data, temp_df], axis=0, ignore_index=True)

			unique_data = unique_data.loc[:,~unique_data.columns.duplicated()]

			# Ensure 'Source' column exists before moving it to the front
			if 'Source' in unique_data.columns:
				unique_data.insert(0, 'Source', unique_data.pop('Source')) # Move 'Source' column to the front

			# Sort by 'Source' column
			unique_data = unique_data.sort_values(by='Source').reset_index(drop=True)

			processed_data[sheet] = unique_data

		return processed_data

	def process_csv(file1_data, file2_data, file1_name, file2_name):
		"""
		Process CSV files to find unique values in common columns.
	
		Parameters:
		file1_data (pd.DataFrame): DataFrame from the first CSV file. 
		file2_data (pd.DataFrame): DataFrame from the second CSV file. 
		file1_name (str): Name of the first input file. 
		file2_name (str): Name of the second input file. 
	
		Returns:
		pd.DataFrame: Processed DataFrame.
		"""
		common_columns = file1_data.columns.intersection(file2_data.columns)
		unique_data = pd.DataFrame()

		for col in common_columns:
			unique_values_file1 = file1_data[col][~file1_data[col].isin(file2_data[col])].drop_duplicates().reset_index(drop=True)
			unique_values_file2 = file2_data[col][~file2_data[col].isin(file1_data[col])].drop_duplicates().reset_index(drop=True)

			combined_unique_values = pd.concat([unique_values_file1, unique_values_file2], ignore_index=True)
			source_column = [file1_name] * len(unique_values_file1) + [file2_name] * len(unique_values_file2)

			temp_df = pd.DataFrame({col: combined_unique_values, 'Source': source_column})
			unique_data = pd.concat([unique_data, temp_df], axis=0, ignore_index=True)

		unique_data = unique_data.loc[:,~unique_data.columns.duplicated()]

		# Ensure 'Source' column exists before moving it to the front
		if 'Source' in unique_data.columns:
			unique_data.insert(0, 'Source', unique_data.pop('Source')) # Move 'Source' column to the front

		# Sort by 'Source' column
		unique_data = unique_data.sort_values(by='Source').reset_index(drop=True)

		return unique_data

	def write_to_excel(processed_data, output_file):
		"""
		Write processed data to an Excel file with multiple sheets.
	
		Parameters:
		processed_data (dict): Dictionary of processed DataFrames. 
		output_file (str): Path to the output Excel file. 
		"""
		with pd.ExcelWriter(output_file) as writer:
			for sheet, data in processed_data.item()
				data.to_excel(writer, sheet_name=sheet, index=False)

	# Main logic
	file1_data = read_file(file1, skip_rows)
	file2_data = read_file(file2, skip_rows)

	file1_name = file1.split('/')[-1]
	file2_name = file2.split('/')[-1]

	if isinstance(file1_data, dict) and isinstance(file2_data, dict):
		# Both files are Excel files with multiple sheets
		common_sheets = get_common_sheets(file1_data.keys(), file2_data.keys())
		processed_data = process_sheets(file1_data, file2_data, common_sheets, file1_name, file2_name)
		write_to_excel(processed_data, output_file)
		print("Comparison complete.")
	elif isinstance(file1_data, pd.DataFrame) and isinstance(file2_data, pd.DataFrame):
		# Both files are CSV files
		processed_data = {'Sheet1': process_csv(file1_data, file2_data, file1_name, file2_name)}
		write_to_excel(processed_data, output_file)
		print("Comparison complete.")
	else:
		raise ValueError("Both files must either Excel files with multiple sheets or CSV files")

# Example usage:
# path1 = '/Users/Local_user/Downloads/file1.xlsx'
# path2 = '/Users/Local_user/Downloads/file2.xlsx'
# out_path = '/Users/Local_user/Downloads/files_comp.xlsx'
# skip_rows = 1 
# unique_differences(path1, path2, out_path, skip_rows)


# func_unique_10
import pandas as pd

def no_of_unique_values(df, columns=None):
    """
    Analyzes the number of unique values in the specified columns of a DataFrame.

    Parameters:
    df (pd.DataFrame): The input DataFrame.
    columns (list, optional): List of columns to analyze. Analyzes all columns if not provided.

    Returns:
    pd.DataFrame: A DataFrame with column names and the count of unique values.
    """
    # If no columns are specified, analyze all columns
    if columns is None:
        columns = df.columns
    
    # Initialize a list to store the results
    result = []
    
    # Iterate over the specified columns and calculate the number of unique values
    for col in columns:
        num_unique = df[col].nunique()
        result.append([col, num_unique])
    
    # Create an output DataFrame from the result list
    output_df = pd.DataFrame(result, columns=['Column Name', 'Unique Values'])
    
    return output_df

# Example usage:
# Creating a sample DataFrame
data = {
    'Category': ['A', 'B', 'A', 'A', 'B', 'C'],
    'Subcategory': ['X', 'Y', 'X', 'Z', 'Y', 'X'],
    'Value': [10, 20, 10, 30, 20, 10]
}
df = pd.DataFrame(data)

# Analyzing specified columns
output_df = analyze_unique_values(df, ['Category', 'Subcategory'])
print(output_df)

# Analyzing all columns
output_df = analyze_unique_values(df)
print(output_df)