from functools import reduce
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Original numbers:", numbers)
print()
#reduce with a lambda function to find the sum of numbers
sum_result = reduce(lambda x, y: x + y, numbers)
print("Sum of numbers:", sum_result)

#filter with a lambda function to keep only even numbers
even_numbers = filter(lambda x: x % 2 == 0, numbers)
even_numbers_list = list (even_numbers)
print("Even numbers:", even_numbers_list)

#map with a lambda function to calculate square of a number
squared_numbers = map(lambda x: x**2, numbers)
squared_numbers_list = list(squared_numbers)
print("Squared numbers:", squared_numbers_list)
