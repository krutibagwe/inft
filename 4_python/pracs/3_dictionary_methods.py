#Write a Python program to demonstrate any 10 methods of Dictionary.

dict1 = {
    'name': 'John',
    'age': 30,
    'city': 'New York',
    'email': 'john@example.com'
}

print("1. keys of dictionary: ", dict1.keys())

print("\n\n2. values of dictionary: ", dict1.values())

print("\n\n3. items of dictionary: ", dict1.items())

print("\n\n4. value of AGE key: ", dict1.get('age'))

dict1.setdefault('gender', 'male')
print("\n\n5. dictionary after default: ", dict1)

#print("\n\n6. Removed value: ", dict1.pop('email'))
print("dictionary after removing EMAIL key: ", dict1)

print("\n\n7. Removed value: ", dict1.pop('email'))
print("dictionary after removing key-value: ", dict1)

copied = dict1.copy()
print("\n\n8. Copied dictionary: ", copied)

print("\n\n9. cleared dictionary: ", dict1.clear())

print("\n\n")
dict3 = {'a': 1, 'b': 2}
dict4 = {'c': 3, 'd': 4}
print(dict3)
print(dict4)
dict3.update(dict4)
print("\n\n10. updated dict 3:", dict3)
