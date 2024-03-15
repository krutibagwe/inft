#pip install multipledispatch
from multipledispatch import dispatch

# passing one parameter
@dispatch(int)
def sum(first):
    print(first+0)

# passing two parameters
@dispatch(int,int)
def sum(first, second):
    result = first+second
    print(result)

@dispatch(int, int, int)
def sum(first, second, third):
    result = first + second + third
    print(result)
    
@dispatch(float, float, float)
def sum(first, second, third):
    result = first + second + third
    print(result)
