# func_conver_01
import pandas as pd
import json

# Declarations
input_f = 'data/input.xlsx'
output_f = 'data/output.json'

field_1 = 'productId'
field_2 = 'locationId'

# Functions
# Product location combinations extraction as JSON
def pr_loc_to_json(input_file, output_file):
	df = pd.read_excel(input_file)
	# Add double quotes to the values
	df[field_1] = df[fields_1].astype(str)
	df[field_2] = df[fields_2].astype(str)
	df.rename(columns={field_1:'Product', field_1:'Location'}, inplace=True)
	json_data = df[['Product', 'Location']].to_dict(orient='records')
	with open(output_file, "w") as f:
		f.write(json.dumps(json_data, indent=4))

def products_to_json(input_file, output_file):
	df = pd.read_excel(input_file)
	# Add double quotes to the values
	df[field_1] = df[fields_1].astype(str)
	df.rename(columns={field_1:'Product'}, inplace=True)
	json_data = df[['Product']].to_dict(orient='records')
	with open(output_file, "w") as f:
		f.write(json.dumps(json_data, indent=4))

# Example usage
# pr_loc_to_json(input_f, output_f)
# products_to_json(input_f, output_f)


# func_conver_02
import pandas as pd
import re
import json

"""
{
	"sheet_name": [
	{
		"location": "10",
		"product": "A10",
		"new": "W3"
		},
		{
		"location": "20",
		"product": "B10",
		"new": "W4"
		}
		]
}
"""

file_name = "file_name"

def txt_to_xlsx(input_file: str, output_file: str):
	# Read the text file content
	with open(input_file, 'r') as file:
		content = file.read()

	# Extract the first word in double quotes
	sheet_name = re.findall(r'"([^"]*)"', content)[0]

	# Load the JSON data from the content
	json_data = json.loads(content)

	# Convert the JSON data to a DataFrame
	df = pd.DataFrame(json_data[sheet_name])

	# Save the DataFrame as an xlsx file
	df.to_excel(output_file, sheet_name=sheet_name, index=False)

	print(df.shape)

# Example usage:
# txt_to_xlsx(file_name, file_name + '.xlsx')


# func_conver_03
import json
import pandas as pd

'''
sample2.json
{
	"start":"Begin",
	"end":"Finish",
	"source": [
	{
		"location": "10",
		"product": "A10", 
		"new": "W3"
		},
		{
		"location": "20",
		"product": "B10",
		"new": "W4"
		}
	],
	"coordinates":	[
	{
		"index": 1,
		"lat": -20.09,
		"long": null
		}
		]
}
'''

def json_to_excel(json_file_path, excel_file_path):
	# Converts a JSON format to Excel with multiple data sheets
    # Load JSON data from file
    with open(json_file_path) as f:
        json_data = json.load(f)

    # Create dictionary of sheets and rows
    sheets = {}
    for table_name, table_data in json_data.items():
        for row in table_data:
            if table_name not in sheets:
                sheets[table_name] = []
            sheets[table_name].append(row)

    # Write data to Excel file
    with pd.ExcelWriter(excel_file_path) as writer:
        for sheet_name, sheet_data in sheets.items():
            df = pd.DataFrame(sheet_data)
            df.to_excel(writer, sheet_name=sheet_name, index=False)

# Execution
            
file_name = 'sample2'

input_file = file_name + '.json'
output_file = file_name + '.xlsx'
        
json_to_excel(input_file, output_file)

# func_conver_04
import json
import pandas as pd

"""
sample.json
{
	"start":false,
	"end":"Finish",
	"source": [
	{
		"location": "10",
		"product": "A10",
		"new": "W3"
		},
		{
		"location": "20",
		"product": "B10",
		"new": "W4"
		}
	],
	"coordinates": [
	{
		"index": 1,
		"lat": -20.09,
		"long": null
		}
	]
}
"""

def json_to_excel(json_file_path, excel_file_path):
	# Load JSON data from file
	with open(json_file_path) as f:
		json_data = json.load(f)

	def convert_bool_to_str(obj):
		if isinstance(obj, bool):
			return str(obj)
		if isinstantce(obj, dict):
			return {k: convert_bool_to_str(v) for k, v in obj.items()}
		if isinstance(obj, list):
			return [convert_bool_to_str(item) for item in obj]
		return obj

	# Convert boolean values to strings
	json_data = convert_bool_to_str(json_data)

	# Create dictionary of sheets and rows
	sheets = {}
	for table_name, table_data in json_data.items():
		for row in table_data:
			if table_name not in sheets:
				sheets[table_name] = []
			sheets[table_name].append(row)

	# Write data to Excel file
	with pd.ExceLWriter(excel_file_path) as writer:
		for sheet_name, sheet_data in sheets.items():
			df = pd.DataFrame(sheet_data)
			df.to_excel(writer, sheet_name=sheet_name, index=False)

file_name = 'input_json'

input_file = file_name + '.json'
output_file = file_name + '.xlsx'

json_to_excel(input_file, output_file)


# func_conver_05
import pandas as pd
import re
import json

'''
sample.txt
{
	"sheet_name": [
	{
		"c1": "10",
		"c2": "A10", 
		"c3": "W3"
		},
		{
		"c1": "20",
		"c2": "B10",
		"c3": "W4"
		}
	]
}
'''

file_name = 'sample.txt'

def txt_to_xlsx(input_file: str, output_file: str):
# Take a text file in sample txt format and create an Excel 
    # Read the text file content
    with open(input_file, 'r') as file:
        content = file.read()

    # Extract the first word in double quotes
    sheet_name = re.findall(r'"([^"]*)"', content)[0]

    # Load the JSON data from the content
    json_data = json.loads(content)

    # Convert the JSON data to a DataFrame
    df = pd.DataFrame(json_data[sheet_name])

    # Save the DataFrame as an xlsx file
    df.to_excel(output_file, sheet_name=sheet_name, index=False)

# Sample usage
txt_to_xlsx(file_name, file_name+'.xlsx')


# func_conver_06