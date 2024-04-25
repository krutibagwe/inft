# To implement a python program to demonstrate anonymous functions (lambda,map,reduce,filter)

from functools import reduce

numbers = [1,2,3,4,5,6,7,8,9,10]
print("Original numbers: ", numbers)
print()

#reduce to find sum of numbers
sum_res = reduce(lambda x, y : x + y, numbers)
print("Sum of numbers: ", sum_res)

#filter to keep only even numbers
even_num = filter(lambda x: x % 2 == 0, numbers)
print("Even numbers: ", list(even_num))

#map to calculate square of numbers
squared_num = map(lambda x: x **2, numbers)
print("Squared numbers: ", list(squared_num))
