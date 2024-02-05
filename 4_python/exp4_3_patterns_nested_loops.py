#nested for loops are used to print the pattern where only even numbers are printed and odd numbers are represented by ‘#’
for i in range(1,7):
    for j in range(1,i+1):
        if j%2==0:
            print(j, end="")
        else:
            print("#", end="")
    print()

#nested for loops and nested while loops are used to print the patterns
for i in range(1,6,2):
    for j in range(1,3):
        while(i!=0):
            print(i, end="")
            i -=1      
    print()
