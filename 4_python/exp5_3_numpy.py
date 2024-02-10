import numpy
import numpy as np
arr = np.array([1, 2, 3, 4, 5])
arr
array([1, 2, 3, 4, 5])
print(np.__version__)
1.26.3
arr = np.array(42)
arr
array(42)
arr= np.array([[1,2,3,],[4,5,6]])
arr
array([[1, 2, 3],
       [4, 5, 6]])
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
arr
array([[[1, 2, 3],
        [4, 5, 6]],

       [[1, 2, 3],
        [4, 5, 6]]])
arr.ndim
3
arr[0]
array([[1, 2, 3],
       [4, 5, 6]])
arr[0][0]
array([1, 2, 3])
arr[0][1]
array([4, 5, 6])
arr[0][0][0]
1
arr[0][0][1]
2
arr[0][0][2]
3
arr[0,0,1]
2
arr[1,1,1]
5
arr = np.array([[1,2,3,4,5],[6,7,8,9,10]])
arr.ndim
2
arr[1][2:]
array([ 8,  9, 10])
arr([0][2],[1][2])
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    arr([0][2],[1][2])
IndexError: list index out of range
arr([[0][2]],[[1][2]])
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    arr([[0][2]],[[1][2]])
IndexError: list index out of range
arr[0][2], arr [1][2]
(3, 8)
arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
newarr = arr.reshape(4,3)
newarr
array([[ 1,  2,  3],
       [ 4,  5,  6],
       [ 7,  8,  9],
       [10, 11, 12]])
newarr = arr.reshape(2,3,2)
newarr
array([[[ 1,  2],
        [ 3,  4],
        [ 5,  6]],

       [[ 7,  8],
        [ 9, 10],
        [11, 12]]])
newarr = newarr.reshape(-1)
newarr
array([ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12])
