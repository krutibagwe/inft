num = 5
for i in range(1, num+1):
    for j in range(0, i*2, 2):
        print(chr(ord('A')+j), end=" ")
    print()
