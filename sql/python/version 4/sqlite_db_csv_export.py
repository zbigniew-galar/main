import sqlite3
import pandas as pd
from pathlib import Path

DB_PATH = Path("src/output_data/sales_forecast.db")
OUTPUT_DIR = DB_PATH.parent

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
conn = sqlite3.connect(DB_PATH)

tables = pd.read_sql_query("SELECT name FROM sqlite_master WHERE type='table';", conn)['name']

for table in tables:
    pd.read_sql_query(f"SELECT * FROM {table}", conn).to_csv(OUTPUT_DIR / f"{table}.csv", index=False)

conn.close()
