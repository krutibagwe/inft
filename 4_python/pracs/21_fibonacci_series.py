#Write a Python program to print Fibonacci series of 10 numbers using a while/for loop.

print("WHILE LOOP: ")
a,b = 0,1

print(a)
print(b)

count = 2

while count<10:
    nextnum = a+b
    print(nextnum)

    a = b
    b = nextnum

    count+=1


print("\nFOR LOOP: ")
a,b = 0,1

print(a)
print(b)

for i in range (2, 10):
    nextnum = a + b
    a = b
    b = nextnum
    print(nextnum)
