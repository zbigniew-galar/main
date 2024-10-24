# func_access_01
import hvac
import json
import base64
from google.oauth2 import service_account
from google.cloud import bigquery

vault_path = "xxx"
app_role = "xxx"
app_secret = "xxx"

csw_core_project = "xxx"
csw_core_dataset = 'xxx'
csw_core_table = "xxx"

vault_url = "https://vault.xxx"
vault_client = hvac.Client(url=vault_url)
vault_auth = vault_client.auth.approle.login(app_role, app_secret)
vault_token = vault_auth["auth"]["client_token"]
vault_secret = vault_client.read(vault_path)
vault_secret = vault_secret["data"]["data"]

if "data" in vault_secret and type(vault_secret["data"]) == str:
	service_account_creds = json.loads(base64.b64decode(vault_secret["data"]))
else:
	# In case credentials are saved directly as JSON object in vault (not encoded) you can get it directly
	service_account_cred = json.loads(base64.b64decode(vault_secret))

bq_credentials = service_account.Credentials.from_service_account_info(service_account_creds)
bq_client = bigquery.Client(credentials=bq_credentials, project=csw_core_project)

# Submit a query job
query = f"SELECT * FROM {csw_core_project}.{csw_core_dataset}.{csw_core_table} WHERE sap_sys IN ('xxx')"
query_job = bq_client.query(query)

# Wait for the query to finish
results = query_job.result()

# Convert the query results to a pandas DataFrame
df = results.to_dataframe()

# Display the DataFrame on the console
print(df.shape, df.columns)
save_path = '/Users/Local_user/Desktop/VS Code projects/Test project/data/google data/all ' + csw_core_table + '.csv'
df.to_csv(save_path, index=False)

# Check the job's status
status = query_job.state

print(f"Job status: {status}")


# func_access_02
import hvac
import json
import base64
import time
import math
from google.oauth2 import service_account
from google.cloud import bigquery

def fetch_and_save_bigquery_data(vault_path, app_role, app_secret, csw_core_project, csw_core_dataset, csw_core_table, save_path):
	"""
	Fetch data from Google BigQuery and save it as a CSV file.
	
	Parameters:
	vault_path (str): Path the Vault secret.
	app_role (str): Vault AppRole. 
	app_secret (str): Vault AppSecret. 
	csw_core_project (str): Google Cloud project ID.
	csw_core_dataset (str): BigQuery dataset name.
	csw_core_table (str): BigQuery table name.
	save_path (str): Path to save the CSV file.
	
	Returns:
	None
	"""
	start_time = time.time() # Start measuring the total execution time

	# Load secrets from Vault
	vault_url = "https://vault.xxx"
	vault_client = hvac.Client(url=vault_url)
	vault_client.auth.approle.login(app_role, app_secret)
	vault_secret = vault_client.read(vault_path)
	vault_secret = vault_secret["data"]["data"]

	if "data" in vault_secret and isinstance(vault_secret["data"], str):
		service_account_creds = json.loads(base64.b64decode(vault_secret["data"]))
	else:
		# In case credentials are saved directly as JSON object in vault (not encoded) you can get it directly
		service_account_cred = json.loads(base64.b64decode(vault_secret))
	
	bq_credentials = service_account.Credentials.from_service_account_info(service_account_creds)
	bq_client = bigquery.Client(credentials=bq_credentials, project=csw_core_project)
	
	# Submit a query job
	query = f"SELECT * FROM {csw_core_project}.{csw_core_dataset}.{csw_core_table} WHERE sap_sys IN ('xxx')"

	fetch_start_time = time.time() # Start measuring the time to fetch data
	query_job = bq_client.query(query)
	results = query_job.result() # Wait for the query to finish
	fetch_end_time = time.time() # End measuring the time to fetch data

	# Convert the query results to a pandas DataFrame
	df = results.to_dataframe()

	# Display the DataFrame shape and columns
	print(f"DataFrame's shape: {df.shape}")
	print(f"DataFrame's columns: {df.columns}")

	# Calculate the number of values
	num_rows, num_columns = df.shape
	num_values = num_rows * num_columns

	# Check the job's status
	status = query_job.state
	print(f"Job status: {status}")

	end_time = time.time() # End measuring the total execution time

	# Calculate execution times
	total_execution_time = math.ceil(end_time - start_time)
	fetch_execution_time = math.ceil(fetch_end_time - fetch_start_time)

	# Calculate the number of values extracted per second
	values_per_second = math.ceil(num_values / total_execution_time)

	# Display execution times and values per second
	print(f"Total execution time: {total_execution_time} seconds")
	print(f"Time to fetch data from BigQuery: {fetch_execution_time} seconds")
	print(f"Number of values: {num_values}")
	print(f"Number of values extracted per second: {values_per_second}")
	print(f"Saving to CSV file: {save_path}")

	# Save the DataFrame to a CSV file
	df.to_csv(save_path, index=False)
	'''
	vault_path = "take from .env file"
	app_role = "take from .env file"
	app_secret = "take from .env file"
	'''
# Example usage:
# fetch_and_save_bigquery_data(
#	vault_path = "xxx",
#	app_role = "xxx",
#	app_secret = "xxx",
#	csw_core_project = "xxx",
#	csw_core_dataset = 'xxx',
#	csw_core_table = "xxx",
#	save_path = '/Users/Local_user/Desktop/VS Code projects/Test project/data/google data/all ' + csw_core_table + '.csv'
# )


# func_access_03
import time
import pandas as pd
import math
import os
from databricks import sql # Import the correct library for Databricks SQL connection

# Define the folder and file paths
save_folder = '/Users/Local_user/Desktop/VS Code projects/Test project/data/'
sql_code_folder = '/Users/Local_user/Desktop/VS Code projects/Test project/Done code/'
file_name - 'test_data.csv'
metadata_name = 'metadata.csv'
save_path = os.path.join(save_folder, file_name)
metadata_path = os.path.join(save_folder, metadata_name)
sql_file_path = os.path.join(sql_code_folder, 'databricks_query.sql')

# Start measuring the total execution time
start_time = time.time()

# Create a connection to the SQL endpoint
connection = sql.connect(
	server_hostname = "xxx",
	http_path = "xxx",
	access_token = "xxx"
)

# Initialize the cursor
cursor = connection.cursor()

# Read the SQL query from the file
with open(sql_file_path, 'r') as file:
	query = file.read()

try:
	fetch_start_time = time.time() # Start measuring the time to fetch data

	# Execute the SQL query
	cursor.execute(query)

	# Fetch all results from the  executed query
	results = cursor.fetchall()

	fetch_end_time = time.time() # End measuring the time to fetch data

	# Convert the results to a pandas DataFrame
	column_names = [col[0] for col in cursor.description]
	df = pd.DataFrame(results, column=column_names)

	# Display the DataFrame shape and columns
	print(f"DataFrame's shape: {df.shape}")
	print(f"DataFrame's columns: {df.columns}")

	# Calculate the number of values
	num_rows, num_columns = df.shape
	num_values = num_rows * num_columns

	end_time = time.time() # End measuring the total execution time

	# Calculate execution times
	total_execution_time = math.ceil(end_time - start_time)
	fetch_execution_time = math.ceil(fetch_end_time - fetch_start_time)

	# Calculate the number of values extracted per second
	values_per_second = math.ceil(num_values / total_excecution_time)

	# Display execution times and values per second
	print(f"Total execution time: {total_execution_time} seconds")
	print(f"Time to fetch data from Databricks: {fetch_execution_time} seconds")
	print(f"Number of values: {num_values}")
	print(f"Number of values extracted per second: {values_per_second}")
	print(f"Saving to CSV file: {save_path}")
	print(f"Saving to CSV metadata file: {metadata_path}")

	# Save the DataFrame to a CSV file
	df.to_csv(save_path, sep=';', index=False)
	metadata = pd.DataFrame(df.columns, columns=['Column Name'])
	metadata.to_csv(metadata_path, sep=';', index=False)

except Exception as e:
	print(f"An error occurred: {e}")

finally
	# Ensure the cursor and connection are closed
	cursor.close()
	connection.close()

# SQL Query
"""
SELECT
	MATERIAL, 
	BASE_UOM
FROM
	xxx.xxx.xxx
WHERE
	`/BIC/DSNAPSCP` = '202423'
	AND
	EXTRACT(YEAR FROM APO_AVADAT) = 2024;
"""
# func_access_04
