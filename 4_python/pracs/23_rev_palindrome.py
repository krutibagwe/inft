#Write a program to print a number in reverse order. Also show if the number is palindrome.
def is_palindrome(num):
    original_num = num
    reversed_num = 0

    while num > 0:
        remainder = num % 10
        reversed_num = (reversed_num * 10) + remainder
        num = num // 10

    return original_num == reversed_num

while True:
    num = int(input("Enter a number: "))
    reversed_num = 0
    original_num = num

    while num > 0:
        remainder = num % 10
        reversed_num = (reversed_num * 10) + remainder
        num = num // 10

    print("Number in reverse order:", reversed_num)

    if is_palindrome(original_num):
        print(f"{original_num} is a palindrome.")
    else:
        print(f"{original_num} is not a palindrome.")

