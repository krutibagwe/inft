#Write a program to calculate factorial of a given number using a for loop.

while True:
    num = int(input("Enter the number: "))

    if num<0:
        print("Enter positive number!")

    else:
        factorial = 1

        for i in range(1, num+1):
            factorial *= i

        print(f"Factorial of {num}: {factorial}")

