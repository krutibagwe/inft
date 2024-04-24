#Write a Python program to declare a base class College having two derived classes student and faculty and display their details.

class College:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def display(self):
        print(f"College name: {self.name}")
        print(f"Address: {self.address}")

class Student(College):
    def __init__(self, name, address, stuid, stuprog):
        super().__init__(name, address)
        self.stuid = stuid
        self.stuprog = stuprog

    def display(self):
        super().display()
        print(f"Student ID: {self.stuid}")
        print(f"Student Program: {self.stuprog}")

class Faculty(College):
    def __init__(self, name, address, factid, factdept):
        super().__init__(name, address)
        self.factid = factid
        self.factdept = factdept

        def display(self):
            print(f"College name: {self.name}")
            print(f"Address: {self.address}")

def create_student():
    name = input("Enter college name: ")
    address = input("Enter student's address: ")
    stuid = input("Enter student's ID: ")
    prog = input("Enter student's program: ")
    return Student(name, address, stuid, prog)

def create_faculty():
    name = input("Enter faculty's name: ")
    address = input("Enter faculty's address: ")
    factid = input("Enter faculty's ID: ")
    factdept = input("Enter faculty's department: ")
    return Faculty(name, address, factid, factdept)

print("Enter Student Details:")
student = create_student()
print("\nStudent Details:")
student.display()

print("\n")

print("Enter Faculty Details:")
faculty = create_faculty()
print("\nFaculty Details:")
faculty.display()
