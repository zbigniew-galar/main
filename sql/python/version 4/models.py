from statsmodels.tsa.holtwinters import SimpleExpSmoothing

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
    """
    Standard SES where alpha is automatically optimized by statsmodels.
    """
    model = SimpleExpSmoothing(series, initialization_method="estimated").fit()
    return model.forecast(months)

def run_ses_alpha_0_1(series, months=24):
    """SES with Alpha = 0.1 (Extremely smooth/stable)."""
    model = SimpleExpSmoothing(series).fit(smoothing_level=0.1, optimized=False)
    return model.forecast(months)

def run_ses_alpha_0_2(series, months=24):
    """SES with Alpha = 0.2."""
    model = SimpleExpSmoothing(series).fit(smoothing_level=0.2, optimized=False)
    return model.forecast(months)

def run_ses_alpha_0_3(series, months=24):
    """SES with Alpha = 0.3."""
    model = SimpleExpSmoothing(series).fit(smoothing_level=0.3, optimized=False)
    return model.forecast(months)

def run_ses_alpha_0_4(series, months=24):
    """SES with Alpha = 0.4."""
    model = SimpleExpSmoothing(series).fit(smoothing_level=0.4, optimized=False)
    return model.forecast(months)

def run_ses_alpha_0_5(series, months=24):
    """SES with Alpha = 0.5 (Balanced reactivity)."""
    model = SimpleExpSmoothing(series).fit(smoothing_level=0.5, optimized=False)
    return model.forecast(months)

def run_ses_alpha_0_6(series, months=24):
    """SES with Alpha = 0.6."""
    model = SimpleExpSmoothing(series).fit(smoothing_level=0.6, optimized=False)
    return model.forecast(months)

def run_ses_alpha_0_7(series, months=24):
    """SES with Alpha = 0.7."""
    model = SimpleExpSmoothing(series).fit(smoothing_level=0.7, optimized=False)
    return model.forecast(months)

def run_ses_alpha_0_8(series, months=24):
    """SES with Alpha = 0.8."""
    model = SimpleExpSmoothing(series).fit(smoothing_level=0.8, optimized=False)
    return model.forecast(months)

def run_ses_alpha_0_9(series, months=24):
    """SES with Alpha = 0.9 (Highly reactive to latest data)."""
    model = SimpleExpSmoothing(series).fit(smoothing_level=0.9, optimized=False)
    return model.forecast(months)
