# func_vlook_01
def join_comp(df1: pd.DataFrame, df2: pd.DataFrame, file1_name: str, file2_name: str, list_cols: list) -> pd.DataFrame:
	# Drop duplicates from both tables to compare only unique values
	print("Left file before dropping duplicates: {}".format(df1.shape))
	df1.drop_duplicates(subset=list_cols, keep='first', inplace=True)
	print("Left file after dropping duplicates: {}".format(df1.shape))
	print("Right file before dropping duplicates: {}".format(df2.shape))
	df2.drop_duplicates(subset=list_cols, keep='first', inplace=True)
	print("Right file after dropping duplicates: {}".format(df1.shape))
	data = df1[list_cols].merge(df2[list_cols], how='outer', on=list_cols, indicator=True)
	data['_merge'] = np.where((data['_merge']=="left_only"), file1_name, np.where((data['_merge']=="right_only"), file2_name, data['_merge']))
	data = data.rename(columns={'_merge':"Comparison"})
	print("{}".format(data.shape))
	print("{}".format(data.columns))
	return data


# func_vlook_02
def replace_data(df_old: pd.DataFrame, df_new: pd.DataFrame, key_cols: list, cols_to_repl: list) -> pd.DataFrame:
	"""
	Replace specific columns in the old DataFrame with values from the new DataFrame based on key columns. 

	This function performs a left merge (join) of the old and new DataFrames on the specified key columns. 
	It then replaces the specified columns in the old DataFrame with corresponding columns from the new DataFrame. 

	Parameters:
	df_old (pd.DataFrame): The original DataFrame.
	df_new (pd.DataFrame): The DataFrame containing the new data. 
	key_cols (list): The list of key columns to merge on.
	cols_to_repl (list): The list of columns to replace in the old DataFrame. 

	Returns:
	pd.DataFrame: The updated DataFrame with the specified columns replaced.
	"""
	# Get the original column order
	orginal_cols = df_old.columns.tolist()

	# Perform a left merge to replace the data
	merged_df = pd.merge(df_old, df_new[key_cols + cols_to_repl], on=key_cols, how='left', suffixes=('', '_new'))

	# Remove old columns and rename new columns as old columns
	for column in cols_to_repl:
		# Delete the old column
		del merged_df[column]

		# Rename the new column to the old column name
		merge_df = merge_df.rename(columns={column + '_new': column})

	# Reorder the columns to match the original order
	merged_df = merged_df[original_cols]

	return merged_df

# Example usage:
# key_cols = ['fromProductLocation', 'fromLocationId', 'toProductId', 'toLocationId']
# cols_to_repl = ['duration']
# updated_df = replace_data(df1, df2, key_cols, cols_to_repl)
# Filtration of columns for display
# df = updated_df[key_cols + cols_to_repl]
# print(df.head(20))


# func_vlook_03
def vlook(df1, df2, key_columns, join_columns):
	"""
	Vlookup. Perform a left merge (join) on two DataFrames based on key columns and specific columns to join from the second DataFrame. 

	Parameters:
	df1 (pd.DataFrame): The first DataFrame to which we will add columns.
	df2 (pd.DataFrame): The second DataFrame from which we will add columns to the first one. 
	key_columns (list): List of key columns to join on. 
	join_columns (list): List of columns to join from the second DataFrame. 

	Returns:
	pd.DataFrame: The resulting DataFrame after the left join.
	"""
	# Validate key columns
	for key in key_columns:
		if key not in df1.columns:
			raise ValueError(f"Key column '{key}' not found in the first DataFrame.")
		if key not in df2.columns:
			raise ValueError(f"Key column '{key}' not found in the second DataFrame.")

	# Validate join columns
	for col in join_columns:
		if col not in df2.columns:
			raise ValueError(f"Join column '{col}' not found in the second DataFrame.")

	# Select only the necessary columns from the seond DataFrame
	df2_selected = df2[key_columns + join_columns]

	# Perform the left join
	result = pd.merge(df1, df2_selected, how='left', on=key_columns)

	return result

# Example usage:
# Filtration of columns
# df = pr_loc[['productId', 'locationId']]
# Key columns to join on
# key_cols = ['productId']
# Columns to join from the second DataFrame
# join_cols = ['materialType', 'processingType', 'uvp']

# Perform the Vlookup operation
# df = vlook(df, prod, key_cols, join_cols)
# Display the results
# print(df.head())


# func_vlook_04
def join_vlook(df1: pd.DataFrame, df2: pd.DataFrame, key_cols: list, new_col: str, source_name: str) -> pd.DataFrame:
	"""
	Vlookup. Perform a left merge (join) of a single columns (with source file name as suffix). 
	The new column is rounded, converted to an integer, and given a suffix indicating its source.

	Parameters:
	df1 (pd.DataFrame): The primary DataFrame. 
	df2 (pd.DataFrame): The DataFrame containing the new column to be added. 
	key_cols (list): The list of key columns to join on. 
	new_col (str): The name of the column to be added from second DataFrame. 
	source_name (str): The suffix to be added to the new column name. 

	Returns:
	pd.DataFrame: The updated DataFrame with the new column added. 
	"""
	print("Data before left join: {}".format(df1.shape))

	# Rename the column to be added with the source_name as suffix
	vlook_col = new_col + '-' + source_name
	df2 = df2.rename(columns={new_col: vlook_col})

	# Perform the left join
	cols = key_cols + [vlook_col]
	data = df1.merge(df2[cols], how='left', on=key_cols, indicator=False)

	# Fill NaN values with 0 and convert the new column to integer
	data[vlook_col] = data[vlook_col].fillna(0)
	try: 
		data[vlook_col] = data[vlook_col].round(0).astype(str).str.split('.').str[0].astype(int)
	except:
		print('String column connected')

	print("Data after left join: {}".format(data.shape))
	print("{}".format(data.columns))
	
	return data

# Example usage:
# df = pr_loc[['productId', 'locationId']]
# df = join_vlook(df, loc, ['locationId'], 'country', 'loc')
# print(df.head())


# func_vlook_05
def match_vlookup(df1: pd.DataFrame, df2: pd.DataFrame, key_col: str, match_col: str) -> pd.DataFrame:
	"""
	Vlookup. Perform an Index Match function from Excel to add a column indicating the row number of matching row. 
	This function adds a column to df1 indicating the row number of matching rows from df2 based on key column. 

	Parameters:
	df1 (pd.DataFrame): The primary DataFrame. 
	df2 (pd.DataFrame): The DataFrame containing the match column. 
	key_col (str): The column to join on. 
	match_col (str): The column in the second DataFrame to match with the key column. 

	Returns:
	pd.DataFrame: The updated DataFrame with the row number of matching rows added. 
	"""
	print("Data befor join: {}".format(df1.shape))

	# Rename the match column to the key_column
	df2 = df2.rename(columns={match_col: key_col})

	# Add a row number column
	df2.reset_index(inplace=True, drop=True)
	df2.reset_index(level=0, inplace=True)
	df2['index'] = df2['index'] + 1

	# Perform the left join
	cols = [key_col, 'index']
	data = df1.merge(df2[cols], how='left', on=key_col, indicator=False)
	data = data.rename(columns={'index': match_col})
	data[match_col] = data[match_col].fillna(0)

	# Convert the new column to integer
	try:
		data[match_col] = data[match_col].round(0).astype(str).str.split('.').str[0].astype(int)
	except:
		print('String column connected')

	del df2['index']
	df2 = df2.rename(columns={key_col: match_col})

	print("Data after left join: {}".format(data.shape))
	print("{}".format(data.columns))

	return data


# func_vlook_06
def left_join(df1: pd.DataFrame, df2: pd.DataFrame, source_name: str, key_cols: list, new_col: str = None) -> pd.DataFrame:
	"""
	Vlookup. Perform a left merge (join) to add all or specified columns from second DataFrame to the first DataFrame.
	If specific new_col is not provided, all columns from second DataFrame (except key columns) are added to the first DataFrame with suffix. 
	If the second DataFrame has only key columns they will be added with the suffix.

	Parameters:
	df1 (pd.DataFrame): The primary DataFrame. 
	df2 (pd.DataFrame): The secondary DataFrame from which new columns or a specific column should be added. 
	source_name (str): The suffix to be added to the new column names.
	key_cols (list): The list of key columns to join on. 
	new_col (str, optional): The name of the column to be added from second DataFrame. Default is None. 

	Returns:
	pd.DataFrame: The updated DataFrame with the new column or columns added. 
	"""
	print(f"Data before left join: {df1.shape}")

	# Convert key columns in both DataFrames to string type
	df1[key_cols] = df1[key_cols].astype(str)
	df2[key_cols] = df2[key_cols].astype(str)

	if new_col is None:
		# Join all columns from second DataFrame (except key columns)
		data = df1.merge(df2.rename(columns={col: f"{col}_{source_name}" for col in df2.columns if col not in key_cols}), how='left', on=key_cols)
		for col in data.columns:
			if col not in key_cols and source_name in col:
				data[col] = data[col].fillna(0)
	else:
		# Join only the specified column from second DataFrame
		join_col = f"{new_col}_{source_name}"
		data = df1.merge(df2[key_cols + [new_col]],rename(columns={new_col: join_col}), how='left', on=key_cols)
		data[join_col] = data[join_col].fillna(0)

	# Compare the newly connected column with the existing column if it exists
	try: 
		data['diff_perc'] = abs(data[new_col] - data[join_col]) / data[join_col]
	except:
		print('Newly connected column was not present in the initial table')

	# Add key columns from second DataFrame with a suffix if df2 has only hte key columns
	if len(df2.columns) == len(key_cols):
		for key in key_cols:
			data[f"{key}_{source_name}"] = df2[key]

	print(f"Data after left join: {data.shape}\n{data.columns}")
	return data


# func_vlook_07
def join_vlook(df1: pd.DataFrame, df2: pd.DataFrame, source_name: str, key_cols: list, new_col: str) -> pd.DataFrame:
	print("Data before left join: {}".format(df1.shape))
	# Changing the name of a column that will be added with source_name as suffix
	vlook_col = new_col + '_' + source_name
	df2 = df2.rename(columns={new_col: vlook_col})
	cols = key_cols + [vlook_col]
	data = df1.merge(df2[cols], how='left', on=key_cols, indicator=False)
	data[vlook_col] = data[vlook_col].fillna(0)
	try:
		data[vlook_col] = data[vlook_col].round(0)
		data[vlook_col] = data[vlook_col].astype(str)
		data[vlook_col] = data[vlook_col].str.split('.').str[0]
		data[vlook_col] = data[vlook_col].astype(int)
	except:
		print("String column connected")
	print("Data after left join: {}".format(data.shape))
	print("{}".format(data.columns))
	return data


# func_vlook_08