
import pandas as pd

def linear_fit (data_ar):
    import statsmodels.api as sm
    import pandas as pd
    ndt = data_ar
    X = pd.Series(range(1, len(ndt) + 1))
    y = ndt
    # ordinary least squares
    fit = sm.OLS(y,sm.add_constant(X)).fit()
    return {'params': fit.params.values, 'fit_values': fit.fittedvalues.values}
# linear_fit ([1,2,2,4,4,5])['params']
# linear_fit ([1,2,2,4,4,5])['fit_values']


# moving average fit
def mov_avg_fit (data_ar, period):
    X = data_ar
    return pd.rolling_mean(X, period)
# mov_avg_fit (['1,2,3,4,5'], 2)

# moving average fit
def boxplot_values (data_df):
    x =  data_df
    return [
         x.min().values[0]
         ,x.quantile(.25).values[0]
        ,x.median().values[0]
        ,x.quantile(.75).values[0]
        ,x.max().values[0]
        ]

#print boxplot_values([377,571,248,573,341,314,1007,398,158,192,405,404,286,176,167,900])
