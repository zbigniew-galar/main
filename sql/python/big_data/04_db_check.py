import pandas as pd
import os
from sqlalchemy import create_engine, text

# --- Configuration Variables ---
# Update 'your_password' with your actual PostgreSQL password
DB_URI = "postgresql://postgres:password123@localhost:5432/taxi_small_project"
output_path = "C:\\Python repositories\\Text Taxi DB project\\src\\output_data\\"

def export_monthly_row_counts():
    """
    Queries the raw_yellow_taxi_trips table to count records per month
    and saves the inventory as an Excel file.
    """
    engine = create_engine(DB_URI)
    
    # SQL logic: 
    # 1. to_char formats the date into '2024-01' strings
    # 2. COUNT(*) counts every row in that group
    query = """
    SELECT 
        to_char(tpep_pickup_datetime, 'YYYY-MM') AS "Year-Month",
        COUNT(*) AS "Total_Rows",
        source_year AS "Ingestion_Year"
    FROM raw_yellow_taxi_trips
    GROUP BY "Year-Month", source_year
    ORDER BY "Year-Month" ASC;
    """
    
    print("--- Querying database for monthly row counts ---")
    
    try:
        # Load result into DataFrame
        df = pd.read_sql_query(query, engine)
        
        if df.empty:
            print("! The raw_yellow_taxi_trips table appears to be empty.")
            return

        # Prepare output file
        output_file = os.path.join(output_path, "taxi_data_inventory_monthly.xlsx")
        
        print(f"--- Saving inventory to: {output_file} ---")
        
        # Save to Excel
        try:
            writer = pd.ExcelWriter(output_file, engine="xlsxwriter")
        except ModuleNotFoundError:
            writer = pd.ExcelWriter(output_file, engine="openpyxl")
            
        df.to_excel(writer, sheet_name="Data_Inventory", index=False)
        writer.close()
        
        print(f"Successfully exported inventory for {len(df)} months.")

    except Exception as e:
        print(f"! Error during database query or export: {e}")

if __name__ == "__main__":
    export_monthly_row_counts()
