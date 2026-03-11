import sqlite3
import pandas as pd
conn = sqlite3.connect("src/output_data/sales_forecast.db")
print(pd.read_sql("SELECT * FROM forecasts LIMIT 5", conn))
conn.close()
