from abc import ABC,abstractmethod

class College(ABC):
    @abstractmethod
    def performance(self):
        pass
        
    def details(self):
        self.name = input("enter the name: ")
        self.dept = input("enter the department: ")
        print()
        print(f"Name - {self.name}")
        print(f"Department - {self.dept}")
        print("College name - SFIT")

class Student(College):
    def performance(self):
        self.cgpa = input(f"enter CGPA: ")
        print(f"CGPA is {self.cgpa}")

class Teacher(College):
    def performance(self):
        self.exp= input(f"enter experience: ")
        print(f"Years of experience is {self.exp}")

s1=Student()
t1=Teacher()
print("For Student, ")
s1.performance()
s1.details()
print("\nFor Teacher, ")
t1.performance()
t1.details()


