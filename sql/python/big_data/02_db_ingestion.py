import pandas as pd
import os
from sqlalchemy import create_engine

# --- Configuration Variables ---
begin_year = 2024
end_year = 2025
local_path = "C:\\Python repositories\\Taxi DB project\\src\\input_data\\yellow_cab_trips\\"

# --- SQL Configuration ---
# Replace 'password123' with the password you set during PostgreSQL installation
DB_URI = "postgresql://postgres:password123@localhost:5432/taxi_project"
engine = create_engine(DB_URI)

# =================================================================
# STEP 1: RAW DATA INGESTION (Load all Parquet files into SQL)
# =================================================================
print("--- Starting Raw Data Ingestion into SQL ---")

raw_cols = {
    'default': ['tpep_pickup_datetime', 'tpep_dropoff_datetime', 'passenger_count', 'trip_distance', 'total_amount'],
    'alt': ['pickup_datetime', 'dropoff_datetime', 'passenger_count', 'trip_distance', 'total_amount'],
    'alt_3': ['Trip_Pickup_DateTime', 'Trip_Dropoff_DateTime', 'Passenger_Count', 'Trip_Distance', 'Total_Amt']
}

for year in range(begin_year, end_year + 1):
    current_year = str(year)
    for month in range(1, 13):
        file_name = f"yellow_tripdata_{current_year}-{month:02d}.parquet"
        file_path = os.path.join(local_path, file_name)
        
        if not os.path.exists(file_path):
            continue
            
        print(f"Loading {file_name}...")
        
        try:
            df = pd.read_parquet(file_path, engine="pyarrow", columns=raw_cols['default'])
        except Exception:
            try:
                df = pd.read_parquet(file_path, engine="pyarrow", columns=raw_cols['alt'])
                df.columns = raw_cols['default']
            except Exception:
                df = pd.read_parquet(file_path, engine="pyarrow", columns=raw_cols['alt_3'])
                df.columns = raw_cols['default']

        # Formatting
        df['tpep_pickup_datetime'] = pd.to_datetime(df['tpep_pickup_datetime'])
        df['tpep_dropoff_datetime'] = pd.to_datetime(df['tpep_dropoff_datetime'])
        df['source_year'] = int(current_year) # Helper column to identify data year quickly
        
        # Save to Master Table
        # 'append' ensures we don't delete previous months/years
        df.to_sql('raw_yellow_taxi_trips', engine, if_exists='append', index=False)

print("\n--- All raw data has been loaded into PostgreSQL table: raw_yellow_taxi_trips ---")
