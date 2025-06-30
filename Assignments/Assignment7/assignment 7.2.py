import pandas as pd

dates = pd.date_range(start='2025-06-01', periods=5, freq='D')
df = pd.DataFrame({'date': dates})

df['year'] = df['date'].dt.year
df['month'] = df['date'].dt.month
df['day'] = df['date'].dt.day
df['weekday'] = df['date'].dt.day_name()
df['is_month_end'] = df['date'].dt.is_month_end
df['quarter'] = df['date'].dt.quarter

print(df)
