m1= int(input("enter marks of subject 1: "))
m2= int(input("enter marks of subject 2: "))
m3= int(input("enter marks of subject 3: "))

av = (m1+m2+m3)/3

if av>50:
    print("Passed")
    print("Average marks are {}.".format(av))
else:
    print("Not Passed")
