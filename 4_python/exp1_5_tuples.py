Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> tuple1=("green", "blue", "red", "yellow")
>>> tuple1
('green', 'blue', 'red', 'yellow')
>>> print(len(tuple1))
4
>>> print(type(tuple1))
<class 'tuple'>
>>> print(tuple1[2])
red
>>> print(tuple1[-1])
yellow
>>> print(tuple1[1:3])
('blue', 'red')
>>> for x in tuple1:
...     print(x)
... 
...     
green
blue
red
yellow
>>> tuple2= (2,4,6,8)
>>> tuple3= tuple1 + tuple2
>>> tuple3
('green', 'blue', 'red', 'yellow', 2, 4, 6, 8)
>>> tuple4= tuple1 * 2
>>> tuple4
('green', 'blue', 'red', 'yellow', 'green', 'blue', 'red', 'yellow')
>>> y= tuple4.count("blue")
>>> y
2
>>> z= tuple2.index(6)
>>> z
2
>>> if "green" in tuple1:
...     print("yes")
... 
    
yes
