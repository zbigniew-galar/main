from sqlalchemy import create_engine, text
import time

# --- Configuration ---
# Update 'your_password' with your PostgreSQL password
DB_URI = "postgresql://postgres:password123@localhost:5432/taxi_small_project"
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
