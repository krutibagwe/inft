#Write a Python program using if else statement to check if number inputted by user is even or odd
while True:
    num = int(input("enter a number:"))

    if num % 2 == 0:
        print(f"{num} is even.")
    else:
        print(f"{num} is odd.")
