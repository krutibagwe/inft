Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> dict1={"name": "abc", "age": 62, "city": "mumbai"}
>>> dict1
{'name': 'abc', 'age': 62, 'city': 'mumbai'}
>>> print(len(dict1))
3
>>> x= dict1.copy()
>>> x
{'name': 'abc', 'age': 62, 'city': 'mumbai'}
>>> dict2= dict.fromkeys(dict1)
>>> dict2
{'name': None, 'age': None, 'city': None}
>>> dict1.get("age")
62
>>> dict1.items()
dict_items([('name', 'abc'), ('age', 62), ('city', 'mumbai')])
>>> dict1.keys()
dict_keys(['name', 'age', 'city'])
>>> dict1.values()
dict_values(['abc', 62, 'mumbai'])
>>> dict1.update({"age": 12})
>>> dict1
{'name': 'abc', 'age': 12, 'city': 'mumbai'}
>>> dict1.pop("age")
12
>>> dict1
{'name': 'abc', 'city': 'mumbai'}
>>> dict1["colour"]="blue"
>>> dict1
{'name': 'abc', 'city': 'mumbai', 'colour': 'blue'}
>>> dict1.popitem()
('colour', 'blue')
>>> dict1
{'name': 'abc', 'city': 'mumbai'}
