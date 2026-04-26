import os
import pandas as pd
import warnings
from datetime import datetime
import models  # Import the module to allow dynamic function access

# Import modular components
from database_manager import create_tables, save_to_sql
from data_ingestion import process_excel
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

# Silence mathematical noise
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
    run_analytics()
    run_segmentation()

    # 4. Backtesting & Model Selection
    all_backtest_details = []
    all_model_performance = []
    final_forecast_output = []
    
    unique_skus = df_monthly['sku'].unique()
    execution_date = datetime.now().date()
    
    print(f"--- [4/6] Backtesting {len(unique_skus)} SKUs with All Models ---")
    
    for sku in unique_skus:
        sku_data = df_monthly[df_monthly['sku'] == sku].sort_values('date')
        
        # Run the dynamic backtesting hub (detects all 'run_' functions)
        details, summary = run_backtest_for_sku(sku_data, BACKTEST_MONTHS, SELECTION_METRIC)
        
        if not details or not summary:
            continue
            
        # Identify the winner for this SKU
        best_model_info = get_best_model(summary, SELECTION_METRIC)
        winner_display_name = best_model_info['model_name']
        
        # Convert display name back to function name: 'Ses Alpha 0 1' -> 'run_ses_alpha_0_1'
        winner_func_name = "run_" + winner_display_name.lower().replace(" ", "_")
        
        # Mark the winner in the performance summary for SQL
        for item in summary:
            item['is_best'] = 1 if item['model_name'] == winner_display_name else 0
            all_model_performance.append(item)
        
        all_backtest_details.extend(details)

        # 5. Production Forecast: DYNAMICALLY call the winning function
        try:
            last_date = pd.to_datetime(sku_data['date'].max())
            forecast_dates = pd.date_range(start=last_date, periods=FORECAST_HORIZON + 1, freq='MS')[1:]
            
            # Fetch the actual function from the models module by its string name
            winning_func = getattr(models, winner_func_name)
            
            # Execute the specific winner (SES or MA with specific parameters)
            preds = winning_func(sku_data['sales_volume'], months=FORECAST_HORIZON)
                
            for d, val in zip(forecast_dates, preds):
                final_forecast_output.append({
                    'sku': sku,
                    'forecast_date': d.strftime('%Y-%m-%d'),
                    'predicted_value': round(float(val), 2),
                    'model_name': winner_display_name,
                    'execution_date': execution_date
                })
        except Exception as e:
            print(f"Error forecasting SKU {sku} with {winner_func_name}: {e}")
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
    print(f"Check 'src/output_data/' for results.")

if __name__ == "__main__":
    run_pipeline(INPUT_FILE)
