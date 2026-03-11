import pandas as pd

def process_excel(file_path):
    df = pd.read_excel(file_path)
    df['Date'] = pd.to_datetime(df['Date'])
    
    # Aggregate daily to monthly per SKU
    df_monthly = df.groupby(['SKU', pd.Grouper(key='Date', freq='MS')]).sum().reset_index()
    
    # Standardize column names for SQL
    df_monthly.columns = ['sku', 'date', 'sales_volume']
    return df_monthly
