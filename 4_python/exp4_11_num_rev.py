num = int (input("enter a number: "))

print("original number: {}".format(num))

rev = 0
while (num!=0):
    rem = num %10
    rev = rev * 10 + rem
    num //=10
print ("reversed number: {}".format(rev))
