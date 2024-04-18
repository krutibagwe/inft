def is_prime(number):
    if number <= 1:
        return False
    
    for i in range(2, number):
        if number % i == 0:
            return False
    
    return True

num = int(input("Enter a positive integer to check if it's prime: "))

# Check if the number is prime
if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")
