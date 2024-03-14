class Employee:
    n = 0

    def __init__(self):
        self.empid = int(input("Enter Employee ID: "))
        self.name = input("Enter Employee name: ")
        self.department = input("Enter Employee Department: ")
        self.salary = float(input("Enter Salary: "))
        self.increase = int(input("Enter increase in salary: "))
        Employee.n += 1

    def display(self):
        print(f"Employee ID: {self.empid}")
        print(f"Employee Name: {self.name}")
        print(f"Employee Department: {self.department}")
        print(f"Employee Original Salary: {self.salary}")

    @staticmethod
    def empcount():
        print(f"Number of employees: {Employee.n}")

    def updatesalary(self, increase):
        original_salary = self.salary
        self.salary += increase
        print(f"Salary after increment: {self.salary}")


class Manager(Employee):
    def __init__(self):
        print("Manager Information:")
        super().__init__()
        super().display()
        self.updatesalary(self.increase)


class Staff(Employee):
    def __init__(self):
        print("Staff Information:")
        super().__init__()
        super().display()
        self.updatesalary(self.increase)


while True:
    print("\nMenu:")
    print("1. Add Manager")
    print("2. Add Staff")
    print("3. Display Employee Count")
    print("4. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        m1 = Manager()
    elif choice == "2":
        s1 = Staff()
    elif choice == "3":
        Employee.empcount()
    elif choice == "4":
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please enter a valid option.")


