import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

# --- Configuration ---
DB_NAME = "taxi_small_project"
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
