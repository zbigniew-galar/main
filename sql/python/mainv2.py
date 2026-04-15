import os
import pandas as pd
import warnings
from datetime import datetime

# Import modular components
from database_manager import create_tables, save_to_sql
from data_ingestion import process_excel
from models import run_ses_forecast, run_moving_average

# 1. Professional Setup: Silence mathematical warnings (Divide by zero, etc.)
warnings.filterwarnings("ignore", category=RuntimeWarning)
warnings.filterwarnings("ignore", category=UserWarning)

def run_pipeline(file_name):
    # Setup Database (creates file if not exists)
    print("--- [1/4] Initializing Database ---")
    create_tables()

    # Data Ingestion & Cleaning
    if file_name.startswith("~$"):
        return

    input_path = os.path.join("src", "input_data", file_name)
    print(f"--- [2/4] Processing {file_name} ---")
    
    try:
        df_monthly = process_excel(input_path)
        # We use 'replace' here to ensure a clean state for production runs
        save_to_sql(df_monthly, 'actual_sales')
    except Exception as e:
        print(f"CRITICAL ERROR during ingestion: {e}")
        return

    # Forecasting Engine
    all_forecasts = []
    unique_skus = df_monthly['sku'].unique()
    execution_date = datetime.now().date()
    
    success_count = 0
    fail_count = 0

    print(f"--- [3/4] Generating Forecasts for {len(unique_skus)} SKUs ---")
    
    for sku in unique_skus:
        sku_data = df_monthly[df_monthly['sku'] == sku].sort_values('date')
        series = sku_data['sales_volume']
        
        # Filter: Skip SKUs with insufficient history (need at least 2 data points)
        if len(series[series > 0]) < 2:
            fail_count += 1
            continue

        try:
            last_date = sku_data['date'].max()
            forecast_dates = pd.date_range(start=last_date, periods=25, freq='MS')[1:]

            # Model Execution
            ses_pred = run_ses_forecast(series, months=24)
            ma_pred = run_moving_average(series, months=24)

            # Data Formatting for SQL
            for date, ses_val, ma_val in zip(forecast_dates, ses_pred, ma_pred):
                # SES Record
                all_forecasts.append({
                    'sku': sku, 'forecast_date': date.date(),
                    'predicted_value': round(float(ses_val), 2),
                    'model_name': 'Simple Exponential Smoothing',
                    'execution_date': execution_date
                })
                # MA Record
                all_forecasts.append({
                    'sku': sku, 'forecast_date': date.date(),
                    'predicted_value': round(float(ma_val), 2),
                    'model_name': 'Moving Average (3M)',
                    'execution_date': execution_date
                })
            success_count += 1

        except Exception:
            # Silently fail for the SKU and move to next
            fail_count += 1
            continue

    # 4. Final Output to SQL
    print(f"--- [4/4] Saving Results ---")
    if all_forecasts:
        forecast_df = pd.DataFrame(all_forecasts)
        # Using 'replace' to ensure old forecasts don't mix with new ones
        save_to_sql(forecast_df, 'forecasts')
        
    print(f"\nPipeline Complete:")
    print(f" - Successfully forecasted: {success_count} SKUs")
    print(f" - Skipped (Incomplete Data): {fail_count} SKUs")
    print(f" - Total rows saved to SQL: {len(all_forecasts)}")

if __name__ == "__main__":
    run_pipeline("Sales.xlsx")
