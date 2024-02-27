class Student:
    def __init__(self):
        self.name = input("enter student's name: ")
        self.id = input("enter student ID: ")
    def display(self):
        print("Name of student: {}\nStudent ID: {}".format(self.name, self.id))

    class Marks:
        def __init__(self):
            self.m1 = int(input("enter marks of subject 1 out of 100: "))
            self.m2 = int(input("enter marks of subject 2 out of 100: "))
            self.m3 = int(input("enter marks of subject 3 out of 100: "))

        def display(self):
            print(f"Total marks out of 300: {self.m1 + self.m2 + self.m3}\nPercentage: {(self.m1 + self.m2 + self.m3)/3}%.")

s1 = Student()
x1 = s1.Marks()
s1.display()
x1.display()

