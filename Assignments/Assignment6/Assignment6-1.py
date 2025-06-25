#How to convert a series of date-strings to a timeseries?
import pandas as pd
date_strings = ['2025-01-01', '2025-01-02', '2025-01-03']
dates = pd.to_datetime(date_strings)
data = [10, 20, 30]
ts = pd.Series(data, index=dates)
print(ts)