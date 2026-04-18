from statsmodels.tsa.holtwinters import SimpleExpSmoothing

def run_ses_forecast(series, months=24):
    model = SimpleExpSmoothing(series, initialization_method="estimated").fit()
    return model.forecast(months)

def run_moving_average(series, window=3, months=24):
    last_ma = series.tail(window).mean()
    return [last_ma] * months # Simple MA assumes a flat forecast
