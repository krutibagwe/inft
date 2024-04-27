#Write a Python program to Implement queue using deque (deck) and show insertion of element from the rear side, deletion of element from the front side, rotate and extend queue..

from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, item):
        """Inserts an element from the rear side of the queue."""
        self.queue.append(item)

    def dequeue(self):
        """Deletes an element from the front side of the queue."""
        if len(self.queue) == 0:
            return None
        return self.queue.popleft()

    def rotate(self, n):
        """Rotates the queue n steps to the right (positive n) or left (negative n)."""
        self.queue.rotate(n)

    def extend(self, iterable):
        """Extends the queue by appending elements from the iterable."""
        self.queue.extend(iterable)

    def display(self):
        print(self.queue)

#--------------------------------------------------------------------
#from this_file_name import Queue

        
# Menu-driven interface
queue = Queue()

while True:
    print("\nQueue Operations:")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Rotate")
    print("4. Extend")
    print("5. Display")
    print("0. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        item = input("Enter the item to enqueue: ")
        queue.enqueue(item)
    elif choice == '2':
        item = queue.dequeue()
        if item is not None:
            print(f"Dequeued item: {item}")
        else:
            print("Queue is empty.")
    elif choice == '3':
        n = int(input("Enter the number of steps to rotate (positive or negative): "))
        queue.rotate(n)
    elif choice == '4':
        items = input("Enter the items to extend (separated by space): ").split()
        queue.extend(items)
    elif choice == '5':
        queue.display()
    elif choice == '0':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")
                    


