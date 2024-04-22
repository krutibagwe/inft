#Write a Python program using if else statement to demonstrate use of all comparison and logical operators in conjunction with if statement

# Define variables for comparison
a = 10
b = 5
c = 10

# Comparison and Logical Operators with if statement
if a > b:
    print(f"{a} is greater than {b}")

if a < b:
    print(f"{a} is less than {b}")
else:
    print(f"{a} is not less than {b}")

if a >= c:
    print(f"{a} is greater than or equal to {c}")

if a <= c:
    print(f"{a} is less than or equal to {c}")

if a == c:
    print(f"{a} is equal to {c}")

if a != b:
    print(f"{a} is not equal to {b}")

# Logical operators with if statement
if a > b and a == c:
    print(f"{a} is greater than {b} AND equal to {c}")

if a > b or a < c:
    print(f"{a} is greater than {b} OR less than {c}")

if not (a < b):
    print(f"{a} is NOT less than {b}")

