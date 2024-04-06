
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math

empdata = {"empid":[1001,1002,1003,1004,1005,1006],
           "ename":["Sonali","Rohan","Raj","Sweta","Mahit","Aakash"],
           "sal":[50000,30000,20000,40000,50000,56000],
           "doj":["13-06-1983","17-12-1976","07-02-2008","04-01-1991","09-03-2009","24-02-2009"]
            }

df = pd.DataFrame(empdata)
print(df)

#data visualisation
x = df["empid"]
y = df["sal"]
plt.bar(x,y, label = "Employee Data", color = "green")
plt.xlabel("Employee ID")
plt.ylabel("Salary")
plt.title("Employee Details")
plt.legend()
plt.show()

#histograms
empages = [22,45,30,59,58,56,57,45,43,43,50,40,34,33,25,19,55,47,62,33,38,24,29,32,50]
bins = [0,10,20,30,40,50,60]

plt.hist(empages, bins, histtype = "bar", rwidth=0.8, color = "cyan")
plt.grid(axis='y', alpha=0.75)
plt.xlabel("Employee ages")
plt.ylabel("Number of employees")
plt.title("Employee Details")
#plt.legend()
plt.show()

# create data
data = [32, 96, 45, 67, 76, 28, 79, 62, 43, 81, 70,
		61, 95, 44, 60, 69, 71, 23, 69, 54, 76, 67,
		82, 97, 26, 34, 18, 16, 59, 88, 29, 30, 66,
		23, 65, 72, 20, 78, 49, 73, 62, 87, 37, 68,
		81, 80, 77, 92, 81, 52, 43, 68, 71, 86]

# create histogram
plt.hist(data)

# display histogram
plt.show()

#pie chart
labels = 'Cricket', 'Hockey', 'Tennis', 'Football'
v = [40,20,90,80]
e = (0,0,0.1,0)
plt.pie(v, explode = e, labels = labels, autopct = '%1.3f%%', shadow = True, startangle = 90)
plt.show()

#scatter plot
x = np.linspace(0,10,50)
y = np.sin(x)
plt.scatter(x,y,marker="v")
plt.show()

#scatter plot
x = np.linspace(0,10,50)
y = np.sin(x)
plt.scatter(x,y,marker="*", alpha = 0.5, color = "green")
plt.show()

x = np.random.normal(5.0, 1.0, 1000)
y = np.random.normal(10.0, 2.0, 1000)
plt.scatter(x, y, color = "purple")
plt.show()
