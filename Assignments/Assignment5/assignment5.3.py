import pandas as pd

data = {'Name': ['Ram', 'Shyam'], 'Age': [25, 22]}
df_dict = pd.DataFrame(data)
print(df_dict)



# using iterrows
for index, row in df_dict.iterrows():
    print(row['Name'], row['Age'])

# using itertuples
for row in df_dict.itertuples():
    print(row.Name, row.Age)




print(df_dict[df_dict['Age'] > 23])


print(df_dict.iloc[1])   # Second row


print(df_dict[['Name']].head(2))


df_dropped = df_dict[df_dict['Age'] > 23]
print(df_dropped)



new_row = pd.DataFrame([{'Name': 'Spike', 'Age': 30}])
df_inserted = pd.concat([df_dict.iloc[:1], new_row, df_dict.iloc[1:]]).reset_index(drop=True)
print(df_inserted)


list_from_rows = df_dict.values.tolist()
print(list_from_rows)
