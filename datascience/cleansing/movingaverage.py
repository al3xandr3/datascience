
import pandas as pd

# moving average fit
def mov_avg_fit (data_ar, period):
    X = data_ar
    return pd.rolling_mean(X, period)
# mov_avg_fit (['1,2,3,4,5'], 2)

