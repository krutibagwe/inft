import math
class AreaCircle:
    def __init__(self):
        self.a = int (input())

    def dispArea(self):
        self.area = math.pi * math.pi * self.a * self.a
        print(f"Area of circle of radius {self.a} is {self.area}.")

class AreaTriangle(AreaCircle):
    def __init__(self):
        print("Enter height: ", end= " ")
        super().__init__()
        self.b = int(input("Enter base: "))
    def dispArea(self):
        self.area = 0.5 * self.a * self.b
        print(f"Area of triangle of height {self.a} and base {self.b} is {self.area}")

class AreaRect(AreaCircle):
    def __init__(self):
        print("Enter length: ", end = " ")
        super().__init__()
        self.b = int(input("Enter breadth: "))
    def dispArea(self):
        self.area = self.a * self.b
        print(f"Area of rectangle of length {self.a} and breadth {self.b} is {self.area}")

print("TRIANGLE: ")
t1 = AreaTriangle()
t1.dispArea()

print("\nRECTANGLE: ")
r1= AreaRect()
r1.dispArea()
