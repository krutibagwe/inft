def sum1(n):
    if n == 1:
        return 1
    else:
        return n + sum1(n - 1)
result = sum1(5)
print(f"Sum of first 5 natural numbers: {result}")
