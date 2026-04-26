from statsmodels.tsa.holtwinters import SimpleExpSmoothing, ExponentialSmoothing
import pandas as pd
import numpy as np

# --- 1. PARAMETERIZED MOVING AVERAGES ---

def run_moving_average_3(series, window=3, months=24):
    """3-Month Moving Average."""
    last_ma = series.tail(window).mean()
    return [last_ma] * months

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


# --- 2. PARAMETERIZED SES (ALPHA SWEEPING) ---

def run_ses_forecast(series, months=24):
    """Standard SES (optimized alpha)."""
    model = SimpleExpSmoothing(series, initialization_method="estimated").fit()
    return model.forecast(months)

def run_ses_alpha_0_1(series, months=24):
    model = SimpleExpSmoothing(series).fit(smoothing_level=0.1, optimized=False)
    return model.forecast(months)

def run_ses_alpha_0_2(series, months=24):
    model = SimpleExpSmoothing(series).fit(smoothing_level=0.2, optimized=False)
    return model.forecast(months)

def run_ses_alpha_0_3(series, months=24):
    model = SimpleExpSmoothing(series).fit(smoothing_level=0.3, optimized=False)
    return model.forecast(months)

def run_ses_alpha_0_4(series, months=24):
    model = SimpleExpSmoothing(series).fit(smoothing_level=0.4, optimized=False)
    return model.forecast(months)

def run_ses_alpha_0_5(series, months=24):
    model = SimpleExpSmoothing(series).fit(smoothing_level=0.5, optimized=False)
    return model.forecast(months)

def run_ses_alpha_0_6(series, months=24):
    model = SimpleExpSmoothing(series).fit(smoothing_level=0.6, optimized=False)
    return model.forecast(months)

def run_ses_alpha_0_7(series, months=24):
    model = SimpleExpSmoothing(series).fit(smoothing_level=0.7, optimized=False)
    return model.forecast(months)

def run_ses_alpha_0_8(series, months=24):
    model = SimpleExpSmoothing(series).fit(smoothing_level=0.8, optimized=False)
    return model.forecast(months)

def run_ses_alpha_0_9(series, months=24):
    model = SimpleExpSmoothing(series).fit(smoothing_level=0.9, optimized=False)
    return model.forecast(months)


# --- 3. HOLT-WINTERS (ADVANCED SEASONAL MODELS) ---

def run_holt_winters_additive(series, months=24):
    """Holt-Winters with Additive Trend and Seasonality."""
    try:
        # Requires at least 24 months for stable seasonal estimation
        model = ExponentialSmoothing(
            series, trend='add', seasonal='add', seasonal_periods=12, 
            initialization_method="estimated"
        ).fit()
        return model.forecast(months)
    except:
        return run_ses_forecast(series, months)

def run_holt_winters_multiplicative(series, months=24):
    """Holt-Winters with Multiplicative Seasonality."""
    try:
        # Multiplicative models require strictly positive data
        if (series <= 0).any():
            return run_holt_winters_additive(series, months)
        model = ExponentialSmoothing(
            series, trend='add', seasonal='mul', seasonal_periods=12, 
            initialization_method="estimated"
        ).fit()
        return model.forecast(months)
    except:
        return run_ses_forecast(series, months)

def run_holt_trend_only(series, months=24):
    """Holt's Linear Trend (No Seasonality)."""
    try:
        model = ExponentialSmoothing(
            series, trend='add', seasonal=None, 
            initialization_method="estimated"
        ).fit()
        return model.forecast(months)
    except:
        return run_ses_forecast(series, months)
