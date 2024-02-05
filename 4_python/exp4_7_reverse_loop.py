#loops are used to print the output in reverse order. The for loop uses a step of -1 instead of +1. In while loop, i is decremented by 1 instead of incremented by 1

num = int(input("Enter the number: "))
for i in range(num, -1, -1):
    print(i)

num = int(input("Enter the number: "))
i = num
while i >= 0:
    print(i)
    i -= 1
