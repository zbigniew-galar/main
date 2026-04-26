import numpy as np
import pandas as pd
import inspect

def metric_mape(actual, forecast):
    """Mean Absolute Percentage Error"""
    actual, forecast = np.array(actual), np.array(forecast)
    mask = actual != 0
    if not np.any(mask): return np.inf
    return np.mean(np.abs((actual[mask] - forecast[mask]) / actual[mask])) * 100

def metric_smape(actual, forecast):
    """Symmetric Mean Absolute Percentage Error"""
    actual, forecast = np.array(actual), np.array(forecast)
    denominator = (np.abs(actual) + np.abs(forecast))
    mask = denominator != 0
    if not np.any(mask): return np.inf
    return np.mean(2.0 * np.abs(actual[mask] - forecast[mask]) / denominator[mask]) * 100

def get_available_metrics():
    """Dynamically finds all functions starting with 'metric_'"""
    current_module = inspect.getmodule(inspect.currentframe())
    functions = inspect.getmembers(current_module, inspect.isfunction)
    return {name.replace('metric_', '').upper(): func for name, func in functions if name.startswith('metric_')}

def calculate_error(actual, forecast, metric='SMAPE'):
    """Universal caller for dynamic metrics"""
    metrics_map = get_available_metrics()
    metric_key = metric.upper()
    
    if metric_key not in metrics_map:
        raise ValueError(f"Metric {metric_key} not found. Available: {list(metrics_map.keys())}")
    
    return metrics_map[metric_key](actual, forecast)

def get_best_model(performance_list, metric='SMAPE'):
    """Selects the winner based on the chosen metric key"""
    if not performance_list: return None
    key = metric.lower() # Assumes dictionary keys in backtest_hub are lowercase metric names
    try:
        return min(performance_list, key=lambda x: x.get(key, np.inf))
    except Exception:
        return performance_list[0]
