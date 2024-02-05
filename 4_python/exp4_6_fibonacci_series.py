#while loop is used to print Fibonacci series of a number given by user 
num = int(input("enter the number: "))
a=0
b=1
c=b
count=1
print(“The Fibonacci series for {} numbers is: “.format(num))
while count<=num:
    print(c, end=" ")
    count+=1
    a=b
    b=c
    c=a+b
print()
