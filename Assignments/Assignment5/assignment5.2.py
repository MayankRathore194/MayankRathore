import pandas as pd
data = [[1, 'Akshat'], [2, 'Aman'], [3, 'Arvind']]
df_list = pd.DataFrame(data, columns=['ID', 'Name'])
print(df_list)


data = {'Name': ['Ram', 'Shyam'], 'Age': [25, 22]}
df_dict = pd.DataFrame(data)
print(df_dict)


data = [['Akshat', 24], ['Rahul', 27]]
df_lists = pd.DataFrame(data, columns=['Name', 'Age'])
print(df_lists)


data = [('Vishnu', 23), ('Ramesh', 21)]
df_tuples = pd.DataFrame(data, columns=['Name', 'Age'])
print(df_tuples)


data = [{'Name': 'Aman', 'Age': 24}, {'Name': 'Bob', 'Arvind': 27}]
df_dicts = pd.DataFrame(data)
print(df_dicts)
