#Write a program to find the lowest number out of the three numbers

while True:
    nums = []

    for i in range(3):
        num = float(input(f"Enter number {i+1}: "))
        nums.append(num)

    res = min(nums)
    print(f"The lowest number among {nums} is {res}")
