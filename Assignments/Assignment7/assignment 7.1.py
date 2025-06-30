import pandas as pd

data = {
    'Email': ['user1@gmail.com', 'invalid-email', 'hello@domain.org'],
    'Mobile': ['9876543210', '12345', '9090909090'],
    'PAN': ['ABCDE1234F', 'abc123', 'XYPQR6789Z']
}

df = pd.DataFrame(data)
print(df)

df['Valid Email'] = df['Email'].str.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')

df['Valid Mobile'] = df['Mobile'].str.match(r'^[6-9]\d{9}$')

df['Valid PAN'] = df['PAN'].str.match(r'^[A-Z]{5}[0-9]{4}[A-Z]$')

print(df)
