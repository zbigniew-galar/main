import sqlite3
import pandas as pd

conn = sqlite3.connect("src/output_data/sales_forecast.db")
query = """
SELECT sku, SUM(sales_volume) as total_volume 
FROM actual_sales 
GROUP BY sku 
ORDER BY total_volume DESC;
"""
print(pd.read_sql(query, conn))
conn.close()
