# func_misc_01
def absolute_values(data: pd.DataFrame, list_cols: list) -> pd.DataFrame:
	"""
	Calculate absolute values of specified columns in a DataFrame.
	
	Parameters:
	data (pd.DataFrame): The input DataFrame.
	list_cols (list): List of column names to calculate absolute values for. Columns with string data types will be converted to float. 
	
	Returns:
	pd.DataFrame: DataFrame with absolute values for specified columns.
	"""
	for col in list_cols:
		if data[col].dtype not in ['int64','float64']:
			data[col] = data[col].astype(float)
		data[col] - data[col].apply(abs)
	return data


# func_misc_02
def concat_data(data1:pd.DataFrame, data2:pd.DataFrame):
	data_files = [data1,data2]
	data - pd.concat(data_files, ignore_index=True, sort=False)
	return data


# func_misc_03
def concatenate_dataframes(df1, df2, method) -> pd.DataFrame:
	"""
	Concatenate two DataFrames either by common column names or by column positions. 
	
	Parameters:
	df1 (pd.DataFrame): The first DataFrame. 
	df2 (pd.DataFrame): The second DataFrame.
	method (str): The method of concatenation. Either "name" or "position".

	Returns:
	pd.DataFrame: The concatenated DataFrame.
	"""
	if method not in ["name", "position"]:
		raise ValueError("Method must be either 'name' or 'position'")
	if method == "name":
		# Find common columns
		common_columns = df1.columns.intersection(df2.columns)
		# Concatenate only the common columns
		result = pd.concat([df1[common_columns], df2[common_columns]], axis=0)

	elif method == "position":
		# Determine the maximum number of columns
		max_columns = max(df1.shape[1], df2.shape[1])

		# Create empty DataFrames with the same number of columns
		df1_extended = pd.DataFrame(index=df1.index, columns=range(max_columns))
		df2_extended = pd.DataFrame(index=df2.index, columns=range(max_columns))

		# Copy the original values to the extended DataFrames
		df1_extended.iloc[:, :df1.shape[1]] = df1.values
		df2_extended.iloc[:, :df2.shape[1]] = df2.values

		# Concatenate DataFrames by position
		result = pd.concat([df1_extended, df2_extended], axis=0, ignore_index=True)

		# Rename columns to numbers starting from 1
		result_columns = range(1, result.shape[1] + 1)
	return result

# Example usage:
# df1 = pd.DataFrame({'A': [1, 2], 'B': [3, 4], 'C': [5, 6]})
# df2 = pd.DataFrame({'A': [7, 8], 'B': [9, 10], 'C': [11, 12]})

# Concatenate by common column names
# concatenate_dataframes(df1, df2, 'name')

# Concatenate by column positions
# concatenate_dataframes(df1, df2, 'position')


# func_misc_04
def columns_to_template(df: pd.DataFrame, columns_list: list) -> pd.DataFrame:
	"""
	Adjust DataFrame columns to match a specified template. 
	
	Parameters:
	df (pd.DataFrame): The input DataFrame.
	columns_list (list): List of column names representing the template.
	
	Returns:
	pd.DataFrame: DataFrame adjusted to the template, with missing columns reported.
	"""
	# Identify missing columns
	missing_columns = [col for col in columns_list if col not in df.columns]

	# Print missing columns
	if missing_columns:
		print(f"The following columns from the template are not present in the DataFrame: {missing_columns}")
	else:
		print("DataFrame's metadata is the same as template.")
	# Filter and reorder columns, using only columns that are present in the DataFrame
	present_columns = [col for col in columns_list if col in df.columns]
	adjusted_columns = df[present_columns].copy()
	return adjusted_df


# func_misc_05
def field_duplicates_in_folder(input_folder, skiprows=0):
	"""
	Duplicate check in all the columns in all the sheets in all the files in a folder.
	Function to check for duplicated values in all columns of all sheets in supported Excel and CSV files within a specified folder. Generates a report indicating which columns have duplicated values and an additional report for columns with inconsistent duplicate indications across files. 

	Parameters:
	input_folder (str): Path to the folder containing the files. 
	skiprows (int): Number of rows to skip at the beginning of each sheet (default is 0).

	Returns:
	None: The function saves an Excel report in the same folder as the input folder.
	"""
	# Supported file extensions
	supported_extensions = ['.xlsx', '.xls', '.xlsm', '.xlsb', '.csv']

	# Initialize an empty list to store the report data
	report_data = []

	# Dictionary to track duplicate indications for each sheet and column combination
	duplicate_tracker = defauldic(list)

	# Iterate over all files in the input folder
	for file_name in os.listdir(input_folder):
		# Get the full path of the file
		file_path = os.path.join(input_folder, file_name)

		# Determine the file extension
		file_extension = os.path.splitext(file_name)[1].lower()

		# Check if the file is supported
		if file_extension in supported_extensions:
			# Read the file based on its extension
			if file_extension in ['.xlsx', '.xls', '.xlsm']:
				# Read all sheets from the Excel file using openpyxl for xlsx, xls and xlsm formats
				engine = 'openpyxl' if file_extension in ['.xlsx', '.xlsm'] else 'xlrd'
				excel_file = pd.read_excel(file_path, sheet_name=None, skiprows=skiprows, engine=engine)
			elif file_extension == '.xlsb':
				# Read all sheets from the Excel file using pyxlsb
				excel_file = pd.read_excel(file_path, sheet_name=None, skiprows=skiprows, engine='pyxlsb')
			elif file_extension == '.csv':
				# Read the CSV file as a single sheet name 'Sheet1'
				excel_file = {'Sheet1': pd.read_csv(file_path, skiprows=skiprows)}
			else:
				continue # Skip unsupported files

			# Iterate through each sheet in the file
			for sheet_name, df in excel_file.items():
				# Iterate through each column in the sheet
				for column in df.columns:
					# Check for duplicated values in the column
					has_duplicates  = df[column].duplicated().any()
					# Append the result to the report data
					report_data.append([file_name, sheet_name, column, "Yes" if has_duplicates else "No"])
					# Track the duplicate indication for the sheet and column combination
					duplicate_tracker[(sheet_name, column)].append("Yes" if has_duplicates else "No")

	# Create a DataFrame for the main report
	report_df = pd.DataFrame(report_data, columns=['File Name', 'Sheet Name', 'Column Name', 'Has Duplicates'])

	# Identify inconsistent duplicate indications
	inconsistent_data = []
	for (sheet_name, column), indications in duplicate_tracker.items():
		if len(set(indications)) > 1: # Check if there are inconsistent indications
			inconsistent_data.append([sheet_name, column, ", ".join(indications)])

	# Create a DataFrame for the inconsistent indications report
	inconsistent_df = pd.DataFrame(inconsistent_data, columns=['Sheet Name', 'Column Name', 'Duplicate Indications'])

	# Define the output path for the report
	folder_name = os.path.basename(os.path.normpath(input_folder))
	output_path = os.path.join(input_folder, f"{folder_name}_duplicates.xlsx")

	# Save the reports as an Excel file with multiple sheets 
	with pd.ExcelWriter(output_path, engine='openpyxl') as writer:
		report_df.to_excel(writer, sheet_name='Duplicate Report', index=False)
		inconsistent_df.to_excel(writer, sheet_name='Inconsistent Duplicates', index=False)

	# Print a message indicating where the report has been saved
	print(f"Report saved to {output_path}")

# Example usage:
# path = '/Users/Local_user/Desktop/VS Code projects/Test project/data/Models'
# field_duplicates_in_folder(path, skiprows=1)


# func_misc_06
from datetime import timedelta, datetime

def arrival_time(hours=0):
	# Shows a specific time x hours from now
    now = datetime.now()
    when = now + timedelta(hours=hours)
    output = when.strftime("%A %H:%M")
    return print(f"{hours} hours from now will be {output}")
    
hours = 120
arrival_time(hours)


# func_misc_07
import pandas as pd
import numpy as np

def haversine(lat1, lon1, lat2, lon2):
	# Calculate distance between location with latitude and longitude assuming Earth is a sphere:
    # Convert latitude and longitude from degrees to radians
    lat1, lon1, lat2, lon2 = map(np.radians, [lat1, lon1, lat2, lon2])

    # Haversine formula
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = np.sin(dlat / 2.0)**2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon / 2.0)**2
    c = 2 * np.arcsin(np.sqrt(a))

    # Radius of Earth in kilometers (mean radius)
    R = 6371.0
    return c * R

def calculate_distances(df, location_col, lat_col, lon_col):
    # Ensure the DataFrame contains the required columns
    if not all(col in df.columns for col in [location_col, lat_col, lon_col]):
        raise ValueError("The DataFrame must contain the specified columns for location, latitude, and longitude.")
    
    # Create a list to store the results
    results = []

    # List of columns to include in the output (excluding the lat/lon columns which are handled separately)
    additional_columns = [col for col in df.columns if col not in [location_col, lat_col, lon_col]]

    # Iterate over each pair of locations
    for i in range(len(df)):
        for j in range(i+1, len(df)):
            location1 = df.iloc[i]
            location2 = df.iloc[j]
            dist = haversine(location1[lat_col], location1[lon_col], location2[lat_col], location2[lon_col])
            
            result = {
                f"{location_col}_1": location1[location_col],
                f"{location_col}_2": location2[location_col],
                f"{lat_col}_1": location1[lat_col],
                f"{lon_col}_1": location1[lon_col],
                f"{lat_col}_2": location2[lat_col],
                f"{lon_col}_2": location2[lon_col],
                'distance_km': dist
            }
            
            # Add additional columns to the result
            for col in additional_columns:
                result[f"{col}_1"] = location1[col]
                result[f"{col}_2"] = location2[col]
            
            results.append(result)

    # Convert the list of results into a DataFrame
    distance_df = pd.DataFrame(results)

    return distance_df

# Example usage
data = {
    'location': ['A', 'B', 'C'],
    'latitude': [52.5200, 48.8566, 51.5074],
    'longitude': [13.4050, 2.3522, -0.1276],
    'other_column': [1, 2, 3]
}

df = pd.DataFrame(data)
result = calculate_distances(df, 'location', 'latitude', 'longitude')
print(result)


# func_misc_08
import pandas as pd
import numpy as np

def vincenty_distance(lat1, lon1, lat2, lon2):
	# Calculate distance between location with latitude and longitude assuming Earth is a flatten spheroid:
    # WGS-84 ellipsiod parameters
    a = 6378137.0  # semi-major axis in meters
    f = 1 / 298.257223563  # flattening
    b = (1 - f) * a  # semi-minor axis

    # Convert latitude and longitude from degrees to radians
    lat1, lon1, lat2, lon2 = map(np.radians, [lat1, lon1, lat2, lon2])

    U1 = np.arctan((1 - f) * np.tan(lat1))
    U2 = np.arctan((1 - f) * np.tan(lat2))
    L = lon2 - lon1

    lambda_ = L
    iter_limit = 100
    for _ in range(iter_limit):
        sin_lambda = np.sin(lambda_)
        cos_lambda = np.cos(lambda_)
        sin_sigma = np.sqrt((np.cos(U2) * sin_lambda)**2 +
                            (np.cos(U1) * np.sin(U2) - np.sin(U1) * np.cos(U2) * cos_lambda)**2)
        if sin_sigma == 0:
            return 0  # co-incident points
        cos_sigma = np.sin(U1) * np.sin(U2) + np.cos(U1) * np.cos(U2) * cos_lambda
        sigma = np.arctan2(sin_sigma, cos_sigma)
        sin_alpha = np.cos(U1) * np.cos(U2) * sin_lambda / sin_sigma
        cos2_alpha = 1 - sin_alpha**2
        if cos2_alpha == 0:
            cos2_sigma_m = 0  # equatorial line
        else:
            cos2_sigma_m = cos_sigma - 2 * np.sin(U1) * np.sin(U2) / cos2_alpha
        C = f / 16 * cos2_alpha * (4 + f * (4 - 3 * cos2_alpha))
        lambda_prev = lambda_
        lambda_ = L + (1 - C) * f * sin_alpha * (
            sigma + C * sin_sigma * (cos2_sigma_m + C * cos_sigma * (-1 + 2 * cos2_sigma_m**2))
        )
        if abs(lambda_ - lambda_prev) < 1e-12:
            break
    else:
        raise ValueError("Vincenty formula failed to converge")

    u2 = cos2_alpha * (a**2 - b**2) / b**2
    A = 1 + u2 / 16384 * (4096 + u2 * (-768 + u2 * (320 - 175 * u2)))
    B = u2 / 1024 * (256 + u2 * (-128 + u2 * (74 - 47 * u2)))
    delta_sigma = B * sin_sigma * (
        cos2_sigma_m + B / 4 * (cos_sigma * (-1 + 2 * cos2_sigma_m**2) -
                                B / 6 * cos2_sigma_m * (-3 + 4 * sin_sigma**2) * (-3 + 4 * cos2_sigma_m**2))
    )
    s = b * A * (sigma - delta_sigma)

    return s / 1000  # convert to kilometers

def calculate_distances(df, location_col, lat_col, lon_col):
    # Ensure the DataFrame contains the required columns
    if not all(col in df.columns for col in [location_col, lat_col, lon_col]):
        raise ValueError("The DataFrame must contain the specified columns for location, latitude, and longitude.")
    
    # Create a list to store the results
    results = []

    # List of columns to include in the output (excluding the lat/lon columns which are handled separately)
    additional_columns = [col for col in df.columns if col not in [location_col, lat_col, lon_col]]

    # Iterate over each pair of locations
    for i in range(len(df)):
        for j in range(i+1, len(df)):
            location1 = df.iloc[i]
            location2 = df.iloc[j]
            dist = vincenty_distance(location1[lat_col], location1[lon_col], location2[lat_col], location2[lon_col])
            
            result = {
                f"{location_col}_1": location1[location_col],
                f"{location_col}_2": location2[location_col],
                f"{lat_col}_1": location1[lat_col],
                f"{lon_col}_1": location1[lon_col],
                f"{lat_col}_2": location2[lat_col],
                f"{lon_col}_2": location2[lon_col],
                'distance_km': dist
            }
            
            # Add additional columns to the result
            for col in additional_columns:
                result[f"{col}_1"] = location1[col]
                result[f"{col}_2"] = location2[col]
            
            results.append(result)

    # Convert the list of results into a DataFrame
    distance_df = pd.DataFrame(results)

    return distance_df

# Example usage
data = {
    'location': ['A', 'B', 'C'],
    'latitude': [52.5200, 48.8566, 51.5074],
    'longitude': [13.4050, 2.3522, -0.1276],
    'other_column': [1, 2, 3]
}

df = pd.DataFrame(data)
result = calculate_distances(df, 'location', 'latitude', 'longitude')
print(result)


# func_misc_09
import pandas as pd

def calculate_absolute_values(df, columns):
    """
    Calculate the absolute values of specified columns in a DataFrame.
    
    Parameters:
    df (pd.DataFrame): The input DataFrame.
    columns (list): The list of column names to calculate absolute values for.
    
    Returns:
    pd.DataFrame: A new DataFrame with the absolute values of the specified columns.
    """
    
    # Validate input types
    if not isinstance(df, pd.DataFrame):
        raise TypeError("The input df must be a pandas DataFrame.")
    
    if not isinstance(columns, list):
        raise TypeError("The columns parameter must be a list.")
    
    for col in columns:
        if not isinstance(col, str):
            raise TypeError("Each column name in the columns list must be a string.")
        if col not in df.columns:
            raise ValueError(f"The column '{col}' is not present in the DataFrame.")
    
    # Create a copy of the DataFrame to avoid modifying the original DataFrame
    df_abs = df.copy()
    
    # Calculate the absolute values for the specified columns
    for col in columns:
        df_abs[col] = df_abs[col].abs()
    
    return df_abs

# Example usage
if __name__ == "__main__":
    # Sample DataFrame
    data = {
        'A': [-1, -2, 3, -4],
        'B': [5, -6, -7, 8],
        'C': [-9, 10, -11, 12]
    }
    df = pd.DataFrame(data)
    
    # Columns to calculate absolute values for
    columns = ['A', 'B']
    
    # Calculate absolute values
    df_abs = calculate_absolute_values(df, columns)
    
    # Display the result
    print(df_abs)
    

# func_misc_10
import pandas as pd
import numpy as np

def adjust_dataframe_to_template(df: pd.DataFrame, columns: list) -> pd.DataFrame:
    """
    Adjust the DataFrame to match the template of specified columns.

    Parameters:
    df (pd.DataFrame): Input DataFrame to be adjusted.
    columns (list): List of columns that should be present in the DataFrame.

    Returns:
    pd.DataFrame: Adjusted DataFrame with columns added and reordered as per the template.
    """
    # Identify missing columns
    missing_columns = [col for col in columns if col not in df.columns]
    
    # Print missing columns
    if missing_columns:
        print(f"Missing columns: {missing_columns}")
    
    # Add missing columns with NaN values
    for col in missing_columns:
        df[col] = np.nan
    
    # Reorder dataframe columns to match the template
    df = df[columns]
    
    return df

# Example usage
if __name__ == "__main__":
    # Create a sample dataframe
    sample_data = {
        'A': [1, 2, 3],
        'B': [4, 5, 6]
    }
    df = pd.DataFrame(sample_data)
    
    # Define the template columns
    template_columns = ['A', 'B', 'C', 'D']
    
    # Adjust dataframe to match the template
    adjusted_df = adjust_dataframe_to_template(df, template_columns)
    
    print(adjusted_df)
    

# func_misc_11