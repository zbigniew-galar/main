from statsmodels.tsa.holtwinters import SimpleExpSmoothing
import pandas as pd
import numpy as np

# --- 1. BACKWARD COMPATIBLE MODELS (Standard Names) ---

def run_ses_forecast(series, months=24):
    """
    Standard Simple Exponential Smoothing (optimized alpha).
    Maintained for backward compatibility with existing main.py imports.
    """
    model = SimpleExpSmoothing(series, initialization_method="estimated").fit()
    return model.forecast(months)

def run_moving_average(series, window=3, months=24):
    """
    Standard 3-Month Moving Average.
    Maintained for backward compatibility with existing main.py imports.
    """
    last_ma = series.tail(window).mean()
    return [last_ma] * months


# --- 2. PARAMETERIZED BRUTE-FORCE MODELS ---

def run_moving_average_6(series, window=6, months=24):
    """6-Month Moving Average."""
    last_ma = series.tail(window).mean()
    return [last_ma] * months

def run_moving_average_9(series, window=9, months=24):
    """9-Month Moving Average."""
    last_ma = series.tail(window).mean()
    return [last_ma] * months

def run_moving_average_12(series, window=12, months=24):
    """12-Month Moving Average."""
    last_ma = series.tail(window).mean()
    return [last_ma] * months
