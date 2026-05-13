## Taxi big data project with PostgreSQL Database
#### Data source
https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page
#### Database server
https://www.enterprisedb.com/downloads/postgres-postgresql-downloads
### VS Code installation
#### Python library installation
We use `psycopg2-binary` for local development because it's easier to install on Windows than the standard version.
``` powershell
# For Python to "speak" to PostgreSQL, it needs a translator (a driver)
>>> pip install psycopg2-binary sqlalchemy
# Reading parquet files
>>> pip install pyarrow
```
#### First we will create  the `db_setup.py` script
``` python
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

# --- Configuration ---
DB_NAME = "taxi_project"
USER = "postgres"
PASSWORD = "password123"  # Update this
HOST = "localhost"
PORT = "5432"

def initialize_database():
    # 1. Connect to default 'postgres' db to create the new database
    conn = psycopg2.connect(dbname='postgres', user=USER, password=PASSWORD, host=HOST, port=PORT)
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cur = conn.cursor()
    
    # Create Database
    cur.execute(f"SELECT 1 FROM pg_catalog.pg_database WHERE datname = '{DB_NAME}'")
    exists = cur.fetchone()
    if not exists:
        cur.execute(f"CREATE DATABASE {DB_NAME}")
        print(f"Database '{DB_NAME}' created.")
    else:
        print(f"Database '{DB_NAME}' already exists.")
    
    cur.close()
    conn.close()

    # 2. Connect to the new database to create the table
    conn = psycopg2.connect(dbname=DB_NAME, user=USER, password=PASSWORD, host=HOST, port=PORT)
    cur = conn.cursor()

    # Create Master Table for Input Data
    # Note: We use a single table for all years for better SQL performance
    create_table_query = """
    CREATE TABLE IF NOT EXISTS yellow_taxi_trips (
        id SERIAL PRIMARY KEY,
        tpep_pickup_datetime TIMESTAMP,
        tpep_dropoff_datetime TIMESTAMP,
        passenger_count FLOAT,
        trip_distance FLOAT,
        total_amount FLOAT,
        confidence FLOAT,
        source_year INT
    );
    """
    cur.execute(create_table_query)
    
    # Create Table for Weekly Metrics (Analysis Output)
    create_metrics_query = """
    CREATE TABLE IF NOT EXISTS weekly_taxi_metrics (
        year_week TEXT,
        metric_name TEXT,
        avg_value FLOAT,
        sum_value FLOAT,
        median_value FLOAT,
        confidence FLOAT,
        trip_count INT,
        hour INT,
        year INT
    );
    """
    cur.execute(create_metrics_query)
    
    conn.commit()
    cur.close()
    conn.close()
    print("SQL tables initialized successfully.")

if __name__ == "__main__":
    initialize_database()
```
#### Second we will load all parquet data into the Database with `db_ingestion.py`
``` python
import pandas as pd
import os
from sqlalchemy import create_engine

# --- Configuration Variables ---
begin_year = 2023
end_year = 2024
local_path = "C:\\Python repositories\\Database project\\src\\input_data\\yellow_cab_trips\\"

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
```
#### If we want to start again with more or less input data we need to drop existing tables in database with `db_reset.py`
``` python
from sqlalchemy import create_engine, text

# --- Configuration ---
DB_URI = "postgresql://postgres:password123@localhost:5432/taxi_project"
engine = create_engine(DB_URI)

def wipe_data():
    """Drops all tables to ensure a clean start for the new run."""
    tables = [
        "raw_yellow_taxi_trips",
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
    
    print("--- Warning: This will delete all existing data in the taxi_project database ---")
    confirm = input("Type 'YES' to confirm: ")
    
    if confirm == "YES":
        with engine.connect() as conn:
            for table in tables:
                conn.execute(text(f"DROP TABLE IF EXISTS {table} CASCADE;"))
                print(f" Dropped: {table}")
            conn.commit()
        print("\n--- Database is now empty ---")
    else:
        print("Operation cancelled.")

if __name__ == "__main__":
    wipe_data()
```
#### Database installation
- Go to the [PostgreSQL Downloads page](https://www.postgresql.org/download/windows/) and download the **Interactive Installer by EDB**.
- Run the `.exe` and follow the wizard.
- **Crucial Step:** During installation, it will ask you to set a password for the **`postgres`** superuser. **Write this down.** This is the `PASSWORD` variable in the code.
- **Port:** Keep the default port **5432**.
- **Components:** Ensure **pgAdmin 4** is checked. This is the visual "browser" for your database.
##### Installation parameters example
``` powershell
Installation Directory: C:\Program Files\PostgreSQL\18
Server Installation Directory: C:\Program Files\PostgreSQL\18
Data Directory: C:\Program Files\PostgreSQL\18\data
Database Port: 5432
Database Superuser: postgres
Operating System Account: NT AUTHORITY\NetworkService
Database Service: postgresql-x64-18
Command Line Tools Installation Directory: C:\Program Files\PostgreSQL\18
pgAdmin4 Installation Directory: C:\Program Files\PostgreSQL\18\pgAdmin 4
Stack Builder Installation Directory: C:\Program Files\PostgreSQL\18
Installation Log: C:\Users\HP\AppData\Local\Temp\install-postgresql.log
```
##### Once installed, PostgreSQL starts automatically every time you turn on your computer
- Open **pgAdmin 4** from your Start Menu.
- It will ask for a "Master Password" (set one for the app).
- On the left sidebar, click **Servers** > **PostgreSQL (Version)**.
- Enter the `postgres` password you created during installation. If you can see a list of "Databases," the server is active.
In the `main_taxi_analysis.py` script, you’ll see a `DB_URI`. This is the "address" of your database. It follows this specific format:
`postgresql://[USER]:[PASSWORD]@[HOST]:[PORT]/[DATABASE_NAME]`
- **User:** `postgres` (default)
- **Password:** What you chose during install.
- **Host:** `localhost` (means "this computer").
- **Port:** `5432` (default).
- **Database:** `taxi_project` (this is what the `db_setup.py` script creates for you).
#### Running the code

| **Order** | **File to Run**     | **Action Required**                     | **Expected Result**                               |
| --------- | ------------------- | --------------------------------------- | ------------------------------------------------- |
| **1**     | `db_setup.py`       | Run once.                               | Creates `taxi_project` database and empty tables. |
| **2**     | `db_ingestion.py`   | Set `begin_year=2023`, `end_year=2024`. | Raw data for 2 years is loaded into SQL.          |
**If we want to start again we run `db_reset.py`.**

#### Checking how many rows per month are in the main table
Output as Excel file via `db_check.py`:
``` python
import pandas as pd
import os
from sqlalchemy import create_engine, text

# --- Configuration Variables ---
# Update 'your_password' with your actual PostgreSQL password
DB_URI = "postgresql://postgres:password123@localhost:5432/taxi_project"
output_path = "C:\\Python repositories\\Database project\\src\\output_data\\"

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
```
#### Index the tables of existing database for much better response time for queries with `db_indexing_main.py`
``` python
from sqlalchemy import create_engine, text
import time

# --- Configuration ---
# Replace 'your_password' with your actual PostgreSQL password
DB_URI = "postgresql://postgres:password123@localhost:5432/taxi_project"
engine = create_engine(DB_URI)

def create_all_indexes():
    """
    Creates indexes for the raw data table.
    Run this ONLY after the data ingestion is complete for maximum speed.
    """
    
    # We use double quotes for "Year-Week" because PostgreSQL interprets 
    # the hyphen as a subtraction operator otherwise.
    commands = [
        # --- Raw Data Table Indexes ---
        "CREATE INDEX IF NOT EXISTS idx_raw_pickup ON raw_yellow_taxi_trips (tpep_pickup_datetime);",
        "CREATE INDEX IF NOT EXISTS idx_raw_source_year ON raw_yellow_taxi_trips (source_year);"
    ]

    print(f"--- Starting Indexing Process at {time.strftime('%H:%M:%S')} ---")
    
    with engine.connect() as conn:
        for i, cmd in enumerate(commands, 1):
            try:
                start_time = time.time()
                print(f"[{i}/{len(commands)}] Executing: {cmd.split(' ON ')[0]}...")
                
                # Execute and commit
                conn.execute(text(cmd))
                conn.commit()
                
                duration = time.time() - start_time
                print(f"    Done in {duration:.2f} seconds.")
                
            except Exception as e:
                print(f"    ! Error creating index: {e}")
                conn.rollback()

    print(f"--- Maintenance Completed at {time.strftime('%H:%M:%S')} ---")

if __name__ == "__main__":
    create_all_indexes()
```
### Expanding the Database by creating new tables
#### Adding new analytical tables with SQL with `db_analysis_metrics_sql.py`
``` python
from sqlalchemy import create_engine, text
import time

# --- Configuration ---
# Update 'your_password' with your PostgreSQL password
DB_URI = "postgresql://postgres:password123@localhost:5432/taxi_project"
engine = create_engine(DB_URI)

def run_sql_query(query_name, sql):
    """Helper function to execute SQL and time the performance."""
    print(f"--- Starting {query_name} ---")
    start_time = time.time()
    with engine.connect() as conn:
        # Drop table if exists to ensure we are not appending to old test data
        table_name = f"analysis_{query_name}"
        conn.execute(text(f"DROP TABLE IF EXISTS {table_name};"))
        
        # Execute the 'CREATE TABLE AS SELECT...' statement
        conn.execute(text(f"CREATE TABLE {table_name} AS {sql}"))
        conn.commit()
    
    duration = time.time() - start_time
    print(f"    Completed in {duration:.2f} seconds.\n")

# =================================================================
# STEP 2: WEEKLY METRICS ANALYSIS (SQL VERSION)
# =================================================================

# --- 01 Passenger Count Week ---
sql_01 = """
SELECT 
    to_char(tpep_pickup_datetime, 'IYYY-IW') AS "Year-Week",
    AVG(passenger_count) AS avg_passenger_count,
    SUM(passenger_count) AS sum_passenger_count,
    percentile_cont(0.5) WITHIN GROUP (ORDER BY passenger_count) AS median_passenger_count,
    COUNT(*) AS trip_count,
    source_year AS "Year"
FROM raw_yellow_taxi_trips
WHERE passenger_count >= 1 AND passenger_count <= 5
GROUP BY "Year-Week", source_year
ORDER BY "Year-Week";
"""

# --- 02 Passenger Count Week Hour ---
sql_02 = """
SELECT 
    to_char(tpep_pickup_datetime, 'IYYY-IW') AS "Year-Week",
    EXTRACT(HOUR FROM tpep_pickup_datetime) AS "Hour",
    AVG(passenger_count) AS avg_passenger_count,
    SUM(passenger_count) AS sum_passenger_count,
    percentile_cont(0.5) WITHIN GROUP (ORDER BY passenger_count) AS median_passenger_count,
    COUNT(*) AS trip_count,
    source_year AS "Year"
FROM raw_yellow_taxi_trips
WHERE passenger_count >= 1 AND passenger_count <= 5
GROUP BY "Year-Week", "Hour", source_year
ORDER BY "Year-Week", "Hour";
"""

# --- 03 Total Amount Week ---
sql_03 = """
SELECT 
    to_char(tpep_pickup_datetime, 'IYYY-IW') AS "Year-Week",
    AVG(total_amount) AS avg_total_amount,
    SUM(total_amount) AS sum_total_amount,
    percentile_cont(0.5) WITHIN GROUP (ORDER BY total_amount) AS median_total_amount,
    COUNT(*) AS trip_count,
    source_year AS "Year"
FROM raw_yellow_taxi_trips
WHERE total_amount >= 0.01 AND total_amount <= 1000
GROUP BY "Year-Week", source_year
ORDER BY "Year-Week";
"""

# --- 04 Total Amount Week Hour ---
sql_04 = """
SELECT 
    to_char(tpep_pickup_datetime, 'IYYY-IW') AS "Year-Week",
    EXTRACT(HOUR FROM tpep_pickup_datetime) AS "Hour",
    AVG(total_amount) AS avg_total_amount,
    SUM(total_amount) AS sum_total_amount,
    percentile_cont(0.5) WITHIN GROUP (ORDER BY total_amount) AS median_total_amount,
    COUNT(*) AS trip_count,
    source_year AS "Year"
FROM raw_yellow_taxi_trips
WHERE total_amount >= 0.01 AND total_amount <= 1000
GROUP BY "Year-Week", "Hour", source_year
ORDER BY "Year-Week", "Hour";
"""

# --- 05 Trip Distance Week ---
sql_05 = """
SELECT 
    to_char(tpep_pickup_datetime, 'IYYY-IW') AS "Year-Week",
    AVG(trip_distance * 1.60934) AS avg_trip_distance_km,
    SUM(trip_distance * 1.60934) AS sum_trip_distance_km,
    percentile_cont(0.5) WITHIN GROUP (ORDER BY trip_distance * 1.60934) AS median_trip_distance_km,
    COUNT(*) AS trip_count,
    source_year AS "Year"
FROM raw_yellow_taxi_trips
WHERE trip_distance >= 0.2 AND trip_distance <= 550
GROUP BY "Year-Week", source_year
ORDER BY "Year-Week";
"""

# --- 06 Trip Distance Week Hour ---
sql_06 = """
SELECT 
    to_char(tpep_pickup_datetime, 'IYYY-IW') AS "Year-Week",
    EXTRACT(HOUR FROM tpep_pickup_datetime) AS "Hour",
    AVG(trip_distance * 1.60934) AS avg_trip_distance_km,
    SUM(trip_distance * 1.60934) AS sum_trip_distance_km,
    percentile_cont(0.5) WITHIN GROUP (ORDER BY trip_distance * 1.60934) AS median_trip_distance_km,
    COUNT(*) AS trip_count,
    source_year AS "Year"
FROM raw_yellow_taxi_trips
WHERE trip_distance >= 0.2 AND trip_distance <= 550
GROUP BY "Year-Week", "Hour", source_year
ORDER BY "Year-Week", "Hour";
"""

# --- 07 Trip Time Week ---
sql_07 = """
SELECT 
    to_char(tpep_pickup_datetime, 'IYYY-IW') AS "Year-Week",
    AVG(EXTRACT(EPOCH FROM (tpep_dropoff_datetime - tpep_pickup_datetime))/60) AS avg_time_min,
    SUM(EXTRACT(EPOCH FROM (tpep_dropoff_datetime - tpep_pickup_datetime))/60) AS sum_time_min,
    percentile_cont(0.5) WITHIN GROUP (ORDER BY EXTRACT(EPOCH FROM (tpep_dropoff_datetime - tpep_pickup_datetime))/60) AS median_time_min,
    COUNT(*) AS trip_count,
    source_year AS "Year"
FROM raw_yellow_taxi_trips
WHERE (EXTRACT(EPOCH FROM (tpep_dropoff_datetime - tpep_pickup_datetime))/60) >= 1 
  AND (EXTRACT(EPOCH FROM (tpep_dropoff_datetime - tpep_pickup_datetime))/60) <= 720
GROUP BY "Year-Week", source_year
ORDER BY "Year-Week";
"""

# --- 08 Trip Time Week Hour ---
sql_08 = """
SELECT 
    to_char(tpep_pickup_datetime, 'IYYY-IW') AS "Year-Week",
    EXTRACT(HOUR FROM tpep_pickup_datetime) AS "Hour",
    AVG(EXTRACT(EPOCH FROM (tpep_dropoff_datetime - tpep_pickup_datetime))/60) AS avg_time_min,
    SUM(EXTRACT(EPOCH FROM (tpep_dropoff_datetime - tpep_pickup_datetime))/60) AS sum_time_min,
    percentile_cont(0.5) WITHIN GROUP (ORDER BY EXTRACT(EPOCH FROM (tpep_dropoff_datetime - tpep_pickup_datetime))/60) AS median_time_min,
    COUNT(*) AS trip_count,
    source_year AS "Year"
FROM raw_yellow_taxi_trips
WHERE (EXTRACT(EPOCH FROM (tpep_dropoff_datetime - tpep_pickup_datetime))/60) >= 1 
  AND (EXTRACT(EPOCH FROM (tpep_dropoff_datetime - tpep_pickup_datetime))/60) <= 720
GROUP BY "Year-Week", "Hour", source_year
ORDER BY "Year-Week", "Hour";
"""

# --- 09 Trip Speed Week ---
sql_09 = """
SELECT 
    to_char(tpep_pickup_datetime, 'IYYY-IW') AS "Year-Week",
    AVG((trip_distance * 1.60934) / (EXTRACT(EPOCH FROM (tpep_dropoff_datetime - tpep_pickup_datetime))/3600)) AS avg_speed_kmh,
    SUM((trip_distance * 1.60934) / (EXTRACT(EPOCH FROM (tpep_dropoff_datetime - tpep_pickup_datetime))/3600)) AS sum_speed_kmh,
    percentile_cont(0.5) WITHIN GROUP (ORDER BY (trip_distance * 1.60934) / (NULLIF(EXTRACT(EPOCH FROM (tpep_dropoff_datetime - tpep_pickup_datetime)), 0)/3600)) AS median_speed_kmh,
    COUNT(*) AS trip_count,
    source_year AS "Year"
FROM raw_yellow_taxi_trips
WHERE trip_distance >= 0.2 AND trip_distance <= 550
  AND EXTRACT(EPOCH FROM (tpep_dropoff_datetime - tpep_pickup_datetime)) > 60
GROUP BY "Year-Week", source_year
ORDER BY "Year-Week";
"""

# --- 10 Trip Speed Week Hour ---
sql_10 = """
SELECT 
    to_char(tpep_pickup_datetime, 'IYYY-IW') AS "Year-Week",
    EXTRACT(HOUR FROM tpep_pickup_datetime) AS "Hour",
    AVG((trip_distance * 1.60934) / (EXTRACT(EPOCH FROM (tpep_dropoff_datetime - tpep_pickup_datetime))/3600)) AS avg_speed_kmh,
    SUM((trip_distance * 1.60934) / (EXTRACT(EPOCH FROM (tpep_dropoff_datetime - tpep_pickup_datetime))/3600)) AS sum_speed_kmh,
    percentile_cont(0.5) WITHIN GROUP (ORDER BY (trip_distance * 1.60934) / (NULLIF(EXTRACT(EPOCH FROM (tpep_dropoff_datetime - tpep_pickup_datetime)), 0)/3600)) AS median_speed_kmh,
    COUNT(*) AS trip_count,
    source_year AS "Year"
FROM raw_yellow_taxi_trips
WHERE trip_distance >= 0.2 AND trip_distance <= 550
  AND EXTRACT(EPOCH FROM (tpep_dropoff_datetime - tpep_pickup_datetime)) > 60
GROUP BY "Year-Week", "Hour", source_year
ORDER BY "Year-Week", "Hour";
"""

if __name__ == "__main__":
    # Execute all analyses
    run_sql_query("01_passenger_count_week", sql_01)
    run_sql_query("02_passenger_count_week_hour", sql_02)
    run_sql_query("03_total_amount_week", sql_03)
    run_sql_query("04_total_amount_week_hour", sql_04)
    run_sql_query("05_trip_distance_week", sql_05)
    run_sql_query("06_trip_distance_week_hour", sql_06)
    run_sql_query("07_time_week", sql_07)
    run_sql_query("08_time_week_hour", sql_08)
    run_sql_query("09_speed_week", sql_09)
    run_sql_query("10_speed_week_hour", sql_10)
    
    print("--- All 10 SQL Analysis tables have been created successfully ---")
```
#### Alternative Python only version when reading parquet files
Adding new tables when rereading source parquet files - this one is slower but it doesn't use SQL queries. This an answer to question how will I add analysis as new tables that can't be calculated with SQL only and I must use Python.
**If we want to use this version we run `db_reset.py` and `db_ingestion.py` first.**
We load particular columns from parquet files, clean the data, and calculate weekly sums, medians, and averages for all metrics with `db_analysis_metrics.py`:
``` python
import pandas as pd
import os
from sqlalchemy import create_engine

# --- Configuration Variables ---
begin_year = 2023
end_year = 2024
local_path = "C:\\Python repositories\\Database project\\src\\input_data\\yellow_cab_trips\\"

# --- SQL Configuration ---
DB_URI = "postgresql://postgres:password123@localhost:5432/taxi_project"
engine = create_engine(DB_URI)

# =================================================================
# STEP 2: WEEKLY METRICS ANALYSIS
# =================================================================

# --- Analysis 1 "passenger_count_week" ---
cols_default = ['tpep_pickup_datetime', 'passenger_count']
cols_alt = ['pickup_datetime', 'passenger_count']
cols_alt_3 = ['Trip_Pickup_DateTime', 'Passenger_Count']

for year in range(begin_year, end_year + 1):
    current_year = str(year)
    print(f"--- Processing Analysis 1 for {current_year} ---")
    data_files = []
    
    for month in range(1, 13):
        file_path = os.path.join(local_path, f"yellow_tripdata_{current_year}-{month:02d}.parquet")
        if not os.path.exists(file_path): continue
        try:
            df = pd.read_parquet(file_path, engine="pyarrow", columns=cols_default)
        except Exception:
            try:
                df = pd.read_parquet(file_path, engine="pyarrow", columns=cols_alt)
                df.columns = cols_default
            except Exception:
                df = pd.read_parquet(file_path, engine="pyarrow", columns=cols_alt_3)
                df.columns = cols_default

        df['tpep_pickup_datetime'] = pd.to_datetime(df['tpep_pickup_datetime'])
        df['passenger_count'] = df['passenger_count'].fillna(0)
        rows_before = df.shape[0]
        df.drop(df[(df['tpep_pickup_datetime'].dt.year != int(current_year)) | (df['tpep_pickup_datetime'].dt.month != month)].index, inplace=True)
        df.drop(df[(df['passenger_count'] < 1) | (df['passenger_count'] > 5)].index, inplace=True)
        df['confidence'] = df.shape[0] / rows_before if rows_before > 0 else 0
        data_files.append(df)

    if not data_files: continue
    trips = pd.concat(data_files, ignore_index=True)
    trips['Year-Week'] = trips['tpep_pickup_datetime'].dt.strftime('%Y-%V')
    trips_agg = trips.groupby(['Year-Week'], as_index=False).agg(
        avg_passenger_count=pd.NamedAgg(column='passenger_count', aggfunc='mean'),
        sum_passenger_count=pd.NamedAgg(column='passenger_count', aggfunc='sum'),
        median_passenger_count=pd.NamedAgg(column='passenger_count', aggfunc='median'),
        confidence=pd.NamedAgg(column='confidence', aggfunc='mean'),
        trip_count=pd.NamedAgg(column='passenger_count', aggfunc='count')
    )
    trips_agg.to_sql('analysis_01_passenger_count_week', engine, if_exists='append', index=False)

# --- Analysis 2 "passenger_count_week_hour" ---
for year in range(begin_year, end_year + 1):
    current_year = str(year)
    print(f"--- Processing Analysis 2 for {current_year} ---")
    data_files = []
    for month in range(1, 13):
        file_path = os.path.join(local_path, f"yellow_tripdata_{current_year}-{month:02d}.parquet")
        if not os.path.exists(file_path): continue
        df = pd.read_parquet(file_path, engine="pyarrow", columns=cols_default)
        df['tpep_pickup_datetime'] = pd.to_datetime(df['tpep_pickup_datetime'])
        df['passenger_count'] = df['passenger_count'].fillna(0)
        rows_before = df.shape[0]
        df.drop(df[(df['passenger_count'] < 1) | (df['passenger_count'] > 5)].index, inplace=True)
        df['confidence'] = df.shape[0] / rows_before if rows_before > 0 else 0
        data_files.append(df)

    if not data_files: continue
    trips = pd.concat(data_files, ignore_index=True)
    trips['Hour'] = trips['tpep_pickup_datetime'].dt.hour
    trips['Year-Week'] = trips['tpep_pickup_datetime'].dt.strftime('%Y-%V')
    trips_agg = trips.groupby(['Year-Week', 'Hour'], as_index=False).agg(
        avg_passenger_count=pd.NamedAgg(column='passenger_count', aggfunc='mean'),
        sum_passenger_count=pd.NamedAgg(column='passenger_count', aggfunc='sum'),
        median_passenger_count=pd.NamedAgg(column='passenger_count', aggfunc='median'),
        confidence=pd.NamedAgg(column='confidence', aggfunc='mean'),
        trip_count=pd.NamedAgg(column='passenger_count', aggfunc='count')
    )
    trips_agg.to_sql('analysis_02_passenger_count_week_hour', engine, if_exists='append', index=False)

# --- Analysis 3 "total_amount_week" ---
cols_default = ['tpep_pickup_datetime', 'total_amount']
for year in range(begin_year, end_year + 1):
    current_year = str(year)
    print(f"--- Processing Analysis 3 for {current_year} ---")
    data_files = []
    for month in range(1, 13):
        file_path = os.path.join(local_path, f"yellow_tripdata_{current_year}-{month:02d}.parquet")
        if not os.path.exists(file_path): continue
        df = pd.read_parquet(file_path, engine="pyarrow", columns=cols_default)
        df['tpep_pickup_datetime'] = pd.to_datetime(df['tpep_pickup_datetime'])
        df['total_amount'] = df['total_amount'].fillna(0)
        rows_before = df.shape[0]
        df.drop(df[(df['total_amount'] < 0.01) | (df['total_amount'] > 1000)].index, inplace=True)
        df['confidence'] = df.shape[0] / rows_before if rows_before > 0 else 0
        data_files.append(df)

    if not data_files: continue
    trips = pd.concat(data_files, ignore_index=True)
    trips['Year-Week'] = trips['tpep_pickup_datetime'].dt.strftime('%Y-%V')
    trips_agg = trips.groupby(['Year-Week'], as_index=False).agg(
        avg_total_amount=pd.NamedAgg(column='total_amount', aggfunc='mean'),
        sum_total_amount=pd.NamedAgg(column='total_amount', aggfunc='sum'),
        median_total_amount=pd.NamedAgg(column='total_amount', aggfunc='median'),
        confidence=pd.NamedAgg(column='confidence', aggfunc='mean'),
        trip_count=pd.NamedAgg(column='total_amount', aggfunc='count')
    )
    trips_agg.to_sql('analysis_03_total_amount_week', engine, if_exists='append', index=False)

# --- Analysis 4 "total_amount_week_hour" ---
for year in range(begin_year, end_year + 1):
    current_year = str(year)
    print(f"--- Processing Analysis 4 for {current_year} ---")
    data_files = []
    for month in range(1, 13):
        file_path = os.path.join(local_path, f"yellow_tripdata_{current_year}-{month:02d}.parquet")
        if not os.path.exists(file_path): continue
        df = pd.read_parquet(file_path, engine="pyarrow", columns=cols_default)
        df['tpep_pickup_datetime'] = pd.to_datetime(df['tpep_pickup_datetime'])
        df['total_amount'] = df['total_amount'].fillna(0)
        rows_before = df.shape[0]
        df.drop(df[(df['total_amount'] < 0.01) | (df['total_amount'] > 1000)].index, inplace=True)
        df['confidence'] = df.shape[0] / rows_before if rows_before > 0 else 0
        data_files.append(df)

    if not data_files: continue
    trips = pd.concat(data_files, ignore_index=True)
    trips['Hour'] = trips['tpep_pickup_datetime'].dt.hour
    trips['Year-Week'] = trips['tpep_pickup_datetime'].dt.strftime('%Y-%V')
    trips_agg = trips.groupby(['Year-Week', 'Hour'], as_index=False).agg(
        avg_total_amount=pd.NamedAgg(column='total_amount', aggfunc='mean'),
        sum_total_amount=pd.NamedAgg(column='total_amount', aggfunc='sum'),
        median_total_amount=pd.NamedAgg(column='total_amount', aggfunc='median'),
        confidence=pd.NamedAgg(column='confidence', aggfunc='mean'),
        trip_count=pd.NamedAgg(column='total_amount', aggfunc='count')
    )
    trips_agg.to_sql('analysis_04_total_amount_week_hour', engine, if_exists='append', index=False)

# --- Analysis 5 "trip_distance_week" ---
cols_default = ['tpep_pickup_datetime', 'trip_distance']
for year in range(begin_year, end_year + 1):
    current_year = str(year)
    print(f"--- Processing Analysis 5 for {current_year} ---")
    data_files = []
    for month in range(1, 13):
        file_path = os.path.join(local_path, f"yellow_tripdata_{current_year}-{month:02d}.parquet")
        if not os.path.exists(file_path): continue
        df = pd.read_parquet(file_path, engine="pyarrow", columns=cols_default)
        df['tpep_pickup_datetime'] = pd.to_datetime(df['tpep_pickup_datetime'])
        df['trip_distance'] = df['trip_distance'].fillna(0)
        rows_before = df.shape[0]
        df.drop(df[(df['trip_distance'] < 0.2) | (df['trip_distance'] > 550)].index, inplace=True)
        df['confidence'] = df.shape[0] / rows_before if rows_before > 0 else 0
        data_files.append(df)

    if not data_files: continue
    trips = pd.concat(data_files, ignore_index=True)
    trips['Year-Week'] = trips['tpep_pickup_datetime'].dt.strftime('%Y-%V')
    trips_agg = trips.groupby(['Year-Week'], as_index=False).agg(
        avg_trip_distance=pd.NamedAgg(column='trip_distance', aggfunc='mean'),
        sum_trip_distance=pd.NamedAgg(column='trip_distance', aggfunc='sum'),
        median_trip_distance=pd.NamedAgg(column='trip_distance', aggfunc='median'),
        confidence=pd.NamedAgg(column='confidence', aggfunc='mean'),
        trip_count=pd.NamedAgg(column='trip_distance', aggfunc='count')
    )
    for col in ['avg_trip_distance', 'sum_trip_distance', 'median_trip_distance']:
        trips_agg[col] = trips_agg[col] * 1.60934
    trips_agg.to_sql('analysis_05_trip_distance_week', engine, if_exists='append', index=False)

# --- Analysis 6 "trip_distance_week_hour" ---
for year in range(begin_year, end_year + 1):
    current_year = str(year)
    print(f"--- Processing Analysis 6 for {current_year} ---")
    data_files = []
    for month in range(1, 13):
        file_path = os.path.join(local_path, f"yellow_tripdata_{current_year}-{month:02d}.parquet")
        if not os.path.exists(file_path): continue
        df = pd.read_parquet(file_path, engine="pyarrow", columns=cols_default)
        df['tpep_pickup_datetime'] = pd.to_datetime(df['tpep_pickup_datetime'])
        df['trip_distance'] = df['trip_distance'].fillna(0)
        rows_before = df.shape[0]
        df.drop(df[(df['trip_distance'] < 0.2) | (df['trip_distance'] > 550)].index, inplace=True)
        df['confidence'] = df.shape[0] / rows_before if rows_before > 0 else 0
        data_files.append(df)

    if not data_files: continue
    trips = pd.concat(data_files, ignore_index=True)
    trips['Hour'] = trips['tpep_pickup_datetime'].dt.hour
    trips['Year-Week'] = trips['tpep_pickup_datetime'].dt.strftime('%Y-%V')
    trips_agg = trips.groupby(['Year-Week', 'Hour'], as_index=False).agg(
        avg_trip_distance=pd.NamedAgg(column='trip_distance', aggfunc='mean'),
        sum_trip_distance=pd.NamedAgg(column='trip_distance', aggfunc='sum'),
        median_trip_distance=pd.NamedAgg(column='trip_distance', aggfunc='median'),
        confidence=pd.NamedAgg(column='confidence', aggfunc='mean'),
        trip_count=pd.NamedAgg(column='trip_distance', aggfunc='count')
    )
    for col in ['avg_trip_distance', 'sum_trip_distance', 'median_trip_distance']:
        trips_agg[col] = trips_agg[col] * 1.60934
    trips_agg.to_sql('analysis_06_trip_distance_week_hour', engine, if_exists='append', index=False)

# --- Analysis 7 "time_minutes_week" ---
cols_default = ['tpep_pickup_datetime', 'tpep_dropoff_datetime']
for year in range(begin_year, end_year + 1):
    current_year = str(year)
    print(f"--- Processing Analysis 7 for {current_year} ---")
    data_files = []
    for month in range(1, 13):
        file_path = os.path.join(local_path, f"yellow_tripdata_{current_year}-{month:02d}.parquet")
        if not os.path.exists(file_path): continue
        df = pd.read_parquet(file_path, engine="pyarrow", columns=cols_default)
        df['tpep_pickup_datetime'] = pd.to_datetime(df['tpep_pickup_datetime'])
        df['tpep_dropoff_datetime'] = pd.to_datetime(df['tpep_dropoff_datetime'])
        df['time'] = ((df['tpep_dropoff_datetime'] - df['tpep_pickup_datetime']).dt.total_seconds() / 60).astype(int)
        rows_before = df.shape[0]
        df.drop(df[(df['time'] < 1) | (df['time'] > 720)].index, inplace=True)
        df['confidence'] = df.shape[0] / rows_before if rows_before > 0 else 0
        data_files.append(df)

    if not data_files: continue
    trips = pd.concat(data_files, ignore_index=True)
    trips['Year-Week'] = trips['tpep_pickup_datetime'].dt.strftime('%Y-%V')
    trips_agg = trips.groupby(['Year-Week'], as_index=False).agg(
        avg_time=pd.NamedAgg(column='time', aggfunc='mean'),
        sum_time=pd.NamedAgg(column='time', aggfunc='sum'),
        median_time=pd.NamedAgg(column='time', aggfunc='median'),
        confidence=pd.NamedAgg(column='confidence', aggfunc='mean'),
        trip_count=pd.NamedAgg(column='time', aggfunc='count')
    )
    trips_agg.to_sql('analysis_07_time_week', engine, if_exists='append', index=False)

# --- Analysis 8 "time_minutes_week_hour" ---
for year in range(begin_year, end_year + 1):
    current_year = str(year)
    print(f"--- Processing Analysis 8 for {current_year} ---")
    data_files = []
    for month in range(1, 13):
        file_path = os.path.join(local_path, f"yellow_tripdata_{current_year}-{month:02d}.parquet")
        if not os.path.exists(file_path): continue
        df = pd.read_parquet(file_path, engine="pyarrow", columns=cols_default)
        df['tpep_pickup_datetime'] = pd.to_datetime(df['tpep_pickup_datetime'])
        df['tpep_dropoff_datetime'] = pd.to_datetime(df['tpep_dropoff_datetime'])
        df['time'] = ((df['tpep_dropoff_datetime'] - df['tpep_pickup_datetime']).dt.total_seconds() / 60).astype(int)
        rows_before = df.shape[0]
        df.drop(df[(df['time'] < 1) | (df['time'] > 720)].index, inplace=True)
        df['confidence'] = df.shape[0] / rows_before if rows_before > 0 else 0
        data_files.append(df)

    if not data_files: continue
    trips = pd.concat(data_files, ignore_index=True)
    trips['Hour'] = trips['tpep_pickup_datetime'].dt.hour
    trips['Year-Week'] = trips['tpep_pickup_datetime'].dt.strftime('%Y-%V')
    trips_agg = trips.groupby(['Year-Week', 'Hour'], as_index=False).agg(
        avg_time=pd.NamedAgg(column='time', aggfunc='mean'),
        sum_time=pd.NamedAgg(column='time', aggfunc='sum'),
        median_time=pd.NamedAgg(column='time', aggfunc='median'),
        confidence=pd.NamedAgg(column='confidence', aggfunc='mean'),
        trip_count=pd.NamedAgg(column='time', aggfunc='count')
    )
    trips_agg.to_sql('analysis_08_time_week_hour', engine, if_exists='append', index=False)

# --- Analysis 9 "speed_week" ---
cols_default = ['tpep_pickup_datetime', 'tpep_dropoff_datetime', 'trip_distance']
for year in range(begin_year, end_year + 1):
    current_year = str(year)
    print(f"--- Processing Analysis 9 for {current_year} ---")
    data_files = []
    for month in range(1, 13):
        file_path = os.path.join(local_path, f"yellow_tripdata_{current_year}-{month:02d}.parquet")
        if not os.path.exists(file_path): continue
        df = pd.read_parquet(file_path, engine="pyarrow", columns=cols_default)
        df['tpep_pickup_datetime'] = pd.to_datetime(df['tpep_pickup_datetime'])
        df['tpep_dropoff_datetime'] = pd.to_datetime(df['tpep_dropoff_datetime'])
        df['time_hrs'] = ((df['tpep_dropoff_datetime'] - df['tpep_pickup_datetime']).dt.total_seconds() / 3600)
        df = df[(df['time_hrs'] > 0) & (df['trip_distance'] > 0.2)].copy()
        df['speed'] = (df['trip_distance'] * 1.60934) / df['time_hrs']
        data_files.append(df)

    if not data_files: continue
    trips = pd.concat(data_files, ignore_index=True)
    trips['Year-Week'] = trips['tpep_pickup_datetime'].dt.strftime('%Y-%V')
    trips_agg = trips.groupby(['Year-Week'], as_index=False).agg(
        avg_speed=pd.NamedAgg(column='speed', aggfunc='mean'),
        sum_speed=pd.NamedAgg(column='speed', aggfunc='sum'),
        median_speed=pd.NamedAgg(column='speed', aggfunc='median'),
        trip_count=pd.NamedAgg(column='speed', aggfunc='count')
    )
    trips_agg.to_sql('analysis_09_speed_week', engine, if_exists='append', index=False)

# --- Analysis 10 "speed_week_hour" ---
for year in range(begin_year, end_year + 1):
    current_year = str(year)
    print(f"--- Processing Analysis 10 for {current_year} ---")
    data_files = []
    for month in range(1, 13):
        file_path = os.path.join(local_path, f"yellow_tripdata_{current_year}-{month:02d}.parquet")
        if not os.path.exists(file_path): continue
        df = pd.read_parquet(file_path, engine="pyarrow", columns=cols_default)
        df['tpep_pickup_datetime'] = pd.to_datetime(df['tpep_pickup_datetime'])
        df['tpep_dropoff_datetime'] = pd.to_datetime(df['tpep_dropoff_datetime'])
        df['time_hrs'] = ((df['tpep_dropoff_datetime'] - df['tpep_pickup_datetime']).dt.total_seconds() / 3600)
        df = df[(df['time_hrs'] > 0) & (df['trip_distance'] > 0.2)].copy()
        df['speed'] = (df['trip_distance'] * 1.60934) / df['time_hrs']
        data_files.append(df)

    if not data_files: continue
    trips = pd.concat(data_files, ignore_index=True)
    trips['Hour'] = trips['tpep_pickup_datetime'].dt.hour
    trips['Year-Week'] = trips['tpep_pickup_datetime'].dt.strftime('%Y-%V')
    trips_agg = trips.groupby(['Year-Week', 'Hour'], as_index=False).agg(
        avg_speed=pd.NamedAgg(column='speed', aggfunc='mean'),
        sum_speed=pd.NamedAgg(column='speed', aggfunc='sum'),
        median_speed=pd.NamedAgg(column='speed', aggfunc='median'),
        trip_count=pd.NamedAgg(column='speed', aggfunc='count')
    )
    trips_agg.to_sql('analysis_10_speed_week_hour', engine, if_exists='append', index=False)

print("\n--- All 10 analyses have been completed and saved to separate SQL tables ---")
```
#### Index the tables of existing database for much better response time for queries with `db_indexing.py`
``` python
from sqlalchemy import create_engine, text
import time

# --- Configuration ---
# Replace 'your_password' with your actual PostgreSQL password
DB_URI = "postgresql://postgres:password123@localhost:5432/taxi_project"
engine = create_engine(DB_URI)

def create_all_indexes():
    """
    Creates indexes for the raw data table and all 10 analysis tables.
    Run this ONLY after the data ingestion is complete for maximum speed.
    """
    
    # We use double quotes for "Year-Week" because PostgreSQL interprets 
    # the hyphen as a subtraction operator otherwise.
    commands = [
        # --- Raw Data Table Indexes ---
        "CREATE INDEX IF NOT EXISTS idx_raw_pickup ON raw_yellow_taxi_trips (tpep_pickup_datetime);",
        "CREATE INDEX IF NOT EXISTS idx_raw_source_year ON raw_yellow_taxi_trips (source_year);",
        
        # --- Analysis Tables Indexes ---
        "CREATE INDEX IF NOT EXISTS idx_a01_yw ON analysis_01_passenger_count_week (\"Year-Week\");",
        "CREATE INDEX IF NOT EXISTS idx_a02_yw ON analysis_02_passenger_count_week_hour (\"Year-Week\");",
        "CREATE INDEX IF NOT EXISTS idx_a03_yw ON analysis_03_total_amount_week (\"Year-Week\");",
        "CREATE INDEX IF NOT EXISTS idx_a04_yw ON analysis_04_total_amount_week_hour (\"Year-Week\");",
        "CREATE INDEX IF NOT EXISTS idx_a05_yw ON analysis_05_trip_distance_week (\"Year-Week\");",
        "CREATE INDEX IF NOT EXISTS idx_a06_yw ON analysis_06_trip_distance_week_hour (\"Year-Week\");",
        "CREATE INDEX IF NOT EXISTS idx_a07_yw ON analysis_07_time_week (\"Year-Week\");",
        "CREATE INDEX IF NOT EXISTS idx_a08_yw ON analysis_08_time_week_hour (\"Year-Week\");",
        "CREATE INDEX IF NOT EXISTS idx_a09_yw ON analysis_09_speed_week (\"Year-Week\");",
        "CREATE INDEX IF NOT EXISTS idx_a10_yw ON analysis_10_speed_week_hour (\"Year-Week\");"
    ]

    print(f"--- Starting Indexing Process at {time.strftime('%H:%M:%S')} ---")
    
    with engine.connect() as conn:
        for i, cmd in enumerate(commands, 1):
            try:
                start_time = time.time()
                print(f"[{i}/{len(commands)}] Executing: {cmd.split(' ON ')[0]}...")
                
                # Execute and commit
                conn.execute(text(cmd))
                conn.commit()
                
                duration = time.time() - start_time
                print(f"    Done in {duration:.2f} seconds.")
                
            except Exception as e:
                print(f"    ! Error creating index: {e}")
                conn.rollback()

    print(f"--- Maintenance Completed at {time.strftime('%H:%M:%S')} ---")

if __name__ == "__main__":
    create_all_indexes()
```
#### Extracting one of the output tables as Excel file via `db_select.py`
``` python
import pandas as pd
import os
from sqlalchemy import create_engine

# --- Configuration Variables ---
# Update with your actual PostgreSQL password
DB_URI = "postgresql://postgres:password123@localhost:5432/taxi_project"
output_path = "C:\\Python repositories\\Database project\\src\\output_data\\"

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
```
#### Extracting all of the output tables as Excel file via `db_select_all.py`
``` python
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
```

**Author:**
Zbigniew Galar
