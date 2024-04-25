#Write a program to print a number in reverse order. Also show if the number is palindrome.

while True:
    def is_palindrome(num):
        num_str = str(num)

        return num_str == num_str[::-1]

    num = int(input("Enter a numeber: "))
    num_str = str(num)
    print("Number in reverse order: ", num_str[::-1])

    if is_palindrome(num):
        print(f"{num} is palindrome")
    else:
        print(f"{num} is not palindrome")
