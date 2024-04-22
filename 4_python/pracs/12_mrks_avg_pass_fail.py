#Write a Python program to read marks of 3 subjects of a student and check if the average marks are above 50 then print that student is passed in exam

while True:
    s1 = float(input("enter the marks of first subject (out of 100): "))
    s2 = float(input("enter the marks of second subject (out of 100): "))
    s3 = float(input("enter the marks of third subject (out of 100): "))

    total=s1+s2+s3
    avg = total/3

    if avg>=50:
        print(f"Average marks are {avg}.\nPASS!")
    else:
        print(f"Average marks are {avg}.\nFAIL!")

