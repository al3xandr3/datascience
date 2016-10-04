
import pandas as pd


# TODO, Day Data missing and filling:

# range of dates we want
idx = pd.date_range(weight_raw['date'].iloc[0], datetime.datetime.today())

# make the timestamp as the index
weight_raw = weight_raw.set_index('date')

# reindex adding missing days
weight_augmented = weight_raw.reindex(idx)

# interpolate missing values
#  http://stackoverflow.com/questions/20240749/pandas-dataframe-interpolating-missing-days
weight_augmented.weight = weight_augmented.weight.interpolate(method='linear')