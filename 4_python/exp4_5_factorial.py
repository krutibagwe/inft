#loops are used to calculate factorial of number given by the user. Range function is also used along with for loop
prod = 1
num = int(input("enter the number: "))
for i in range(1,num+1):
    prod *=i
print(“Factorial of {} is {}.”.format(num,prod))

prod = 1
num = int(input("Enter the number: "))
i = 1
while i <= num:
    prod *= i
    i += 1
print("Factorial of {} is {}.".format(num, prod))
