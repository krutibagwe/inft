Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> colours={"red", "green", "blue"}
>>> colours.add("yellow")
>>> colours
{'green', 'blue', 'red', 'yellow'}
>>> shapes= {"green", "circle", "square"}
>>> a=colours.difference(shapes)
>>> a
{'blue', 'red', 'yellow'}
>>> colours.discard("blue")
>>> colours
{'green', 'red', 'yellow'}
>>> colours.pop()
'green'
>>> colours
{'red', 'yellow'}
>>> colours.update(shapes)
>>> colours
{'circle', 'red', 'yellow', 'square', 'green'}
>>> x= {"circle", "green"}
>>> c=colours.issuperset(x)
>>> c
True
>>> colours.remove("green")
>>> colours
{'circle', 'red', 'yellow', 'square'}
>>> number={"one", "two", "three"}
>>> m= colours.intersection(number)
>>> m
set()
>>> print(m)
set()
>>> n= colours.union(number)
>>> n
{'two', 'one', 'circle', 'three', 'red', 'yellow', 'square'}
>>> col={"red", "black", "orange"}
>>> m= colours.intersection(col)
>>> m
{'red'}
n= colours.isdisjoint(col)
n
False
o= colours.symmetric_difference(col)
o
{'circle', 'yellow', 'square', 'orange', 'black'}
