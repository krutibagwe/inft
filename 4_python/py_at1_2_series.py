def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        result = 1
        for i in range(2, num + 1):
            result *= i
        return result

def series_sum(n):
    sum_series = 0
    for i in range(n + 1):
        term = 1 / factorial(i)
        sum_series += term
    return sum_series

while True:
    try:
        n = int(input("Enter a positive integer n: "))
        if n < 0:
            print("Please enter a positive integer.")
        else:
            break
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

result_sum = series_sum(n)

print("Series S = 1 + 1/1! + 1/2! + 1/3! ...... 1/n!")
print(f"The sum of the series S for n = {n} is: {result_sum}")
