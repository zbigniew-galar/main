from sqlalchemy import create_engine, text

# --- Configuration ---
DB_URI = "postgresql://postgres:password123@localhost:5432/taxi_small_project"
engine = create_engine(DB_URI)

def wipe_test_data():
    """Drops all tables to ensure a clean start for the full 17-year run."""
    tables = [
        "raw_yellow_taxi_trips"
    ]
    
    print("--- Warning: This will delete all existing data in the taxi_project database ---")
    confirm = input("Type 'YES' to confirm: ")
    
    if confirm == "YES":
        with engine.connect() as conn:
            for table in tables:
                conn.execute(text(f"DROP TABLE IF EXISTS {table} CASCADE;"))
                print(f" Dropped: {table}")
            conn.commit()
        print("\n--- Database is now empty and ready for the full run ---")
    else:
        print("Operation cancelled.")

if __name__ == "__main__":
    wipe_test_data()
