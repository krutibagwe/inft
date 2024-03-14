class Employee:
    n=0
    def __init__(self):
        self.empid = int(input("Enter Employee ID: "))
        self.name = input("Enter Employee name: ")
        self.department = input("Enter Employee Department: ")
        self.salary = float(input("Enter Salary: "))
        Employee.n += 1

    def display(self):
        print(f"Employee ID: {self.empid}")
        print(f"Employee Name: {self.name}")
        print(f"Employee Department: {self.department}")
        print(f"Employee Salary: {self.salary}")

    @staticmethod
    def empcount():
        print(f"Number of employees: {Employee.n}")

    def updatesalary(self, increase):
        self.salary += increase
        print(f"Salary after increment: {self.salary}")


class Manager(Employee):
    def __init__(self):
        print("\nManager Information:")
        super().__init__()
        super().display()


class Staff(Employee):
    def __init__(self):
        print("\nStaff Information:")
        super().__init__()
        super().display()


m1 = Manager()
s1 = Staff()
Employee.empcount()
