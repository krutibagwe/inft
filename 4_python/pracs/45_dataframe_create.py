#Write a Python program to implement Data Frames and different techniques to create Data Frames.

import pandas as pd

data1 = {'Name': ['John', 'Anna', 'Peter', 'Linda'],
         'Age': [28, 35, 45, 30],
         'City': ['New York', 'Paris', 'London', 'Sydney']}
df1 = pd.DataFrame(data1)
print("DataFrame created from a dictionary of lists:")
print(df1)
print()

data2 = [{'Name': 'John', 'Age': 28, 'City': 'New York'},
         {'Name': 'Anna', 'Age': 35, 'City': 'Paris'},
         {'Name': 'Peter', 'Age': 45, 'City': 'London'},
         {'Name': 'Linda', 'Age': 30, 'City': 'Sydney'}]
df2 = pd.DataFrame(data2)
print("DataFrame created from a list of dictionaries:")
print(df2)
print()


data3 = [('John', 28, 'New York'),
         ('Anna', 35, 'Paris'),
         ('Peter', 45, 'London'),
         ('Linda', 30, 'Sydney')]
df3 = pd.DataFrame(data3, columns=['Name', 'Age', 'City'])
print("DataFrame created from a list of tuples:")
print(df3)
print()

import numpy as np

data4 = np.array([[1, 'John', 28],
                  [2, 'Anna', 35],
                  [3, 'Peter', 45],
                  [4, 'Linda', 30]])
df4 = pd.DataFrame(data4, columns=['ID', 'Name', 'Age'])
print("DataFrame created from a NumPy array:")
print(df4)
print()

df5 = pd.read_csv('filename.csv')
print("DataFrame from CSV file: ")
print(df5)
                   
