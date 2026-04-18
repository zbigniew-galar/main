import sqlite3
import pandas as pd

DB_PATH = "src/output_data/sales_forecast.db"

def create_tables():
    """Initializes the analytical framework schema."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # 1. ACTUAL SALES
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS actual_sales (
            sku TEXT,
            date DATE,
            sales_volume REAL,
            PRIMARY KEY (sku, date)
        )
    ''')
    
    # 2. BACKTEST_DETAILS
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS backtest_details (
            sku TEXT,
            date DATE,
            model_name TEXT,
            predicted_value REAL,
            actual_value REAL,
            mape REAL,
            smape REAL
        )
    ''')
    
    # 3. MODEL_PERFORMANCE
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS model_performance (
            sku TEXT,
            model_name TEXT,
            avg_mape REAL,
            avg_smape REAL,
            is_best INTEGER DEFAULT 0
        )
    ''')

    # 4. FINAL FORECASTS
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS forecasts (
            sku TEXT,
            forecast_date DATE,
            predicted_value REAL,
            model_name TEXT,
            execution_date DATE,
            PRIMARY KEY (sku, forecast_date, execution_date)
        )
    ''')
    
    conn.commit()
    conn.close()

def save_to_sql(df, table_name, if_exists='replace'):
    """Universal saver for dynamic tables."""
    conn = sqlite3.connect(DB_PATH)
    try:
        df.to_sql(table_name, conn, if_exists=if_exists, index=False)
    except Exception as e:
        print(f"Error saving to {table_name}: {e}")
    finally:
        conn.close()

def get_connection():
    """Utility used by accuracy_report.py to run SQL queries."""
    return sqlite3.connect(DB_PATH)
