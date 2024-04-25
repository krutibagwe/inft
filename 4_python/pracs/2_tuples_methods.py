# Write a Python program to demonstrate working on tuples and any methods of Tuple.

tuple1 = (10, 20, 30, 40, 20, 50)

#method 1: accessing elements
print("1. Tuple elements: ")
for element in tuple1:
    print(element, end = " ")

#method 2: length of tuple
print("\n\n2. Length of tuple: ", len(tuple1))


#method 3: indexing and slicing
print("\n\n3. Indexing and slicing: ")
print("First element: ", tuple1[0])
print("Last element: ", tuple1[-1])
print("Slicing from index 1 to 4: ", tuple1[1:4])

#method 4: concatenating tuples
tuple2 = (1,2,3)
tuple3 = ('a', 'b', 'c')
concatenated_tuple = tuple2 + tuple3
print("\n\n4. Concatenated Tuple: ", concatenated_tuple)

#method 5: element count
print("\n\n5. Count of 20: ", tuple1.count(20))

#method 6: find index of element
print("\n\n6. Index of 40: ", tuple1.index(40))

#method 7: reverse a tuple
print("\n\n7. Reversed tuple: ", tuple1[::-1])

#method 8: sorting tuple using sorted()
print("\n\n8. Sorted tuple: ", tuple(sorted(tuple1)))

#method 9: min and max
print("\n\n9. Min element: ", min(tuple1))
print("Max element: ", max(tuple1))

#method 10
print("\n\n10. Sum of tuple elements: ", sum(tuple1))

#method 11: checking for unique elements USE SET()
print("\n\n11. Unique elements: ", set(tuple1))
      
