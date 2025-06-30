import pandas as pd

df = pd.read_csv("customers-100.csv")

print(df)

df['Subscription Date'] = pd.to_datetime(df['Subscription Date'], format='%d-%m-%Y', errors='coerce')
df['Email Domain'] = df['Email'].str.split('@').str[1]
df.drop_duplicates(subset='Customer Id', inplace=True)

top_countries = df['Country'].value_counts().head()
monthly = df['Subscription Date'].dt.to_period('M').value_counts().sort_index()

print("Top 5 Countries by Customers:\n", top_countries)
print("\nMonthly Subscriptions:\n", monthly)
print("\nTop 5 Email Domains:\n", df['Email Domain'].value_counts().head())
