#Write a Python program to demonstrate any 10 inbuilt Math methods.

import math

#1 square root
num1 = 12
square_root =  math.sqrt(num1)
print("Square root")
print (f"number: {num1} square root: {square_root} \n")

#2 power (x raised to y)
base = 2
exponent = 3
power_res = math.pow(base, exponent)
print("Power (x raised to y)")
print(f"base: {base} exponent: {exponent} result: {power_res}\n")

#3 factorial
num2 = 6
factorial_res = math.factorial(num2)
print("Factorial")
print(f"number: {num2} factorial: {factorial_res}\n")

#4 CEIL smallest integer greater than or equal
num4 = 3.7
print(num4)
print("Ceil")
print(math.ceil(num4), "\n")

#5 FLOOR largest integer less than or equal
print(num4)
print("Floor")
print(math.floor(num4), "\n")

#6 fabs: absolute value
num5 = -10
print("fabs: absolute value")
print(num5)
print(math.fabs(num5), "\n")

#7 is square root: returns square root integer
num6 = 25
num7 = 12
print("Is Square Root")
print(num6, math.isqrt(num6))
print(num7, math.isqrt(num7), "\n")

#8 radians from degree
angle1 = 30
angradian= math.radians(angle1)
print("Radians from degree")
print(f"angle: {angle1}")
print(angradian, "\n")

#9 sine
print("Sine")
print(angradian)
print(math.sin(angradian), "\n")

#10 e raised to power x
x = 2
print("e raised to the power")
print(x)
print(math.exp(x))
