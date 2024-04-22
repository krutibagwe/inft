# Write a Python class named Circle constructed by a radius and two methods which will compute the area and the perimeter of a circle.

import math

while True: 
    class Circle:
        def __init__(self):
            self.radius = float(input("enter the radius: "))

        def calc_area(self):
            return math.pi * self.radius**2

        def calc_peri(self):
            return 2 * math.pi * self.radius

    c1 = Circle()
    print("Area: ", c1.calc_area())
    print("Perimeter: ", c1.calc_peri())
