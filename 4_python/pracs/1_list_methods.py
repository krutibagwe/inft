#Write a Python program to demonstrate any 10 methods of List.

fruits = ['cherry', 'apple', 'pineapple', 'banana']
print (fruits, "\n")

# 1. append
fruits.append('orange')
print("Append")
print(fruits, "\n")

#2. insert
fruits.insert(2, 'mango')
print("Insert")
print(fruits, "\n")

#3 pop
popped_fruit = fruits.pop(2)
print("Pop")
print(popped_fruit)
print(fruits, "\n")

#4 remove
fruits.remove('banana')
print("Remove")
print(fruits, "\n")

#5 index
index = fruits.index('apple')
print("Index")
print("apple: ", index)

#6 sort
fruits.sort()
print("Sort")
print(fruits, "\n")

#7 reverse
fruits.reverse()
print("Reverse")
print(fruits, "\n")

#8 count
nos = fruits.count('cherry')
print("Count")
print(nos, "\n")

#9 extend
more_fruits = ['guava', 'watermelon', 'grapes']
fruits.extend(more_fruits)
print("Extend")
print(more_fruits)
print(fruits, "\n")

#10 copy
fruits_copy = fruits.copy()
print("Copy")
print(fruits_copy, "\n")

#11 clear
fruits_copy.clear()
print("Clear")
print(fruits_copy)
