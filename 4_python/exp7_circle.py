import math
class Circle:
    def __init__ (self):
        self.radius = int(input("enter the radius: "))

    def area(self):
        print(f"Area of circle of radius {self.radius} is { math.pi * self.radius * self.radius}.")

    def perimeter(self):
        print (f"Perimeter of circle of radius {self.radius} is {2* math.pi* self.radius}. ")


c1 = Circle()
c1.area()
c1.perimeter()
