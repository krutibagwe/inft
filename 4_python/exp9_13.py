import math
class Areacircle:
    def __init__(self):
        self.a = int(input("Enter value: "))
    def display_area(self):
        self.area = math.pi * self.a * self.a
        print("area of circle is",self.area)
        
class AreaSquare(Areacircle):
    def __init__(self):
        super().__init__()
        self.b = int(input("Enter value: "))
    def display_area(self):
        self.area = self.a * self.b
        print("area of square is ",self.area)
        
c=AreaSquare()
c.display_area()
