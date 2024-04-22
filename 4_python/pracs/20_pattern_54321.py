'''
print pattern
5 4 3 2 1
4 3 2 1
3 2 1
2 1
1
'''


rows = 5
for i in range(rows, 0, -1):    #outer loop
    for j in range(i, 0, -1):   #inner loop
        print(j, end=" ")
    print()
