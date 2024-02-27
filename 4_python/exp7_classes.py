class Student:
    def __init__(self):
        self.name = "abc"
        self.age =  33

    def display(self):
         print ("name of the student is ", s1.name)
         print("age of the student is: ", s1.age)

    def update(self,n,a):
        self.name=n
        self.age=a

s1=Student()
print(s1.name)
print(s1.age)
s1.display()
s2= Student()
s2.update("xyz", 50)
print(s2.name)
print(s2.age)
