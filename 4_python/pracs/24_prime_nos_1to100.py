#Write a python program to print prime numbers between 1 to 100

import math

# Function to check if a number is prime
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, math.isqrt(num) + 1):
        if num % i == 0:
            return False
    return True

# Print prime numbers between 1 to 100
print("Prime numbers between 1 and 100:")
for number in range(1, 101):
    if is_prime(number):
        print(number, end=" ")
