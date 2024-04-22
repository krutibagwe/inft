#Write a program to find the sum of natural numbers up to n, where n is provided by the user.

while True:
    n = int(input("enter the value of n: "))
    nos = []

    for i in range(1,n+1):
        nos.append(i)

    res = sum(nos)
    print(f"Sum of {n} natural numbers is {res}.")
