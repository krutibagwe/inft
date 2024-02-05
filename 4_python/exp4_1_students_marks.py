#for and while loops are used to input marks of 10 students and calculate & print average marks. If-else statement is used inside for/while loop to check if student has passed 
for i in range(1,11):
    print("Student {}:".format(i))
    m1= int(input("enter marks of 1st subject: "))
    m2= int(input("enter marks of 2nd subject: "))
    m3= int(input("enter marks of 3rd subject: "))
    
    total= m1+m2+m3
    print(total)
    avg= total/3
    print(avg)
    if avg>50:
        print("pass")
    else:
        print(“fail”)

i=1
while i<=10:
    print("Student {}:".format(i))
    m1= int(input("enter marks of 1st subject: "))
    m2= int(input("enter marks of 2nd subject: "))
    m3= int(input("enter marks of 3rd subject: "))
    
    total= m1+m2+m3
    print(total)
    avg= total/3
    print(avg)
    if avg>50:
        print("pass")
    else:
        print(“fail”)
    i+=1
