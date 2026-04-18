import os
import pandas as pd
from datetime import datetime
from database_manager import create_tables, save_to_sql
from data_ingestion import process_excel
from models import run_ses_forecast, run_moving_average

def run_pipeline(file_name):
    # 1. Setup Database
    print("--- Initializing Database ---")
    create_tables()

    # 2. Data Ingestion & Cleaning
    # Ignore the ~$ temporary files Excel creates
    if file_name.startswith("~$"):
        print("Skipping temporary Excel file.")
        return

    input_path = os.path.join("src", "input_data", file_name)
    print(f"--- Processing {file_name} ---")
    df_monthly = process_excel(input_path)
    
    # Save historical data to SQL
    save_to_sql(df_monthly, 'actual_sales')

    # 3. Forecasting Loop
    all_forecasts = []
    unique_skus = df_monthly['sku'].unique()
    execution_date = datetime.now().date()

    print(f"--- Generating Forecasts for {len(unique_skus)} SKUs ---")
    
    for sku in unique_skus:
        # Get historical data for this specific SKU
        sku_data = df_monthly[df_monthly['sku'] == sku].sort_values('date')
        series = sku_data['sales_volume']
        
        # We need at least 2 data points for SES
        if len(series) < 2:
            continue

        # Generate Dates for the next 24 months
        last_date = sku_data['date'].max()
        forecast_dates = pd.date_range(start=last_date, periods=25, freq='MS')[1:]

        # Run Models
        ses_pred = run_ses_forecast(series, months=24)
        ma_pred = run_moving_average(series, months=24)

        # Prepare SES data for SQL
        for date, val in zip(forecast_dates, ses_pred):
            all_forecasts.append({
                'sku': sku,
                'forecast_date': date.date(),
                'predicted_value': round(val, 2),
                'model_name': 'Simple Exponential Smoothing',
                'execution_date': execution_date
            })

        # Prepare MA data for SQL
        for date, val in zip(forecast_dates, ma_pred):
            all_forecasts.append({
                'sku': sku,
                'forecast_date': date.date(),
                'predicted_value': round(val, 2),
                'model_name': 'Moving Average (3M)',
                'execution_date': execution_date
            })

    # 4. Save Forecasts to SQL
    if all_forecasts:
        forecast_df = pd.DataFrame(all_forecasts)
        save_to_sql(forecast_df, 'forecasts')
        print(f"--- Pipeline Complete. {len(all_forecasts)} forecast rows saved. ---")

if __name__ == "__main__":
    # Point to your specific file name from the screenshot
    run_pipeline("Sales.xlsx")
