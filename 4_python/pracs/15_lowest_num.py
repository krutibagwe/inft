# Write a program to find the lowest number out of the three numbers

while True:
    num1 = float(input("Enter number 1: "))
    num2 = float(input("Enter number 2: "))
    num3 = float(input("Enter number 3: "))

    if num1 <= num2 and num1 <= num3:
        lowest = num1
    elif num2 <= num1 and num2 <= num3:
        lowest = num2
    else:
        lowest = num3

    print(f"The lowest number among {num1}, {num2}, {num3} is {lowest}")
