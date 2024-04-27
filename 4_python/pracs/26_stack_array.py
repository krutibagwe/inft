#Write a Python program to implement a stack using an array.

import array as arr

class Stack:
    def __init__(self,size):
        self.size = size
        self.stack = arr.array('i', [0] * size)
        self.top = -1

    def is_full(self):
        return self.top == self.size - 1

    def is_empty(self):
        return self.top == -1

    def push(self, num):
        if self.is_full():
            print("Stack is full. Cannot push element!")
        else:
            self.top += 1
            self.stack[self.top] = num
            print(f"Pushed {num} onto stack.")

    def pop(self):
        if self.is_empty():
            print("Stack is empty. Cannot pop element!")
        else:
            popped = self.stack[self.top]
            self.top -= 1
            print(f"Poppped element: {popped}")

    def display(self):
        if self.is_empty():
            print("Stack is empty!")
        else:
            print("Stack elements: ")
            for i in range(self.top, -1, -1):
                print(self.stack[i])

size = int(input("Enter size of the stack: "))
stack = Stack(size)

while True:
    print("\nStack Operations:")
    print("1. Push")
    print("2. Pop")
    print("3. Display")
    print("0. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        num = int(input("Enter number to be pushed: "))
        stack.push(num)
    elif choice == 2:
        stack.pop()
    elif choice == 3:
        stack.display()
    elif choice == 0:
        print("Exiting the program...")
        break
    else:
        print("Invalid choice. Please try again.")
        
