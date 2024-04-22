#Write a Python program to demonstrate types of operators.

# Arithmetic operators
a = 10
b = 3

print("Addition:", a + b)       # Addition
print("Subtraction:", a - b)    # Subtraction
print("Multiplication:", a * b) # Multiplication
print("Division:", a / b)       # Division
print("Floor Division:", a // b) # Floor Division (integer division)
print("Modulus:", a % b)        # Modulus (remainder of division)
print("Exponentiation:", a ** b) # Exponentiation (a raised to the power of b)


# Assignment operators
x = 5  # Assigns 5 to variable x
x += 3 # Equivalent to: x = x + 3
x -= 1 # Equivalent to: x = x - 1
x *= 2 # Equivalent to: x = x * 2
x /= 4 # Equivalent to: x = x / 4
print("Updated value of x:", x)


# Comparison operators
x = 10
y = 5

print("x > y is", x > y)   # Greater than
print("x < y is", x < y)   # Less than
print("x == y is", x == y) # Equal to
print("x != y is", x != y) # Not equal to
print("x >= y is", x >= y) # Greater than or equal to
print("x <= y is", x <= y) # Less than or equal to


# Logical operators
p = True
q = False

print("p and q is", p and q) # Logical AND
print("p or q is", p or q)   # Logical OR
print("not p is", not p)     # Logical NOT



# Bitwise operators
a = 5   # 101 (in binary)
b = 3   # 011 (in binary)

print("Bitwise AND:", a & b)  # Bitwise AND
print("Bitwise OR:", a | b)   # Bitwise OR
print("Bitwise XOR:", a ^ b)  # Bitwise XOR
print("Bitwise NOT (a):", ~a) # Bitwise NOT
print("Left Shift (a << 1):", a << 1) # Left shift
print("Right Shift (a >> 1):", a >> 1) # Right shift



# Membership operators
string = "Hello, World!"
print("Substring 'Hello' in string?", 'Hello' in string)
print("Character 'z' not in string?", 'z' not in string)



# Identity operators
x = [1, 2, 3]
y = [1, 2, 3]
z = x

print("x is y?", x is y)     # False (different objects)
print("x is z?", x is z)     # True (same object)
print("x is not y?", x is not y) # True (different objects)
