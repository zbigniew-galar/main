# func_files_01
def excel_to_csv(input_excel_path, skip_rows):
	"""
	Save Excel to CSV files. 
	Reads an Excel file with all its sheets as separate DataFrames, then saves those as CSV files named the same as input sheets in the same folder as the source Excel file. 
	
	Parameters:
	input_excel_path (str): The path to the input Excel file.
	skip_rows (int): The number of rows to skip when reading any of the sheets. 
	"""
	# Read the Excel file
	excel_file = pd.ExcelFile(input_excel_path)

	# Get the directory of the input Excel file
	directory = os.path.dirname(input_excel_path)

	# Iterate through each sheet
	for sheet_name in excel_file.sheet_names:
		# Read the sheet into a DataFrame, skipping the specified number of rows
		df = pd.read_excel(input_excel_path, sheet_name=sheet_name, skiprows=skip_rows)

		# Construct the output CSV file path
		output_csv_path = os.path.join(directory, f"{sheet_name}.csv")

		# Save the DataFrame as CSV file
		df.to_csv(output_csv_path, index=False)

		print(f"Saved {sheet_name} to {output_csv_path}")

# Example usage:
# excel_path = '/Users/Local_user/Desktop/VS Code projects/Test project/data/excel_file.xlsx'
# skip_rows = 0
# excel_to_csv(excel_path, skip_rows)


# func_files_02
def save_file(data: pd.DataFrame, name: str):
	dump_file_name  = name + '.xlsx'
	data_dump = os.path.join(os.getcwd(), dump_file_name)
	writer = pd.ExceWriter(data_dump, engine='xlsxwriter')
	data.to_excel(writer, sheet_name=name, index=False)
	writer.save()
	print('Data dump at: {}'.format(data_dump))


# func_files_03
def save_local(data: pd.DataFrame, name: str):
	"""
	Save a DataFrame as an Excel file in the local directory.
	
	Parameters:
	data (pd.DataFrame): The DataFrame to be saved.
	name (str): The name of the Excel file (without extension). 
	
	Returns:
	None
	"""
	# Construct the full file name with xlsx extension
	dump_file_name = name + '.xlsx'

	# Ge the full path to the file in the current working directory
	data_dump = os.path.join(os.getcwd(), dump_file_name)

	# Create  an Excel writer object using xlsxwriter engine
	writer = pd.ExcelWriter(data_dump, engine='xlsxwriter')

	# Write the DataFrame to an Excel sheet with the same name as the file
	data.to_excel(writer, sheet_name=name, index=False)

	# Close the writer to save the file
	writer.close()

	# Print the location where the file will be saved
	print('Saving file at: {}'.format(data_dump))


# func_files_04
def  save_excel(out_path: str, data: pd.DataFrame, tab: str, rows: int = 0):
	"""
	Save a DataFrame as an Excel file in a specified directory with an optional starting row. 

	Parameters:
	out_path (str): The full path where the Excel file will be saved.
	data (pd.DataFrame): The DataFrame to be saved.
	tab (str): The name of the excel sheet.
	rows (int, optional): The starting row for the data in the Excel sheet. Default is 0.

	Returns:
	None
	"""
	# Create an Excel writer object using xlsxwriter engine
	writer = pd.ExcelWriter(out_path, engine='xlsxwriter')

	# Write the DataFrame to an Excel sheet with the specified name and starting row
	data.to_excel(writer, sheet_name=tab, index=False, startrow=rows)

	# Close the writer to save the file
	writer.close()

	# Print the location where the file is saved
	print('Saving file at: {}'.format(out_path))


# func_files_05
def file_load(file_path: str, tab: str, skipped_rows: int) -> pd.DataFrame:
	# Load data from an Excel or CSV file with tab selection and number of rows to skip
	if (file_path[len(file_path)-5:]=='.xlsx' or
	file_path[len(file_path)-5:]=='.xlsm' or
	file_path[len(file_path)-4:]=='.csv'):
		try:
			full_path - file_path
			data = pd.read_excel(full_path, sheet_name=tab, keep_default_na=False, skiprows=skipped_rows)
		except FileNotFoundError:
			full_path = file_path
			data = pd.read_excel(full_path, sheet_name=tab, keep_default_na=False, skiprows=skipped_rows)
		except:
			full_path = file_path
			data = pd.read_csv(full_path, keep_default_na=False, skiprows=skipped_rows)
		finally:
			print("{}".format(data.shape))
			print("{}".format(data.columns))
	else:
		try:
			full_path = file_path + '.xlsx'
			data = pd.read_excel(full_path, sheet_name=tab, deep_default_na=False, skiprows=skipped_rows)
		except FileNotFoundError:
			full_path = file_path + '.xlsm'
			data = pd.read_excel(full_path, sheet_name=tab, keep_default_na=False, skiprows=skipped_rows)
		except:
			full_path = file_path + '.csv'
			data = pd.read_csv(full_path, keep_default_na=False, skiprows=skipped_rows)
		finally:
			print("{}".format(data.shape))
			print("{}".format(data.columns))
		return data


# func_files_06
def file_read(file_path: str, tab: str = 0, skipped_rows: int = None) -> pd.DataFrame:
	"""
	Load data from an Excel or CSV file with optional sheet/tab selection and row skipping.
	
	Parameters:
	file_path (str): Path to the input file (Excel or CSV). 
	tab (str, optional): Name or index of the sheet/tab to load from an Excel file. Default is 0 (first sheet). 
	skipped_rows (int, optional): Number of rows to skip at the beginning of the file. Default is None. 
	
	Returns:
	pd.DataFrame: Loaded data as a DataFrame. Returns None if an error occurs. 
	
	Raises:
	ValueError: If the file format is unsupported. 
	FileNotFoundError: If the file is not found at the specified path.
	"""
	try:
		if file_path.endswith(('xlsxl', '.xlsm')):
			# Load data from and Excel file with optional sheet/tab selection and row skipping
			data = pd.read_excel(file_path, sheet_name=tab, skiprows=skipped_rows)
		elif file_path.endswith('.csv'):
			# Load data from CSV file with optional row skipping
			data = pd.read_csv(file_path, skiprows=skipped_rows)
		else:
			raise ValueError("Invalid file format. Only xlsx, xlsm, and csv files are supported.")
	except FileNotFoundError:
		print(f"File not found: {file_path}")
		return None
	except Exception as e:
		print(f"An error occured: {e}")
		return None

	# Print the shape and columns of the loaded DataFrame
	print(f"Data shape: {data.shape}")
	print(f"Data columns: {data.columns}")

	return data

# Example usage:
# df  = file_read('data.xlsx', tab='Sheet1', skipped_rows=2)
# df  = file_read('data.csv'', skipped_rows=0)


# func_files_07
def load_excel(file_path, skip_rows=0):
	"""
	Load Excel and provide a summary of the DataFrames created from each sheet. 
	Also creates a metadata summary sheet with sheet names as column names and field names as values. 

	Parameters:
	file_path (str): The path to the Excel file.
	skip_rows (int, optional): The starting row for data ingestion from all sheets (default is 0).
	
	Returns:
	dataframes (dict): A dictionary containing DataFrames for each sheet.
	summary_df (pd.DataFrame): A summary DataFrame with DataFrames names and sheet names.
	metadata_summary_df (pd.DataFrame): A metadata summary DataFrame with sheet names as column names and field names as values. 
	"""
	# Step 1: Read the Excel file and get all sheet names
	xls = pd.ExcelFile(file_path)
	sheet_names = xls.sheet_names

	# Step 2: Create a dictionary to store DataFrames
	dataframes = {}

	# Step 3: Lists to store DataFrame names and sheet names for the summary
	df_names = []
	sheet_names_list = []

	# Step 4: Dictionary to store metadata for each sheet
	metadata = {}

	# Step 5: Variable to track the maximum number of columns in any sheet
	max_columns = 0

	# Step 6: Loop through each sheet and read it into a DataFrame
	for i, sheet_name in enumerate(sheet_names):
		df_name = f'df{i+1}'

		# Read the sheet into a DataFrame starting from a specified row
		df = pd.read_excel(file_path, sheet_name=sheet_name, skiprows=skip_rows)
		dataframes[df_name] = df

		# Add the DataFrame name and sheet name to the lists
		df_names.append(df_name)
		sheet_names_list.append(sheet_name)

		# Update the maximum number of columns if necessary
		max_columns = max(max_columns, len(df.columns))

		# Create a metadata list starting with the column names
		metadata[sheet_name] = list(df.columns)

	# Step 7: Determine the maximum number of rows needed for the metadata summary
	max_rows = max(len(columns) for columns in metadata.values())

	# Step 8: Pad metadata list to ensure they all have the same number of rows
	for sheet_name, columns in metadata.items():
		columns.extend([None] * (max_rows - len(columns)))

	# Step 9: Create the metadata summary DataFrame
	metadata_summary_df = pd.DataFrame(metadata)
	
	# Step 10: Create the summary DataFrame
	summary_df = pd.DataFrame({
		'DataFrame Name': df_names,
		'Sheet Name': sheet_names_list
	})

	return dataframes, summary_df, metadata_summary_df
"""
file_path = '/Users/Local_user/VS Code projects/Test project/data/excel_file.xlsx'
skip_rows = 1 # Start reading from the second row (0-indexed row 1)

# Call the function
dataframes, summary_df, metadata_summary_df = load_excel(file_path, skip_rows)

# Access individual DataFrames
df1 = dataframes['df1']

# Display the results
print("DataFrames Dictionary")
for df_name, df in dataframes.items():
	print(f"\n{df_name}:")
	print(df.head())

print("\nSummary DataFrame:")
print(summary_df)

print("\nMetadata Summary DataFrame:")
print(metadata_summary_df)
"""


# func_files_08
import os
import pandas as pd

def read_files_in_folder(folder_path: str, skip_rows: int = 0) -> dict:
    """
    Reads all files in a given folder from CSV, XLSX, XLS, XLSB, and XLSM formats.
    For Excel files, all sheets are read. Returns a dictionary of DataFrames.
    The dictionary keys are either the CSV filename (without extension) or Excel sheet names.
    Spaces in filenames are replaced with underscores.

    Args:
        folder_path (str): Path to the folder containing the files.
        skip_rows (int): Number of rows to skip when reading files (default is 0).

    Returns:
        dict: Dictionary with DataFrame objects, keyed by sheet name or file name.
    """
    
    # Initialize an empty dictionary to store the DataFrames
    dataframes = {}
    
    # List all files in the folder
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        
        # Skip if it's not a file
        if not os.path.isfile(file_path):
            continue

        # Determine the file type by extension
        extension = filename.lower().split('.')[-1]
        file_base = '.'.join(filename.split('.')[:-1])  # Remove the extension
        file_base = file_base.replace(" ", "_")  # Replace spaces with underscores
        
        try:
            if extension == 'csv':
                # Read CSV file, skip the specified rows, and store DataFrame
                df = pd.read_csv(file_path, skiprows=skip_rows)
                # Use the file base name (without extension) as the key
                dataframes[file_base] = df
                
            elif extension in ['xlsx', 'xls', 'xlsm', 'xlsb']:
                # Read Excel file, skip rows, and get all sheets
                excel_sheets = pd.read_excel(file_path, sheet_name=None, skiprows=skip_rows)
                # Add each sheet as a separate DataFrame with the sheet name as the key
                for sheet_name, df in excel_sheets.items():
                    # Name format: "filebasename_sheetname"
                    sheet_key = f"{file_base}_{sheet_name.replace(' ', '_')}"
                    dataframes[sheet_key] = df
                    
            else:
                # Unsupported file format, skip the file
                print(f"Skipping unsupported file format: {filename}")
                
        except Exception as e:
            # Handle any exceptions that occur during file reading
            print(f"Error reading file {filename}: {str(e)}")

    print("DataFrames that were read:")
    for df_name in dataframes.keys():
        print(df_name)
    
    return dataframes


# Example usage
df_dict = read_files_in_folder("C:\Python repositories\Main project\data\input\input_folder")
"""
# Display the first DataFrame from the dictionary
# Check if the dictionary is not empty
if df_dict:
    # Get the first DataFrame's key
    first_df_key = list(df_dict.keys())[0]
    
    # Display the first 3 rows of the first DataFrame
    print(f"First 3 rows of the DataFrame '{first_df_key}':")
    print(df_dict[first_df_key].head(3))
else:
    print("No DataFrames were found.")
"""
# Assign first DataFrame from the dictionary as df1
df1 = df_dict[list(df_dict.keys())[0]]
print(df1.columns)


# func_files_09
import pandas as pd
from typing import Optional

def load_file(file_path: str, sheet_name: Optional[str] = None, skip_rows: Optional[int] = 0) -> pd.DataFrame:
    """
    Load a CSV or Excel file into a DataFrame.

    Parameters:
    - file_path (str): The path to the file to be loaded.
    - sheet_name (Optional[str]): The name of the sheet in an Excel file. Default is None.
    - skip_rows (Optional[int]): The number of rows to skip when loading the file. Default is 0.

    Returns:
    - DataFrame: The loaded data.
    """
    # Check the file extension to determine the file type
    file_extension = file_path.split('.')[-1].lower()
    
    try:
        if file_extension == 'csv':
            # Load CSV file
            df = pd.read_csv(file_path, skiprows=skip_rows)
        elif file_extension in ['xls', 'xlsx', 'xlsm']:
            # Load Excel file
            df = pd.read_excel(file_path, sheet_name=sheet_name, skiprows=skip_rows)
        else:
            raise ValueError("Unsupported file type. Please provide a CSV or Excel file.")
        print(df.shape, df.columns)
        return df
    
    except FileNotFoundError:
        print(f"Error: The file at {file_path} was not found.")
        raise
    except Exception as e:
        print(f"An error occurred: {e}")
        raise

# Example usage:
df1 = load_file('C:\Python repositories\Main project\data\input\mapping_file.csv')
df2 = load_file('C:\Python repositories\Main project\data\input\Table template.xlsx', sheet_name='Plan', skip_rows=0)


# func_files_10
