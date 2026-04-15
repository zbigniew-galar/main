import pandas as pd
import numpy as np
import os
from database_manager import get_connection

def calculate_pearson_logic(df):
    """
    Calculates the specific 6-month YoY correlation requested.
    """
    # Pivot to get SKU as rows and Dates as columns
    pivot_df = df.pivot(index='sku', columns='date', values='sales_volume').fillna(0)
    dates = sorted(pivot_df.columns)
    
    if len(dates) < 18:  # Need at least 18 months for a 6-month YoY check
        return pd.DataFrame()

    # Define windows
    last_6 = dates[-6:]
    last_year_6 = dates[-18:-12]
    
    results = []
    for sku in pivot_df.index:
        y_current = pivot_df.loc[sku, last_6].values
        y_prior = pivot_df.loc[sku, last_year_6].values
        
        # Pearson Calculation
        if np.std(y_current) == 0 or np.std(y_prior) == 0:
            corr = 0
        else:
            corr = np.corrcoef(y_current, y_prior)[0, 1]
        
        # Logic Flags
        direction = "Positive" if corr > 0 else "Negative" if corr < 0 else "Neutral"
        is_strong = "Yes" if corr > 0.7 else "No"
        r_sq = f"{round(corr**2 * 100, 2)}%" if corr > 0.7 else "-"
        
        results.append({
            'sku': sku,
            'pearson_correlation': round(corr, 4),
            'direction': direction,
            'strong_positive_70': is_strong,
            'r_squared_pct': r_sq
        })
    
    return pd.DataFrame(results)

def run_analytics():
    print("--- Starting Historical Sales Analytics ---")
    conn = get_connection()
    output_folder = os.path.join("src", "output_data")
    
    # 1. Descriptive Statistics (Quartiles & Distribution)
    # Since SQLite lacks percentiles, we pull to Pandas for the heavy lifting
    df_raw = pd.read_sql("SELECT * FROM actual_sales", conn)
    
    desc_stats = df_raw.groupby('sku')['sales_volume'].describe(percentiles=[.25, .5, .75])
    desc_stats = desc_stats.rename(columns={'25%': '1st_quartile', '50%': 'median', '75%': '3rd_quartile'})
    desc_stats.to_excel(os.path.join(output_folder, "sku_distribution_stats.xlsx"))
    print("Exported: sku_distribution_stats.xlsx")

    # 2. Pearson Correlation Table
    corr_df = calculate_pearson_logic(df_raw)
    if not corr_df.empty:
        corr_df.to_excel(os.path.join(output_folder, "sales_seasonality_correlation.xlsx"), index=False)
        print("Exported: sales_seasonality_correlation.xlsx")

    # 3. Rolling Statistics (3M & 6M)
    df_raw['date'] = pd.to_datetime(df_raw['date'])
    df_raw = df_raw.sort_values(['sku', 'date'])
    df_raw['rolling_avg_3m'] = df_raw.groupby('sku')['sales_volume'].transform(lambda x: x.rolling(3).mean())
    df_raw['rolling_std_3m'] = df_raw.groupby('sku')['sales_volume'].transform(lambda x: x.rolling(3).std())
    df_raw.to_excel(os.path.join(output_folder, "rolling_stats.xlsx"), index=False)
    print("Exported: rolling_stats.xlsx")

    # 4. Lag Features (t-1, t-12)
    df_lags = df_raw.copy()
    df_lags['sales_lag_1'] = df_lags.groupby('sku')['sales_volume'].shift(1)
    df_lags['sales_lag_12'] = df_lags.groupby('sku')['sales_volume'].shift(12)
    df_lags.to_excel(os.path.join(output_folder, "lag_features.xlsx"), index=False)
    print("Exported: lag_features.xlsx")

    # 5. Outlier Detection (Z-Score > 3)
    df_outliers = df_raw.copy()
    df_outliers['mean'] = df_outliers.groupby('sku')['sales_volume'].transform('mean')
    df_outliers['std'] = df_outliers.groupby('sku')['sales_volume'].transform('std')
    df_outliers['z_score'] = (df_outliers['sales_volume'] - df_outliers['mean']) / df_outliers['std']
    df_outliers['is_outlier'] = df_outliers['z_score'].apply(lambda x: "Yes" if abs(x) > 3 else "No")
    # Brute Force Capping
    df_outliers['capped_sales'] = np.where(df_outliers['z_score'] > 3, df_outliers['mean'] + (3 * df_outliers['std']), 
                                           np.where(df_outliers['z_score'] < -3, df_outliers['mean'] - (3 * df_outliers['std']), df_outliers['sales_volume']))
    
    df_outliers.to_excel(os.path.join(output_folder, "outlier_detection_capping.xlsx"), index=False)
    print("Exported: outlier_detection_capping.xlsx")

    conn.close()
    print("--- Analytics Complete ---")

if __name__ == "__main__":
    run_analytics()
