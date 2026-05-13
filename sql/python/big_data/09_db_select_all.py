import pandas as pd
import os
from sqlalchemy import create_engine

DB_URI = "postgresql://postgres:password123@localhost:5432/taxi_small_project"
output_path = "C:\\Python repositories\\Text Taxi DB project\\src\\output_data\\"

tables_to_export = [
    "analysis_01_passenger_count_week",
    "analysis_02_passenger_count_week_hour",
    "analysis_03_total_amount_week",
    "analysis_04_total_amount_week_hour",
    "analysis_05_trip_distance_week",
    "analysis_06_trip_distance_week_hour",
    "analysis_07_time_week",
    "analysis_08_time_week_hour",
    "analysis_09_speed_week",
    "analysis_10_speed_week_hour"
]

def export_tables_to_excel(tables):
    os.makedirs(output_path, exist_ok=True)
    engine = create_engine(DB_URI)
    
    for table in tables:
        try:
            df = pd.read_sql_table(table, con=engine)
            
            if df.empty:
                print(f"! Skipped {table}: Table is empty.")
                continue

            output_file = os.path.join(output_path, f"EXPORT_{table}.xlsx")
            df.to_excel(output_file, sheet_name="SQL_Export", index=False, engine="openpyxl")
            print(f"Exported {table}: {len(df)} rows to {output_file}")

        except Exception as e:
            print(f"! Error extracting {table}: {e}")

if __name__ == "__main__":
    export_tables_to_excel(tables_to_export)
