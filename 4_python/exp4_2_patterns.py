#loops are used to print star patterns. The symbol * as a string is multiplied by a integer to print the pattern
for i in range(1,6):
    print('*' * i)

i=1
while i<6:
    print('*' * i)
    i+=1 

==================== RESTART: C:/Users/SQL/Desktop/exp4_1.py ===================
*
**
***
****
*****
>>>

#loops are used to print the above star pattern in reverse. The value of i was decremented after each iteration
num = int(input("Enter the number: "))
i = num
while i >0:
    print('*' *i) 
    i -= 1

i=5
while i>0:
    print('*' *i)
    i-=1
