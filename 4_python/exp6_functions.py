def area(side):
    return(side*side)
print("area of a square: ", area(15))

#function to find average of a dictionary
def mean(my_dict):
    my_mean=sum(my_dict.values())/len(my_dict)
    return(my_mean)

avg = mean({"1":12, "2":13, "3":14})
print(avg +10)

#function to find sum of a set
def my_sum(my_set):
    total = sum(my_set)
    return total
avg = my_sum({1,2,3,4,5})
print(avg)

#implicit return statement
def display(str):
    print("the string is ", str)
print(display("Hello"))

#keyword argument
def display(str, int_x, float_y):
    print("The string is ", str)
    print("The integer is ", int_x)
    print("The floating value is ", float_y)
display(str="Hello", int_x=10, float_y=12.3)

num = 12
fl = 12.34
str1 = "Hi"

display(int_x=num, float_y=fl, str= str1)

#functions with default arguments
#first two are positional arguments, third is keyword argument


def display(int_x, float_y, str="hello"):
    print("The string is ", str)
    print("The integer is ", int_x)
    print("The floating value is ", float_y)

#display(str="hi", int_x=10, float_y=12.3)
#display(int_x=10, float_y=12.3)
#display(float_y, int_x, str) 
#display(float_y=12.3, int_x=10)
#display(float_y=12.3, int_x=10, str)

    
#variable length arguments when total number of arguments is not known
def display(int_x, *float_values):
    type(float_values)
    print(int_x)
    for values in float_values:
        print(values)
#display(10,12)
display(10,12,2,3,4,5,6)


num1=10
def add (int_x, int_y):
    global num3
    num3=20
    print(num3)
    print(num1)
    return int_x+int_y
#print(add(10,12))

print(add(10,12))
print(num3)
print(num1)

#lambda function
sum=lambda x,y : x+y
print("Sum = ", sum(3,5))

#lambda function to change the string to uppercase
upp= lambda x: x.upper()
n = "hello"
print(upp(n))

#lambda fucntion to find cuberoot 
import math
cuberoot =  lambda x: pow (x, 1/3)
print (cuberoot(27))


def linearSearch(array,key):
    for i in range(len(array)):
        if array[i]==key:
            print(i)
    return -1
lst=[]
length = int(input("enter the number of elements in the list: "))

for i in range(length):
    elem= int(input(f"enter element {i+1}: "))
    lst.append(elem)

key = int(input("enter the number to be searched: "))
result = linearSearch(lst,key)
