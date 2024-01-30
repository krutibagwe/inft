Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> list1=["green", "red", "blue"]
>>> print(list1)
['green', 'red', 'blue']
>>> list1.append("yellow")
>>> print(list1)
['green', 'red', 'blue', 'yellow']
>>> list2= list1.copy()
>>> print(list2)
['green', 'red', 'blue', 'yellow']
>>> list1.append("blue")
>>> list1.count("blue")
2
>>> list3=["monday", "tuesday", "friday"]
>>> list1.extend(list3)
>>> print(list1)
['green', 'red', 'blue', 'yellow', 'blue', 'monday', 'tuesday', 'friday']
>>> list1.index("monday")
5
>>> list1.insert(5, "black")
>>> print(list1)
['green', 'red', 'blue', 'yellow', 'blue', 'black', 'monday', 'tuesday', 'friday']
>>> list1.pop(4)
'blue'
>>> print(list1)
['green', 'red', 'blue', 'yellow', 'black', 'monday', 'tuesday', 'friday']
>>> list1.remove("black")
>>> print(list1)
['green', 'red', 'blue', 'yellow', 'monday', 'tuesday', 'friday']
>>> list1.reverse()
>>> print(list1)
['friday', 'tuesday', 'monday', 'yellow', 'blue', 'red', 'green']
>>> list1.sort()
>>> print(list1)
['blue', 'friday', 'green', 'monday', 'red', 'tuesday', 'yellow']
>>> print(len(list1))
7
print(list1[3:6])
['monday', 'red', 'tuesday']
print(list1[-2])
tuesday
list1[0]= "orange"
print(list1)
['orange', 'friday', 'green', 'monday', 'red', 'tuesday', 'yellow']
