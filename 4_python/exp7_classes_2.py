#class variable 
class Sample:
    x=10

    @classmethod
    def modify(cls):
        cls.x = cls.x + 1

s1 = Sample()
s2 = Sample()

print(s1.x)
print(s2.x)

s1.modify()
print(s1.x)
print(s2.x)

#demonstration of class and static variable
class Myclass:
    #class variable or static variable
    n=0

    #constructor that increments n when an instance is created
    def __init__(self):
        Myclass.n =  Myclass.n + 1

    #static method to display no of occurences
    @staticmethod
    def NoOfObjects():
        print("No. of instances created", Myclass.n)

obj1 = Myclass()
obj2 = Myclass()
obj3 = Myclass()
Myclass.NoOfObjects()

#demonstration of __ class
class Person:
    def __init__(self):
        self.name = "kruti"
        self.age = 19
        self.date = 21
        self.month = 5
        self.year = 2004

    def display(self):
        print("{} is {} years old. The Date of Birth is {}/{}/{}".format(self.name, self.age, self.date, self.month, self.year))

p1 = Person()
p1.display()

class Person:
    def __init__(self, n, a, d, m, y):
        self.name = n
        self.age = a
        self.date = d
        self.month = m
        self.year = y

    def display(self):
        print("{} is {} years old. The Date of Birth is {}/{}/{}".format(self.name, self.age, self.date, self.month, self.year))

p1 = Person("abc", 30, 15, 8, 2020)
p1.display()
p2 = Person("xyz", 6, 27, 2, 2024)
p2.display()

#demonstration of inner class
class Person:
    def __init__(self):
        self.name = "kruti"

    def display(self):
        print(self.name)

    class Dob:
        def __init__(self):
            self.dd = 21
            self.mm = 5
            self.yy = 2004

        def display(self):
            print("Date of Birth is {}/{}/{}".format(self.dd, self.mm, self.yy))
p1 = Person()
p1.display()

#create inner class object
x1 = Person().Dob()
x1.display()

























    
