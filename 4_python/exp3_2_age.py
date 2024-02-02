name = input("Enter your name: ")
age = int(input("Enter your age: "))
experience = int(input("Enter number of years of experience: "))

if (age>18) and (experience>5):
    print("{} is eligible for the job.".format(name))
else:
    print("{} is not eligible for the job.".format(name))
                 
