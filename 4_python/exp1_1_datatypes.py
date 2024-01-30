Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a=12
a
12
type(a)
<class 'int'>
b=0.36
type(b)
<class 'float'>
>>> a="hello"
>>> type(a)
<class 'str'>
>>> x=2j
>>> type(x)
<class 'complex'>
>>> a=["red", "green", "blue"]
>>> type(a)
<class 'list'>
>>> b=("red", "green", "blue")
>>> type(b)
<class 'tuple'>
>>> x={"red", "green", "blue"}
>>> type(x)
<class 'set'>
>>> x={"name": "John", "age": 65}
>>> type(x)
<class 'dict'>
>>> x= range(5)
>>> type(x)
<class 'range'>
>>> x,y,z=10,20,30
>>> x+z
40
>>> x=frozenset({"red", "green", "blue"})
>>> type(x)
<class 'frozenset'>
>>> x=memoryview(bytes(4))
>>> x
<memory at 0x000001E001898640>
>>> x=b"hello
SyntaxError: unterminated string literal (detected at line 1)
>>> type(x)
<class 'memoryview'>
>>> x=b"hello"
>>> type(x)
<class 'bytes'>
>>> import random
>>> print(random.randrange(1,10))
3
