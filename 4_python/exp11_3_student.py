class Student:
    def __init__(self, r, n, a):
        self.rollno = r
        self.name = n
        self.age = a

    def disp(self):
        print(f"Name: {self.name}\nRoll no: {self.rollno}\nAge: {self.age}")
