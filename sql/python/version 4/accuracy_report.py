import pandas as pd
import os

# Handle import regardless of execution context
try:
    from database_manager import get_connection
except ImportError:
    from src.database_manager import get_connection

# Configuration: Analytical SQL Queries
# We leverage JOINs between model_performance and sku_segmentation
REPORTS_CONFIG = {
    "backtest_granular_analysis.xlsx": """
        SELECT 
            b.sku, 
            s.animal_persona,
            b.date, 
            b.model_name, 
            b.actual_value, 
            b.predicted_value,
            b.mape,
            b.smape
        FROM backtest_details b
        LEFT JOIN sku_segmentation s ON b.sku = s.sku
        ORDER BY s.animal_persona, b.sku, b.date
    """,
    
    "model_comparison_by_animal.xlsx": """
        SELECT 
            s.animal_persona,
            m.model_name, 
            AVG(m.mape) as avg_mape, 
            AVG(m.smape) as avg_smape,
            COUNT(DISTINCT m.sku) as sku_count
        FROM model_performance m
        JOIN sku_segmentation s ON m.sku = s.sku
        GROUP BY s.animal_persona, m.model_name
        ORDER BY s.animal_persona, avg_mape ASC
    """,
    
    "best_model_per_sku_full_context.xlsx": """
        SELECT 
            m.sku,
            s.abc,
            s.xyz,
            s.animal_persona,
            m.model_name,
            m.mape,
            m.smape
        FROM model_performance m
        JOIN sku_segmentation s ON m.sku = s.sku
        WHERE m.is_best = 1
        ORDER BY s.abc, s.xyz
    """,
    
    "future_forecast_with_segments.xlsx": """
        SELECT 
            f.sku, 
            s.animal_persona,
            f.forecast_date, 
            f.predicted_value, 
            f.model_name
        FROM forecasts f
        LEFT JOIN sku_segmentation s ON f.sku = s.sku
        ORDER BY s.animal_persona, f.sku, f.forecast_date
    """
}

def export_report_to_excel(query, filename):
    """
    Executes a SQL query and saves the result as an Excel file in the output folder.
    """
    output_folder = os.path.join("src", "output_data")
    
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        
    full_path = os.path.join(output_folder, filename)
    
    try:
        conn = get_connection()
        df = pd.read_sql(query, conn)
        conn.close()
        
        if not df.empty:
            df.to_excel(full_path, index=False)
            print(f"Successfully exported: {filename}")
        else:
            print(f"Report {filename} skipped: No data returned.")
            
    except Exception as e:
        print(f"Error generating {filename}: {e}")

def run_all_reports():
    """
    Orchestrates the export of the entire analytical suite.
    """
    print("--- Starting Enhanced Analytical Report Export ---")
    for filename, query in REPORTS_CONFIG.items():
        export_report_to_excel(query, filename)
    print("--- All reports finished ---")

if __name__ == "__main__":
    run_all_reports()
