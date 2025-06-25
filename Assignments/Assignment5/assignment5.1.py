import pandas as pd

data = {'a': 10, 'b': 20, 'c': 30}
series_dict = pd.Series(data)
print(series_dict)



data = [10, 20, 30, 40]
series_list = pd.Series(data)
print(series_list)




print(series_dict['a'])       # by label
print(series_list[2])         # by index
