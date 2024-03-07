#parent class
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

p = Person("John", "Doe")
p.printname()

#child class inherits from Parent class
class Student(Person):
    pass
s1 = Student("ABC", "def")
s1.printname()
