import pandas as pd
import numpy as np
import inspect
import models 
import evaluation

def get_dynamic_members(module, prefix):
    """Helper to find functions in a module by prefix"""
    return [func for name, func in inspect.getmembers(module, inspect.isfunction) if name.startswith(prefix)]

def run_backtest_for_sku(sku_data, backtest_months, metric='MAPE'):
    sku_data = sku_data.sort_values('date').copy()
    sku = sku_data['sku'].iloc[0]
    
    if len(sku_data) <= backtest_months:
        return None, None

    train_data = sku_data.iloc[:-backtest_months]
    test_data = sku_data.iloc[-backtest_months:]
    actual_values = test_data['sales_volume'].values
    test_dates = test_data['date'].values
    
    backtest_details = []
    summary_results = []
    
    available_models = get_dynamic_members(models, 'run_')
    available_metrics = evaluation.get_available_metrics() # Dict of {NAME: func}

    for model_func in available_models:
        model_name = model_func.__name__.replace('run_', '').replace('_', ' ').title()
        
        try:
            preds = model_func(train_data['sales_volume'], months=backtest_months)
            preds = np.array(preds).flatten()
            
            # 1. Collect Granular Results (Detail Table)
            for i in range(len(test_dates)):
                row = {
                    'sku': sku,
                    'date': test_dates[i],
                    'model_name': model_name,
                    'predicted_value': round(float(preds[i]), 2),
                    'actual_value': float(actual_values[i])
                }
                # Dynamically add every metric found in evaluation.py
                for m_name, m_func in available_metrics.items():
                    row[m_name.lower()] = round(m_func([actual_values[i]], [preds[i]]), 4)
                backtest_details.append(row)
            
            # 2. Collect Aggregate Performance (Summary Table)
            summary_row = {'sku': sku, 'model_name': model_name}
            for m_name, m_func in available_metrics.items():
                summary_row[m_name.lower()] = round(m_func(actual_values, preds), 4)
            summary_results.append(summary_row)
            
        except Exception as e:
            print(f"Error skipping {model_name} for SKU {sku}: {e}")
            continue

    return backtest_details, summary_results
