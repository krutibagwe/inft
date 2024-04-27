#Write a Python program to declare a class Calculate which calculates the Area of Circle, Triangle and Rectangle (Use Method Overloading).

class Calculate:
    def area(self, shape, *args):
        if shape == 'circle':
            radius = float(input("Enter the radius of the circle: "))
            return 3.14 * radius * radius
        elif shape == 'triangle':
            base = float(input("Enter the base length of the triangle: "))
            height = float(input("Enter the height of the triangle: "))
            return 0.5 * base * height
        elif shape == 'rectangle':
            length = float(input("Enter the length of the rectangle: "))
            width = float(input("Enter the width of the rectangle: "))
            return length * width

# Test the class
calc = Calculate()

while True:
    print("\nMenu:")
    print("1. Calculate area of circle")
    print("2. Calculate area of triangle")
    print("3. Calculate area of rectangle")
    print("4. Exit")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice == '1':
        print("Area of circle:", calc.area('circle'))
    elif choice == '2':
        print("Area of triangle:", calc.area('triangle'))
    elif choice == '3':
        print("Area of rectangle:", calc.area('rectangle'))
    elif choice == '4':
        print("Exiting program...")
        break
    else:
        print("Invalid choice. Please enter a valid option.")
