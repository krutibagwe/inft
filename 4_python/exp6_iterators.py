'''l1 = [1,2,3,4,5]
for i in l1:
    print (i) 

list2 = ['alice', 'bob', 'charlie']
for i in list2:
    print (i)

list2 = ['alice', 'bob', 'charlie']
iter_lst1 = iter(list2)
print(next(iter_lst1))
print(next(iter_lst1))
print(next(iter_lst1))
print(next(iter_lst1))
#to handle the exception, stop iteration 

list2 = ['alice', 'bob', 'charlie']
iter_lst1 = iter(list2)
while True:
    try:
        print(next(iter_lst1))
    except StopIteration:
        print("No more elements in the list!")
        break    
   

# A generator function that yields 1 for first time, 
# 2 second time and 3 third time 
def simpleGeneratorFun(): 
	yield 1			
	yield 2			
	yield 3			

# Driver code to check above generator function 
for value in simpleGeneratorFun(): 
	print(value)
	
# A Python program to demonstrate use of 
# generator object with next() 
# A generator function 
def simpleGeneratorFun(): 
	yield 1
	yield 2
	yield 3

# x is a generator object 
x = simpleGeneratorFun() 

# Iterating over the generator object using next 
# In Python 3, __next__() 
print(next(x)) 
print(next(x)) 
print(next(x))

# A simple generator for Fibonacci Numbers 
def fib(limit): 
	
	# Initialize first two Fibonacci Numbers 
	a, b = 0, 1

	# One by one yield next Fibonacci Number 
	while a < limit: 
		yield a 
		a, b = b, a + b 

# Create a generator object 
x = fib(5) 

# Iterating over the generator object using next 
# In Python 3, __next__() 
print(next(x)) 
print(next(x)) 
print(next(x)) 
print(next(x)) 
print(next(x)) 

# Iterating over the generator object using for 
# in loop. 
print("\nUsing for in loop")
# create the generator object
squares_generator = (i * i for i in range(5))

# iterate over the generator and print the values
for i in squares_generator:
    print(i) 

def infinite():
    n = 0
    while True:
        yield n
        n += 1
        
for i in infinite():
    if i%4 == 0:
        continue
    elif i == 13:
        break
    else:
        print(i)


def naturalno(limit): 
	
	# Initialize first two Fibonacci Numbers 
	a= 1

	# One by one yield next Fibonacci Number 
	while a < limit: 
		yield a 
		a = a+1

# Create a generator object 
x = naturalno(10)
for i in x:
    print(i)
'''












	


	
