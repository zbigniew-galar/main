import pandas as pd
import os
from sqlalchemy import create_engine

# --- Configuration Variables ---
# Update with your actual PostgreSQL password
DB_URI = "postgresql://postgres:password123@localhost:5432/taxi_small_project"
output_path = "C:\\Python repositories\\Text Taxi DB project\\src\\output_data\\"

# Choose the table you want to export
target_table = "analysis_01_passenger_count_week"

def export_table_to_excel(table_name: str):
    """Extracts a full table from SQL and saves it as an Excel file."""
    engine = create_engine(DB_URI)
    
    print(f"--- Extracting {table_name} from database ---")
    
    try:
        # 1. Pull the data using 'SELECT *'
        # We use pd.read_sql_query for more control over the SQL command
        query = f"SELECT * FROM {table_name}"
        df = pd.read_sql_query(query, engine)
        
        if df.empty:
            print(f"! Warning: Table {table_name} appears to be empty.")
            return

        # 2. Define the output file name and path
        output_file = os.path.join(output_path, f"EXPORT_{table_name}.xlsx")
        
        # 3. Save to Excel using your preferred engine
        print(f"--- Saving to Excel: {output_file} ---")
        try:
            writer = pd.ExcelWriter(output_file, engine="xlsxwriter")
        except ModuleNotFoundError:
            writer = pd.ExcelWriter(output_file, engine="openpyxl")
            
        df.to_excel(writer, sheet_name="SQL_Export", index=False)
        writer.close()
        
        print(f"Successfully exported {len(df)} rows.")

    except Exception as e:
        print(f"! Error during export: {e}")

if __name__ == "__main__":
    # You can change 'target_table' at the top or pass a list here
    export_table_to_excel(target_table)
