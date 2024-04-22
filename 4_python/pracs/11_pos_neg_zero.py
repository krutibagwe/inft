#Write a Python program using if elif else statement to demonstrate if number inputted by user is positive, negative or zero
while True:
    num = int(input("enter a number: "))

    if num>0:
        print(f"{num} is positive.")
    elif num<0:
        print(f"{num} is negative.")
    else:
        print(f"The number entered ({num}) is zero. ")
