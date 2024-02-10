import array
import array as arr
a = arr.array('i', [1,2,3])
a[0]
1
a[1]
2
a= arr.array('d'[2.5,3.6,4.8])
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    a= arr.array('d'[2.5,3.6,4.8])
TypeError: string indices must be integers, not 'tuple'
a= arr.array('d',[2.5,3.6,4.8])
a.typecode
'd'
for i in range(0,3):
    print (a[i])

    
2.5
3.6
4.8
a.itemsize
8
a.insert(5,6,7)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    a.insert(5,6,7)
TypeError: insert expected 2 arguments, got 3
a.insert(2,6.3)
a
array('d', [2.5, 3.6, 6.3, 4.8])
a.pop
<built-in method pop of array.array object at 0x00000204873F4220>
a.pop()
4.8
a
array('d', [2.5, 3.6, 6.3])
a.pop(2)
6.3
a
array('d', [2.5, 3.6])
a.remove(2.5)
a
array('d', [3.6])
a.index(3.6)
0
a1 = arr.array('d', [1.0,2.0,3.0,4.0])
a2 = a1*3
a2
array('d', [1.0, 2.0, 3.0, 4.0, 1.0, 2.0, 3.0, 4.0, 1.0, 2.0, 3.0, 4.0])
a2[2:5]
array('d', [3.0, 4.0, 1.0])
a[4:]
array('d')
>>> a2[4:]
array('d', [1.0, 2.0, 3.0, 4.0, 1.0, 2.0, 3.0, 4.0])
>>> a2[:5]
array('d', [1.0, 2.0, 3.0, 4.0, 1.0])
>>> a2[::-1]
array('d', [4.0, 3.0, 2.0, 1.0, 4.0, 3.0, 2.0, 1.0, 4.0, 3.0, 2.0, 1.0])
>>> a2[:-4,-1]
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    a2[:-4,-1]
TypeError: array indices must be integers
>>> a2[:-3:-1]
array('d', [4.0, 3.0])
>>> a1.append(5.0)
>>> a
array('d', [3.6])
>>> a1
array('d', [1.0, 2.0, 3.0, 4.0, 5.0])
>>> a1.append(6.0,7.0)
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    a1.append(6.0,7.0)
TypeError: array.append() takes exactly one argument (2 given)
>>> a1.reverse()
>>> a1
array('d', [5.0, 4.0, 3.0, 2.0, 1.0])
>>> a1.buffer_info()
(2218434125552, 5)
>>> a1.byteswap()
>>> a1
array('d', [2.561e-320, 2.0553e-320, 1.0435e-320, 3.16e-322, 3.03865e-319])
>>> a2.count(4.0)
3
>>> a1.extend(a2)
>>> a1
array('d', [2.561e-320, 2.0553e-320, 1.0435e-320, 3.16e-322, 3.03865e-319, 1.0, 2.0, 3.0, 4.0, 1.0, 2.0, 3.0, 4.0, 1.0, 2.0, 3.0, 4.0])
>>> del a2
