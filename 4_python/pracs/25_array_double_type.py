#Write a Python program to create an array of double data type.
#a. Using this array, create another array whose elements are three times that of the elements of the first array.
#b. perform slicing and indexing of arrays.
#c. Demonstrate various methods of array class

import array as arr

initial_val = [1.0, 2.0, 3.0, 4.0, 5.0]
a1 = arr.array('d', initial_val)

tripled_val = [3*x for x in a1]
a2 = arr.array('d', tripled_val)

print(a1)
print(a2)

print("\n\n1. size of byte: ", a1.itemsize)

a1.insert(2,30) #index and value
print("\n\n2. after inserting: ", a1)

popped = a1.pop()
print("\n\n3. after popping last element: ", a1)
print("poppped elem: ", popped)
popped2 = a1.pop(2) #pop using index
print(a1, popped2)

a1.remove(1.0)
print("\n\n4. removing using elem 1.0: ", a1)

print("\n\n5. index of elem: ", a1.index(4.0))

a1.append(25.0)
print("\n\n6. appending elem: ", a1)

a1.reverse()
print("\n\n7. reverse array: ", a1)

a1.extend(a2)
print("\n\n8. extending a1: ", a1)

print("\n\n9. count of 15.0: ", a1.count(3.0))

#slicing
print("\n\nSLICING: \n")
print(a1)
print(a1[2:5])
print("starting 4: ", a1[4:])
print("last 3: ", a1[:3])
print("reverse: ", a1[::-1])
print(a1[:-3:-1])
