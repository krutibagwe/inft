num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
num3=int(input("Enter third number: "))


if num1 >= num2 and num1 >= num3:
    print("{} is the greatest.".format(num1))
elif num2 >= num1 and num2 >= num3:
    print("{} is the greatest.".format(num2))
else:
    print("{} is the greatest.".format(num3))
