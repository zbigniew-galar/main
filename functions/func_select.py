# func_select_01
def filter_rows(input_df: pd.DataFrame, column_name: str, values_list: list, option: str) -> pd.DataFrame:
	"""
	Filters the DataFrame based on the specified column and list of values.
	
	Parameters:
	input_df (pd.DataFrame): The input DataFrame.
	column_name (str): The column based on which the filtering is done. 
	values_list (list): The list of values for filtering. 
	option (str): A string that can be either 'incl' or 'excl'.
	
	Returns:
	pd.DataFrame: The filtered DataFrame.
	"""
	# Validate input parameters
	if not isinstance(input_df, pd.DataFrame):
		raise ValueError("input_df must be a pandas DataFrame")
	
	if column_name not in input_df.columns:
		raise ValueError(f"Column '{columns_name}' does not exist in the DataFrame")

	if option not in ['incl', 'excl']:
		raise ValueError("Option must be either 'incl' or 'excl'.")

	# Filter the DataFrame based on the option
	if option == 'incl':
		filtered_df = input_df[input_df[column_name].isin(values_list)]
	elif option == 'excl':
		filtered_df = input_df[~input_df[column_name].isin(values_list)]
	return filtered_df
"""
# Filter rows based on the list of values including or excluding 
filter_values = [8091813]
filtered = filter_rows(inv, 'productId', filter_values, 'incl')
# Filter chain with other columns
filter_values = ['MR21']
filtered = filter_rows(filtered, 'locationId', filter_values, 'incl')
# Display the results
print(filtered.head(20)), print(filtered.shape)
"""


# func_select_02
def single_fil_col(data: pd.DataFrame, fil_col: str, fil_val):
	"""
	Filtering rows that contain in column certain values. 
	This function filters out rows from the DataFrame that contain a specific value in the specific column. 

	Parameters:
	data (pd.DataFrame): The DataFrame to be filtered. 
	fil_col (str): The column to filter on. 
	fil_val (str): The value to filter out. 

	Returns:
	pd.DataFrame: The filtered DataFrame.
	"""
	# Add option of exluding NaN values, many values
	fitered = data[(data[fil_col]==fil_val)].index
	print("No of rows before filtering: {}".format(data.shape[0]))
	data.drop(filtered, inplace=True)
	data.reset_index(inplace=True, drop=True)
	print("No of rows after filtering: {}".format(data.shape[0]))
	return data


# func_select_03
import pandas as pd

def filter_dataframe(df: pd.DataFrame, column: str, values: list, mode: str) -> pd.DataFrame:
    """
    Filter a DataFrame based on values in a specified column.

    Parameters:
    df (pd.DataFrame): The input DataFrame to be filtered.
    column (str): The name of the column to filter on.
    values (list): The list of values to filter by.
    mode (str): The mode of filtering - "in" to include rows, "out" to exclude rows.

    Returns:
    pd.DataFrame: The filtered DataFrame.
    """
    
    # Validate mode parameter
    if mode not in ['in', 'out']:
        raise ValueError("Mode should be either 'in' or 'out'")
    
    # Check if the specified column exists in the DataFrame
    if column not in df.columns:
        raise ValueError(f"Column '{column}' does not exist in the DataFrame")
    
    # Filter the DataFrame based on the mode
    if mode == 'in':
        filtered_df = df[df[column].isin(values)]
    else:  # mode == 'out'
        filtered_df = df[~df[column].isin(values)]
    
    return filtered_df

# Example usage:
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [24, 27, 22, 32],
    'City': ['New York', 'Los Angeles', 'New York', 'Chicago']
}
df = pd.DataFrame(data)
filtered_df_in = filter_dataframe(df, 'City', ['New York', 'Chicago'], 'in')
filtered_df_out = filter_dataframe(df, 'City', ['New York', 'Chicago'], 'out')
print(filtered_df_in)
print(filtered_df_out)


# func_select_04
