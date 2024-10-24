# func_meta_01
def extract_row_from_folder(folder_path: str, row_number: int, skip_rows: int=0):
	"""
	Extract a specific row from all CSV and Excel files in a folder and save the results to a new Excel file.

	Parameters:
	folder_path (str): The path to the folder containing the files. 
	row_number (int): The 1-indexed row number to extract (0 for headers). 
	skip_rows (int, optional): The number of rows to skip at the beginning of each file. Default is 0.

	Returns:
	None
	"""
	# Initialize an empty list to store the extracted row
	extracted_rows = []

	# List all files in the folder
	for file_name in os.listdir(folder_path):
		file_path = os.path.join(folder_path, file_name)

		if file_name.endswith('.csv'):
			# Read CSV file
			try:
				df = pd.read_csv(file_path, skiprows=skip_rows)
				if row_number == 0:
					# Extract headers
					row_data = df.columns.tolist()
				else:
					row_index = row_number - 1
					if row_index < len(df):
						row_data = df.iloc[row_index].tolist()
					else:
						continue
				for col_index, value in enumerate(row_data):
					extracted_rows.append([file_name, None, col_index + 1, value])
			except Exception as e:
				print(f"Errror reading {file_name}: {e}")

		elif file_name.endswith('.xlsx') or file_name.endswith('.xls'):
			# Read Excel file
			try: 
				excel_file = pd.ExcelFile(file_path)
				for sheet_name in excel_file.sheet_names:
					df = pd.read_excel(file_path, sheet_name=sheet_name, skiprows=skip_rows)
					if row_number == 0:
						# Extract headers
						row_data = df.columns.tolist()
				else:
					row_index = row_number - 1
					if row_index < len(df):
						row_data = df.iloc[row_index].tolist()
					else:
						continue
				for col_index, value in enumerate(row_data):
					exctracted_rows.append([file_name, sheet_name, col_index + 1, value])
			except Exception as e:
				print(f"Error reading {file_name}: {e}")

	# Create a DataFrame from the extracted rows
	if extracted_rows:
		column = ['File Name', 'Sheet Name', 'Column', 'Value']
		output_df = pd.DataFrame(extracted_rows, columns=columns)

		# Save the output DataFrame as a new Excel file
		if row_number == 0:
			output_file_path = os.path.join(folder_path, 'folder_files_headers.xlsx')
			output_df.to_excel(output_file_path, index=False)
		else:
			output_file_path = os.path.join(folder_path, f"folder_files_row_{row_number}.xlsx")
			output_df.to_excel(output_file_path, index=False)
		print(f"Output saved to {output_file_path}")
	else:
		print("No datra extracted. Please check the folder and row number.")

# Example usage:
# For extracting headers:
# extract_row_from_folder('/Users/Local_user/Downloads/', 0)
# For extracting the 3rd row (1-indexed):
# extract_row_from_folder('/Users/Local_user/Downloads/', 3)


# func_meta_02
def extract_metadata(file1_path, file2_path, output_path, skip_rows=0):
	"""
	Extract metadata from two files (Excel or CSV) and save the metadata to an output Excel file.

	Parameters:
	file1_path (str): Path to the first input file (Excel or CSV).
	file2_path (str): Path to the second input file (Excel or CSV).
	output_path (str): Path to the output Excel file where the metadata will be saved. 
	skip_rows (int, optional): Number of rows to skip at the beginning of each sheet (default is 0).

	Raises:
	ValueError: If the file type is not supported. 

	Returns:
	None.
	"""
	def read_file(file_path, skip_rows):
		"""
		Reads an Excel or CSV file and extracts data and sheet names. 

		Parameters:
		file_path (str): Path to the input file (Excel or CSV).
		skip_rows (int): Number of rows to skip at the beginning of each sheet.

		Returns:
		data (dict): Dictionary where keys are sheet names and values are DataFrames containing the data. 
		sheet_name (list): List of sheet names in the file.
		"""
		file_extension = os.path.splitext(file_path)[1].lower()
		if file_extension in ['.xls', '.xlsx', '.xlsm']:
			# Read Excel file
			xls = pd.ExcelFile(file_path)
			sheet_names = xls.sheet_names
			data = {sheet: pd.read_excel(file_path, sheet_name=sheet, skiprows=skip_rows) for sheet in sheet_names}
		elif file_extension == '.csv':
			# Read CSV file
			data = {'CSV': pd.read_csv(file_path, skiprows=skip_rows)}
			sheet_names = ['CSV']
		else:
			raise ValueError("Unsupported file type")
		return data, sheet_name

	def create_metadata_df(data, sheet_names, file_name):
		"""
		Creates a metadata DataFrame from the data and sheet names.

		Parameters:
		data (dict): Dictionary where keys are sheet names and values are DataFrames containing the data. 
		sheet_names (list): List of sheet names in the file. 
		file_name (str): Name of the file from which the data was extracted. 

		Returns:
		metadata_df (pd.DataFrame): DataFrame containing metadata information.
		"""
		metadata = {}
		for sheet in sheet_names:
			df = data[sheet]
			metadata[sheet] = df.columns.tolist()
		metadata_df = pd.DataFrame(dict([(k, pd.Series(v)) for k, v in metadata.items()]))
		metadata_df['Scource'] = file_name
		return metadata_df

	def create_detailed_metadata_df(data, sheet_names, file_name):
		"""
		Creates a detailed metadata DataFrame from the data and sheet names.

		Parameters:
		data (dict): Dictionary where keys are sheet names and values are DataFrames containing the data. 
		sheet_names (list): List of sheet names in the file. 
		file_name (str): Name of the file from which data was extracted. 

		Returns:
		detailed_metadata_df (pd.DataFrame): DataFrame containing detailed metadata information.
		"""
		detailed_metadata = []
		for sheet in sheet_names:
			df = data[sheet]
			for col in df.columns:
				detailed_metadata.append([file_name, sheet, col])
		return pd.DataFrame(detailed_metadata, columns=['File Name', 'Sheet Name', 'Field Name'])

	# Read the first and second file
	data1, sheet_names1 = read_file(file1_path, skip_rows)
	data2, sheet_names2 = read_file(file1_path, skip_rows)

	# Extract file names from paths
	file1_name = os.path.basename(file1_path)
	file2_name = os.path.basename(file2_path)

	# Create metadata DataFrames for both files
	metadata_df1 = create_metadata_df(data1, sheet_names1, file1_name)
	metadata_df2 = create_metadata_df(data2, sheet_names2, file2_name)

	# Create detailed metadata DataFrames for both files
	detailed_metadata_df1 = create_detailed_metadata_df(data1, sheet_names1, file1_name)
	detailed_metadata_df2 = create_detailed_metadata_df(data2, sheet_names2, file2_name)

	# Concatenate the metadata DataFrames
	combined_metadata_df = pd.concat([metadata_df1, metadata_df2], axis=0, ignore_index=True)

	# Move the 'Source' column to the first position
	cols = ['Source'] + [col for col in combined_metadata_df.columns if col != 'Source']
	combined_metadata_df = combined_metadata_df[cols]

	# Concatenate the detailed metadata DataFrames
	combined_detailed_metadata_df = pd.concat([detailed_metadata_df1, detailed_metadata_df2], axis=0, ignore_index=True)

	# Create a unique identifier by concatenating 'Sheet Name' and 'Field Name'
	combined_detailed_metadata_df['Combination'] = combined_detailed_metadata_df['Sheet Name'].astype(str) + '_' + combined_detailed_metadata_df['Field Name'].astype(str)

	# Identify unique combinations
	unique_combinations = combined_detailed_metadata_df['Combination'].value_counts()
	unique_combinations = unique_combinations[unique_combinations == 1].index

	# Filter the combined detailed metadata DataFrame to get unique combinations
	unique_detailed_metadata_df = combined_detailed_metadata_df[combined_detailed_metadata_df['Combinations'].isin(unique_combinations)]
	unique_detailed_metadata_df = unique_detailed_metadata_df.drop(columns=['Combination'])

	# Write the results to an Excel file
	with pd.ExcelWriter(output_path, engine='openpyxl') as writer:
		metadata_df1.to_excel(writer, sheet_name='File1 Metadata', index=False)
		metadata_df2.to_excel(writer, sheet_name='File2 Metadata', index=False)
		combined_metadata_df.to_excel(writer, sheet_name='Combined Metadata', index=False)
		combined_detailed_metadata_df.to_excel(writer, sheet_name='Detailed Metadata', index=False)
		unique_detailed_metadata_df.to_excel(writer, sheet_name='Unique Metadata', index=False)
	print(f"Metadata extracted successfully and saved to {output_path}")

# Example usage:
# path1 = '/Users/Local_user/Desktop/VS Code projects/data/file1.xlsx'
# path2 = '/Users/Local_user/Desktop/VS Code projects/data/file2.xlsx'
# out_path = '/Users/Local_user/Desktop/VS Code projects/data/files_metadata_comp.xlsx'
# skip_rows = 1
# extract_metadata(path1, path2, out_path, skip_rows)

# func_meta_03
import pandas as pd
from openpyxl import load_workbook

def extract_values_from_excel(excel_file, row_number):
	# Extracts metadata from the Excel file stored in a specific row from multiple sheets as new sheet
    # Load Excel file using pandas
    xls = pd.ExcelFile(excel_file)
    
    # Create an empty list to store tuples of sheet name and values
    data = []
    
    # Iterate through each sheet in the Excel file
    for sheet_name in xls.sheet_names:
        # Read values from specified row in current sheet
        df = pd.read_excel(excel_file, sheet_name=sheet_name, header=None, skiprows=row_number-1, nrows=1)
        
        # Append each value to data list as a separate row
        for value in df.values.tolist()[0]:
            data.append((sheet_name, value))
    
    # Create a new list of tuples with each value in a separate row and duplicate sheet name
    new_data = []
    for tup in data:
        for value in tup[1:]:
            new_data.append((tup[0], value))
    
    # Create a new DataFrame from new_data list
    df_new = pd.DataFrame(new_data, columns=['Sheet name', 'Values'])
    
    # Write new DataFrame to a new sheet in original Excel file
    book = load_workbook(excel_file)
    writer = pd.ExcelWriter(excel_file, engine='openpyxl') 
    writer.book = book
    df_new.to_excel(writer, index=False)
    writer.save()

file_name = output_file

extract_values_from_excel(file_name, 1)


# func_meta_04
import pandas as pd

def update_excel_column_names(input_path: str, header_row: int = 1):
	"""
	Change column names to all lower case with underscore instead of spaces with header row specific as second parameter (default = 1).
	"""
    # Load the Excel file
	xls = pd.ExcelFile(input_path, engine='openpyxl')
    
    # Dictionary to store dataframes
	sheet_dfs = {}
    
    # Iterate through each sheet
	for sheet_name in xls.sheet_names:
        # Read the sheet with the specified header row
		df = pd.read_excel(xls, sheet_name=sheet_name, header=header_row-1)
        
        # Update column names
		df.columns = [col.lower().replace(' ', '_') for col in df.columns]
        
        # Store the dataframe in the dictionary
		sheet_dfs[sheet_name] = df
    
    # Write the updated dataframes back to the Excel file
	with pd.ExcelWriter(input_path, engine='openpyxl') as writer:
		for sheet_name, df in sheet_dfs.items():
			df.to_excel(writer, sheet_name=sheet_name, index=False)

# Example usage
input_path = 'data/input/metadata_template - Copy.xlsx'
update_excel_column_names(input_path, 1)


# func_meta_05
import pandas as pd

def extract_row_from_file(file_path, row_number, skip_rows=0):
    """
    Extracts a specified row from a file and returns a DataFrame containing the sheet name and extracted values.
    
    Parameters:
    - file_path (str): Path to the input file.
    - row_number (int): The row number to extract (1-based index, 0 for headers).
    - skip_rows (int): Optional parameter to specify how many rows to skip when reading the file.
    
    Returns:
    - DataFrame: A DataFrame with the sheet name and extracted values.
    """
    def extract_from_csv(file_path, row_number, skip_rows):
        df = pd.read_csv(file_path, skiprows=skip_rows)
        if row_number == 0:
            row_data = df.columns.tolist()
        else:
            row_data = df.iloc[row_number - 1].tolist()
        return pd.DataFrame({'Sheet Name': ['CSV'] * len(row_data), 'Value': row_data})
    
    def extract_from_excel(file_path, row_number, skip_rows):
        xls = pd.ExcelFile(file_path)
        output = pd.DataFrame(columns=['Sheet Name', 'Value'])
        for sheet_name in xls.sheet_names:
            df = pd.read_excel(file_path, sheet_name=sheet_name, skiprows=skip_rows)
            if row_number == 0:
                row_data = df.columns.tolist()
            else:
                row_data = df.iloc[row_number - 1].tolist()
            sheet_df = pd.DataFrame({'Sheet Name': [sheet_name] * len(row_data), 'Value': row_data})
            output = pd.concat([output, sheet_df], ignore_index=True)
        return output
    
    # Determine file type and extract accordingly
    if file_path.endswith('.csv'):
        return extract_from_csv(file_path, row_number, skip_rows)
    elif file_path.endswith(('.xlsx', '.xls', '.xlsm')):
        return extract_from_excel(file_path, row_number, skip_rows)
    else:
        raise ValueError("Unsupported file format. Only CSV, XLSX, XLS, and XLSM are supported.")

# Example usage
df = extract_row_from_file('C:\Python repositories\Main project\data\input\Table template.xlsx', 0, skip_rows=0)
print(df)


# func_meta_06
import pandas as pd
import os

def extract_rows_from_folder(folder_path, row_number, skip_rows=0):
    """
    Extracts a specified row from all supported files in a folder and saves the result into an Excel file.
    
    Parameters:
    - folder_path (str): Path to the input folder containing the files.
    - row_number (int): The row number to extract (1-based index, 0 for headers).
    - skip_rows (int): Optional parameter to specify how many rows to skip when reading the files.
    
    Returns:
    - None
    """
    def extract_from_csv(file_path, row_number, skip_rows):
        df = pd.read_csv(file_path, skiprows=skip_rows)
        if row_number == 0:
            row_data = df.columns.tolist()
        else:
            row_data = df.iloc[row_number - 1].tolist()
        return pd.DataFrame({'File Name': [os.path.basename(file_path)] * len(row_data),
                             'Sheet Name': ['CSV'] * len(row_data),
                             'Value': row_data})
    
    def extract_from_excel(file_path, row_number, skip_rows):
        xls = pd.ExcelFile(file_path)
        output = pd.DataFrame(columns=['File Name', 'Sheet Name', 'Value'])
        for sheet_name in xls.sheet_names:
            df = pd.read_excel(file_path, sheet_name=sheet_name, skiprows=skip_rows)
            if row_number == 0:
                row_data = df.columns.tolist()
            else:
                row_data = df.iloc[row_number - 1].tolist()
            sheet_df = pd.DataFrame({'File Name': [os.path.basename(file_path)] * len(row_data),
                                     'Sheet Name': [sheet_name] * len(row_data),
                                     'Value': row_data})
            output = pd.concat([output, sheet_df], ignore_index=True)
        return output
    
    output = pd.DataFrame(columns=['File Name', 'Sheet Name', 'Value'])
    
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        if file_name.endswith('.csv'):
            file_df = extract_from_csv(file_path, row_number, skip_rows)
            output = pd.concat([output, file_df], ignore_index=True)
        elif file_name.endswith(('.xlsx', '.xls', '.xlsm')):
            file_df = extract_from_excel(file_path, row_number, skip_rows)
            output = pd.concat([output, file_df], ignore_index=True)
    
    # Define output file name
    if row_number == 0:
        output_file_name = 'files_headers.xlsx'
    else:
        output_file_name = f'files_row_{row_number}_values.xlsx'
    
    # Save the combined DataFrame to an Excel file
    output.to_excel(os.path.join(folder_path, output_file_name), index=False)

# Example usage (\f string is interpreted as escape character so double backslashes are used)
df = extract_rows_from_folder('C:\\Python repositories\\Main project\\data\\input\\folder', 0, skip_rows=0)


# func_meta_07