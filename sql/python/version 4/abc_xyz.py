import pandas as pd
import numpy as np
import os
from database_manager import get_connection

def run_segmentation():
    print("--- Starting Dynamic ABC/XYZ Animal Segmentation ---")
    conn = get_connection()
    output_folder = os.path.join("src", "output_data")
    
    # Extract data for processing
    df = pd.read_sql("SELECT * FROM actual_sales", conn)
    
    # Calculate Metrics per SKU
    sku_stats = df.groupby('sku')['sales_volume'].agg(['sum', 'mean', 'std']).reset_index()
    sku_stats.columns = ['sku', 'total_volume', 'mean_sales', 'std_dev']
    
    # Coefficient of Variation (CV) = Standard Deviation / Mean
    sku_stats['cv'] = sku_stats['std_dev'] / sku_stats['mean_sales']
    sku_stats['cv'] = sku_stats['cv'].fillna(0)

    # 1. ABC Analysis (Volume-based Ranking)
    sku_stats = sku_stats.sort_values('total_volume', ascending=False)
    sku_stats['cum_vol'] = sku_stats['total_volume'].cumsum()
    total_vol = sku_stats['total_volume'].sum()
    sku_stats['cum_pct'] = sku_stats['cum_vol'] / total_vol
    
    def abc_classify(pct):
        if pct <= 0.80: return 'A' 
        if pct <= 0.95: return 'B' 
        return 'C'                 

    sku_stats['abc'] = sku_stats['cum_pct'].apply(abc_classify)

    # 2. Dynamic XYZ Analysis (Quantile-based Thresholds)
    # Instead of hardcoded values, we calculate the spectrum based on your data
    lower_threshold = sku_stats['cv'].quantile(0.33)
    upper_threshold = sku_stats['cv'].quantile(0.66)
    
    print(f"XYZ Thresholds determined: X <= {lower_threshold:.2f}, Z > {upper_threshold:.2f}")

    def xyz_classify(cv):
        if cv <= lower_threshold: return 'X'  # Stable (Bottom 33% of CV)
        if cv <= upper_threshold: return 'Y'  # Fluctuating (Middle 33% of CV)
        return 'Z'                            # Highly Volatile (Top 33% of CV)

    sku_stats['xyz'] = sku_stats['cv'].apply(xyz_classify)
    
    # 3. Animal Segmentation Logic
    # Mapping based on your specific table
    animal_map = {
        'AX': 'Horses',   'BX': 'Horses',
        'AY': 'Mad Bulls', 'AZ': 'Mad Bulls', 'BY': 'Mad Bulls', 'BZ': 'Mad Bulls',
        'CX': 'Turtles',
        'CY': 'Rabbits',  'CZ': 'Rabbits'
    }
    
    sku_stats['segment_code'] = sku_stats['abc'] + sku_stats['xyz']
    sku_stats['animal_persona'] = sku_stats['segment_code'].map(animal_map)

    # 4. Save and Export
    sku_stats.to_excel(os.path.join(output_folder, "abc_xyz_segmentation.xlsx"), index=False)
    
    # Update SQL table for analytical use
    conn = get_connection()
    sku_stats[['sku', 'abc', 'xyz', 'animal_persona', 'cv']].to_sql('sku_segmentation', conn, if_exists='replace', index=False)
    conn.close()
    
    print("Exported: abc_xyz_segmentation.xlsx and updated SQL table 'sku_segmentation'")
    print("--- Segmentation Complete ---")

if __name__ == "__main__":
    run_segmentation()
