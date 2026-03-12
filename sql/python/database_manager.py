import sqlite3
import pandas as pd

DB_PATH = "src/output_data/sales_forecast.db"

def create_tables():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Create table for Actual Sales
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS actual_sales (
            sku TEXT,
            date DATE,
            sales_volume INTEGER,
            PRIMARY KEY (sku, date)
        )
    ''')
    
    # Create table for Forecasts
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS forecasts (
            sku TEXT,
            forecast_date DATE,
            predicted_value REAL,
            model_name TEXT,
            execution_date DATE
        )
    ''')
    conn.commit()
    conn.close()

def save_to_sql(df, table_name):
    conn = sqlite3.connect(DB_PATH)
    # This automatically maps Pandas columns to SQL columns
    df.to_sql(table_name, conn, if_exists='append', index=False)
    conn.close()
