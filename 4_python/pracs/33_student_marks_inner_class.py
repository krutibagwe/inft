#Declare a Class with class-name Student which accepts the Student details, creates an inner class of Student Marks with a constructor that takes marks as arguments and returns the total and percentage of marks along with the student details

class Student:
    def __init__(self):
        self.name = input("Enter student name: ")
        self.id = input("Enter student ID: ")

    def display(self):
        print(f"Name of student: {self.name} \nStudent ID: {self.id}")

    class Marks:
        def __init__(self):
            self.m1 = float(input("Enter marks of subject 1 (out of 100): "))
            self.m2 = float(input("Enter marks of subject 2 (out of 100): "))
            self.m3 = float(input("Enter marks of subject 3 (out of 100): "))

        def display(self):
            print(f"Total marks (out of 300): {self.m1 + self.m2 + self.m3}")
            print(f"Percentage: {(self.m1 + self.m2 + self.m3)/3}%.")

s1 = Student()
x1 = s1.Marks()
s1.display()
x1.display()
