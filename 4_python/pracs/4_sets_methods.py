#Write a Python program to demonstrate any 10 methods of Sets.

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
print ("set 1: ", set1)
print("set 2: ", set2)

set1.add(60)
print("\n\n1. Set after adding: ", set1)

set1.remove(20)
print("\n\n2. set after removing: ", set2)

print("\n\n3. Union: ", set1.union(set2))

print("\n\n4. Intersection: ", set1.intersection(set2))

print("\n\n5. Difference: ", set1.difference(set2))

print("\n\n6. is set1 subset of set2: ", set1.issubset(set2))

copied = set1.copy()
print("\n\n7. copied set: ", copied)

print("\n\n8. Length of set 1: ", len(set1))

print("\n\n9. Popped element from set 2: ", set2.pop())

set1.update([80, 100, 90])
print("\n\n10. updated set 1: ", set1)

print("\n\n11. set 2 after clearing: ", set2.clear())
