#Write a Python program to Create a user defined module to implement a data structure queue. The module should perform the following functions: insertion of element from the rear side, deletion of element from the front side, rotate and extend queue.

list1 = []

while True:
    print("\n1.Enqueue from rear side\n2.Dequeue from front side\n3.Extend the queue\n4.Rotate the queue\n5.Exit the program")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        insertr = int(input("enter the element to be inserted:  "))
        list1.append(insertr)
        print("Queue after insertion from rear end:")
        print(list1)

    if choice == 2:
        list1.pop(0)
        print("Queue after deletion from front end:")
        print(list1)

    if choice == 3:
        list2 = []
        n2 = int(input("Enter number of elements to be extended: "))
        print(f"Enter the {n2} elements: ")
 
        for i in range(0, n2):
            ele2 = int(input())
            list2.append(ele2)

        list1.extend(list2)
        print("Queue after extending: ")
        print(list1)

    if choice == 4:
        n3= int(input("Enter the number to be rotated by: "))
        list1 = [list1[(i+n3)%len(list1)] for i,x in enumerate(list1)]
        print(f"Queue after rotation by {n3}: ")
        print(list1)

    if choice == 5:
        print("Exiting the program.")
        break
