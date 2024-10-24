# func_aggr_01
def aggregate_rows(df, key, col_name, agg_type):
	"""
	Aggregate single column with different types of aggregation with sorting of the results.

	Parameters:
	df (pd.DataFrame): The DataFrame to perform aggregation on. 
	key (str): The column name to group by. 
	col_name (str): The column name to perform aggregation on. 
	agg_type (str): The type of aggregation to perform, Options are: 'sum', 'count', 'mean', 'median', 'max', 'min'.

	Returns:
	pd.DataFrame: A DataFrame with the aggregated and sorted data.
	"""
	# Check if the provided type is valid
	valid_agg_types = ['sum', 'count', 'mean', 'median', 'max', 'min']
	if agg_type not in valid_agg_types:
		raise ValueError(f"Invalid aggregation type. Expected one of : {valid_agg_types}")

	# Perform the aggregation
	data = df.groupby(key)[col_name].agg([agg_type])

	# Reset the index
	data.reset_index(inplace=True)

	# Sort the results
	data = data.sort_values(by=(agg_type), ascending=True)

	return data


# func_aggr_02
def agg_df(df, key_cols, agg_cols, agg_type):
	"""
	Aggregates a DataFrame based on specified key columns, numerical columns, ang aggregation type.

	Parameters:
	df (pd.DataFrame): The input Dataframe. 
	key_columns (list): List of key columns to group by. 
	numerical_columns (list): List of numerical columns to aggregate. 
	agg_type (str): Type of aggregation ('sum', 'count', 'mean', 'median', 'max', 'min').

	Returns:
	pd.DataFrame: Aggregated DataFrame. 
	"""
	# Validate the aggregation type
	valid_agg_types = ['sum', 'count', 'mean', 'median', 'max', 'min']
	if agg_type not in valid_agg_types:
		raise ValueError(f"Invalid aggregation type. Expected one of {valid_agg_types}, got {agg_type}")

	# Validate numerical columns
	for col in agg_cols:
		if col not in df.columns:
			raise ValueError(f"Column '{col}' not found in DataFrame")

	# Perform the aggregation
	if agg_type == 'median':
		# Median is not directly available as a string method in groupby.agg
		aggregated_df = df.groupby(key_cols)[agg_cols].median().reset_index()
	else:
		aggregated_df = df.groupby(key_cols)[agg_cols].agg(agg_type).reset_index()

	return aggregated_df

# Example usage:
# Filtration of columns
# df = pr_loc[['productId', 'locationId']]
# Key columns to aggregate on
# key_cols = ['locationId']
# Columns to aggregate
# agg_cols = ['Value']
# Aggregation type
# ['sum', 'count', 'mean', 'median', 'max', 'min']
# agg_type = 'median'
# aggr = agg_df(df, key_cols, agg_cols, agg_type)
# Display the result
# print(aggr.head())


# func_aggr_03
def count_aggr(data: pd.DataFrame, list_cols: list) -> pd.DataFrame:
	"""
	Aggregates DataFrame based on list of columns and count occurrences.
	
	Parameters:
	data (pd.DataFrame): The input DataFrame
	list_cols (list): List of column names to group by.
	
	Returns:
	pd.DataFrame: Aggregated DataFrame with counts.
	"""
	data = data.rename(columns={str(list_cols[0]): 'Count'})
	data[list_cols[0]] = data['Count']
	list_cols = list_cols + ['Count']
	data = data.groupby(list_cols, as_index=False)['Count'].count()
	print(f"Shape of the aggregated data: {data.shape}")
	print(f"Columns of the aggregated data: {data.columns}")
	return data


# func_aggr_04
def sum_aggr(data: pd.DataFrame, list_cols: list, sum_col: str):
	"""
	Aggregate a DataFrame based on key columns and sum a specified column. 
	This function groups the DataFrame by the specified key columns and sums the values in the specified column. 

	Parameters:
	data (pd.DataFrame): The DataFrame to be aggregated. 
	list_cols (list): The list of key columns to group by. 
	sum_col (str): The column to sum. 

	Returns:
	pd.DataFrame: The aggregated DataFrame. 
	"""
	print("No of rows before aggregation: {}".format(data.shape[0]))
	
	# Convert the column to be summed to float
	data[sum_col] = data[sum_col].astype(float)
	
	# Group by the key columns and sum the specified column
	data = data.groupby(list_cols, as_index=False)[sum_col].sum()

	# Convert the summed column back to integer
	data[sum_col] = data[sum_col].astype(int)
	
	print("No of rows after aggregation: {}".format(data.shape[0]))
	print("{}".format(data.columns))
	
	return data


# func_aggr_05
import pandas as pd

def rows_per_value(df, key, col_name, aggregation):
    """  
    Aggregates the rows of a DataFrame based on a specified key and aggregation type.
    Parameters:
    df (pd.DataFrame): The input DataFrame.
    key (str): The column name to group by.
    col_name (str): The column name from which to take values for aggregation.
    aggregation (str): The type of aggregation ('count', 'mean', 'median', 'max', 'min', 'sum').

    Returns:
    pd.DataFrame: The aggregated DataFrame with the column name corresponding to the aggregation type.
    """
    
    # Dictionary to map aggregation types to Pandas functions
    aggregation_functions = {
        'count': 'count',
        'mean': 'mean',
        'median': 'median',
        'max': 'max',
        'min': 'min',
        'sum': 'sum'
    }
    
    # Validate the aggregation type
    if aggregation not in aggregation_functions:
        raise ValueError(f"Invalid aggregation type. Choose from {list(aggregation_functions.keys())}")
    
    # Perform the aggregation
    if aggregation == 'count':
        data = df.groupby(key).agg({col_name: 'count'})
    else:
        data = df.groupby(key).agg({col_name: aggregation_functions[aggregation]})
    
    # Rename the column to the type of aggregation
    data.columns = [aggregation]
    
    return data

# Example usage:
df = pd.DataFrame({
    'Category': ['A', 'B', 'A', 'A', 'B', 'C'],
    'Values': [10, 20, 30, 40, 50, 60]
})
result = rows_per_value(df, 'Category', 'Values', 'sum')
print(result)


# func_aggr_06
import pandas as pd

def aggregate_and_count(df, group_by_columns):
    """
    Aggregates the DataFrame based on the specified columns and counts the number of rows for each group.

    Parameters:
    df (pd.DataFrame): The input DataFrame.
    group_by_columns (list): A list of columns to group by.

    Returns:
    pd.DataFrame: A DataFrame with the count of rows for each group.
    """
    # Step 2: Input Validation
    if not isinstance(df, pd.DataFrame):
        raise ValueError("The first argument must be a pandas DataFrame.")
    if not isinstance(group_by_columns, list) or not all(isinstance(col, str) for col in group_by_columns):
        raise ValueError("The second argument must be a list of strings representing column names.")
    if len(group_by_columns) == 0:
        raise ValueError("The list of columns to group by must not be empty.")

    # Step 3: Perform Aggregation
    # Group by the specified columns and count the number of rows for each group
    aggregated_df = df.groupby(group_by_columns).size().reset_index(name='count')

    # Step 4: Return the Result
    return aggregated_df

# Example usage
if __name__ == "__main__":
    # Creating a sample DataFrame
    data = {
        'Category': ['A', 'B', 'A', 'A', 'B', 'C'],
        'Subcategory': ['X', 'Y', 'X', 'Z', 'Y', 'X'],
        'Value': [10, 20, 10, 30, 20, 10]
    }
    df = pd.DataFrame(data)

    # Defining the columns to group by
    group_by_columns = ['Category', 'Subcategory']

    # Calling the function
    result = aggregate_and_count(df, group_by_columns)
    
    # Display the result
    print(result)


# func_aggr_07