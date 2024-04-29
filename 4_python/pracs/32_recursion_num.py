#Write a Python program to calculate sum of first 5 natural numbers/factorial/ gcd-lcm/ n raise to x using recursion

def sum_of_natural_numbers(n):
    # Base case: If n is 0, return 0
    if n == 0:
        return 0
    # Recursive case: Sum of first n natural numbers = n + sum of first (n-1) natural numbers
    return n + sum_of_natural_numbers(n - 1)

def factorial(n):
    # Base case: 0! = 1
    if n == 0:
        return 1
    # Recursive case: n! = n * (n-1)!
    return n * factorial(n - 1)

def gcd(a, b):
    # Base case: GCD(a, 0) = a
    if b == 0:
        return a
    # Recursive case: GCD(a, b) = GCD(b, a % b)
    return gcd(b, a % b)

#lcm without recursion
def lcm(a, b):
    greater = max(a, b)
    smallest = min(a, b)
    for i in range(greater, a*b+1, greater):
        if i % smallest == 0:
            return i

def lcm2(a, b):
    return abs(a * b) // gcd(a, b)

def power_of_n(base, exponent):
    # Base case: x^0 = 1
    if exponent == 0:
        return 1
    # Recursive case: x^n = x * x^(n-1)
    return base * power_of_n(base, exponent - 1)

# Get user input for the operations
n = int(input("Enter a number to calculate the sum of first n natural numbers: "))
factorial_num = int(input("Enter a number to calculate its factorial: "))
num1 = int(input("Enter the first number to calculate GCD and LCM: "))
num2 = int(input("Enter the second number to calculate GCD and LCM: "))
base = int(input("Enter the base number for exponentiation: "))
exponent = int(input("Enter the exponent for exponentiation: "))

# Calculate and display the results using recursion
print("Sum of first", n, "natural numbers:", sum_of_natural_numbers(n))
print("Factorial of", factorial_num, ":", factorial(factorial_num))
print("GCD of", num1, "and", num2, ":", gcd(num1, num2))
print("LCM of", num1, "and", num2, ":", lcm(num1, num2))
print(base, "raised to the power of", exponent, ":", power_of_n(base, exponent))
print("LCM of", num1, "and", num2, ":", lcm2(num1, num2))
