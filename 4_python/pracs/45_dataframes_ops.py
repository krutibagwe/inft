#Write a Python program to implement any 5 operations on Data Frame.

import pandas as pd

#dataframe from dictionary of lists
data = { 'Name': ['Alice', 'Bob', 'Charlie', 'David'],
         'Age': [28, 54, 34, 24],
         'City': ['NY', 'LA', 'Paris', 'Hong Kong']}
df = pd.DataFrame(data)

print("Original DataFrame: ")
print(df)

print("\n1.Accessing a column: ")
print(df['Name'])

print("\n2.Accessing a row: ")
print(df.loc[0])

df['Gender'] = ['Female','Male','Male','Male']
print("\n3.Adding new column: ")
print(df)

print("\n4.Filtering rows based on age (age>30): ")
print(df[df['Age']>30])

print("\n5.Sorting by age COLUMN: ")
print(df.sort_values(by='Age'))

df.rename(columns={'City': 'Location'}, inplace=True)
print("\n6.Renaming columns: ")
print(df)
