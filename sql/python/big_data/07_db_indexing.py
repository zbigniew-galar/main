from sqlalchemy import create_engine, text
import time

# --- Configuration ---
# Replace 'your_password' with your actual PostgreSQL password
DB_URI = "postgresql://postgres:password123@localhost:5432/taxi_small_project"
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
