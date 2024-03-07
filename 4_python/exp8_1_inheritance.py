#parent class
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

p = Person("John", "Doe")

#child class inherits from Parent class
class Student(Person):
    def __init__ (self, fname, lname, d):
        Person.__init__ (self, fname, lname)
        self.div = d
        print(self.div)

       
s1 = Student("ABC", "def", "A")
s1.printname()

