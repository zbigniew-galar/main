import os
import pandas as pd
import warnings
from datetime import datetime

# Import modular components
from database_manager import create_tables, save_to_sql
from data_ingestion import process_excel
from models import run_ses_forecast, run_moving_average, run_moving_average_6, run_moving_average_9, run_moving_average_12
from backtesting_hub import run_backtest_for_sku
from evaluation import get_best_model
from accuracy_report import run_all_reports
from sales_analytics import run_analytics
from abc_xyz import run_segmentation

# --- CONFIGURATION PARAMETERS ---
BACKTEST_MONTHS = 6          # Number of months to go back for validation
SELECTION_METRIC = 'MAPE'    # Metric to decide the 'Best' model (MAPE or SMAPE)
FORECAST_HORIZON = 24        # Months to forecast into the future
INPUT_FILE = "Sales.xlsx"    # Your source data file
# --------------------------------

# Silence mathematical noise for a clean terminal output
warnings.filterwarnings("ignore", category=RuntimeWarning)
warnings.filterwarnings("ignore", category=UserWarning)

def run_pipeline(file_name):
    # 1. Setup Database
    print(f"--- [1/6] Initializing Database & Tables ---")
    create_tables()

    # 2. Data Ingestion
    if file_name.startswith("~$"):
        return

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    input_path = os.path.join(BASE_DIR, "input_data", file_name)
    
    print(f"--- [2/6] Ingesting {file_name} ---")
    try:
        df_monthly = process_excel(input_path)
        save_to_sql(df_monthly, 'actual_sales')
    except Exception as e:
        print(f"CRITICAL ERROR during ingestion: {e}")
        return

    # 3. Descriptive Analytics & Segmentation
    print(f"--- [3/6] Running Sales Analytics & Animal Segmentation ---")
    run_analytics()      # Generates Lags, Rolling Stats, and Outlier reports
    run_segmentation()   # Assigns Horses, Mad Bulls, Turtles, and Rabbits

    # 4. Backtesting & Model Selection
    all_backtest_details = []
    all_model_performance = []
    final_forecast_output = []
    
    unique_skus = df_monthly['sku'].unique()
    execution_date = datetime.now().date()
    
    print(f"--- [4/6] Backtesting & Selecting Best Models (Metric: {SELECTION_METRIC}) ---")
    
    for sku in unique_skus:
        sku_data = df_monthly[df_monthly['sku'] == sku].sort_values('date')
        
        # Run the dynamic backtesting hub
        details, summary = run_backtest_for_sku(sku_data, BACKTEST_MONTHS, SELECTION_METRIC)
        
        if not details or not summary:
            continue
            
        # Identify the winner for this SKU
        best_model_info = get_best_model(summary, SELECTION_METRIC)
        winner_name = best_model_info['model_name']
        
        # Mark the winner in the performance summary
        for item in summary:
            item['is_best'] = 1 if item['model_name'] == winner_name else 0
            all_model_performance.append(item)
        
        all_backtest_details.extend(details)

        # 5. Production Forecast: Run winner on full dataset
        try:
            last_date = pd.to_datetime(sku_data['date'].max())
            forecast_dates = pd.date_range(start=last_date, periods=FORECAST_HORIZON + 1, freq='MS')[1:]
            
            series = sku_data['sales_volume']
            if "Smoothing" in winner_name:
                preds = run_ses_forecast(series, months=FORECAST_HORIZON)
            else:
                preds = run_moving_average(series, months=FORECAST_HORIZON)
                
            for d, val in zip(forecast_dates, preds):
                final_forecast_output.append({
                    'sku': sku,
                    'forecast_date': d.strftime('%Y-%m-%d'),
                    'predicted_value': round(float(val), 2),
                    'model_name': winner_name,
                    'execution_date': execution_date
                })
        except Exception:
            continue

    # 6. Finalizing SQL & Exporting Reports
    print(f"--- [5/6] Updating SQL Analytical Framework ---")
    if all_backtest_details:
        save_to_sql(pd.DataFrame(all_backtest_details), 'backtest_details')
    if all_model_performance:
        save_to_sql(pd.DataFrame(all_model_performance), 'model_performance')
    if final_forecast_output:
        save_to_sql(pd.DataFrame(final_forecast_output), 'forecasts')

    print(f"--- [6/6] Generating Final Excel Reports ---")
    run_all_reports()

    print(f"\nPipeline Execution Successful.")
    print(f"Processed {len(unique_skus)} SKUs. All outputs saved in 'src/output_data/'.")

if __name__ == "__main__":
    run_pipeline(INPUT_FILE)
