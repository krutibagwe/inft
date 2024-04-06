import pandas as pd
import xlrd

df = pd.read_excel("C:\\Users\\Student\\Downloads\\employees_new.xlsx")

print(df)
#print(df.columns)
'''
max_sal = (df["Salary"].max())
print("\nMax sal is: ",  max_sal)

min_bon = (df["Bonus %"].min())
print("\nMin bonus is: ", min_bon)

print()
print(df["Bonus %"])

print()
print(df[["Salary", "Team"]])

#salary more than 
print()
print(df[df.Salary >= 101004 ])
'''
print(df.head(5)) #to get first 5 rows
print(df.tail()) #to get last 5 rows
print(df.describe()) # to get statistical description of dataset
print(df.shape) # to get dimensions of dataset, no of rows and columns

#to find unique values of team column
print(df["Team"].value_counts())
print(df.Gender.value_counts().sum())

#to check missing values
print(df.isnull())
print(df.isnull().sum())

#slicing columns and rows
print(df.iloc[:,1:3])

#print(df.loc[:,"Gender", "Salary"])


import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import math
