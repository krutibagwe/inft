#number is taken an input and loops are used to find the sum of all numbers up to number n
num= int(input("enter the number: "))
add=0
for i in range(1,num+1):
    add +=i
print(add)

num =int(input("enter the number:" ))
add=0
i=0
while i<=num:
    add +=i
    i+=1
print(add) 
