from sqlalchemy import create_engine, text
import time

# --- Configuration ---
# Replace 'your_password' with your actual PostgreSQL password
DB_URI = "postgresql://postgres:password123@localhost:5432/taxi_small_project"
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
