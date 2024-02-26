while True:
    print("1.Enter 1 for AssertionError: \n2.Enter 2 for ZeroDivisionError: \n3.Enter 3 for TypeError: ")
    print("4.Enter 4 for NameError: \n5.Enter 5 for IndexError: \n6.Enter 6 to Exit\n")
    num = int(input("Enter your choice: "))

    if num==1:
        try:
            n=int(input("enter number between 2 to 3:"))
            assert n>=2 and n<=3
            print("number entered is", n)
        except AssertionError:
            print("Assertion Error: enter number between 2 to 5.")

    elif num == 2:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        try:
            c = a / b
            print("Answer is {}".format(c))
        except ZeroDivisionError:
            print("Zero Division Error: Cannot divide by zero.")

    elif num == 3:
        x = int(input("Enter a number: "))
        y = input("Enter another number: ")
        try:
            z = x + y
        except TypeError:
            print("Type Error: Cannot add an int to a string.")
            
    elif num==4:
        try:
            a=int(input("enter number a: "))
            b=int(input("enter number b : "))
            print("Dividing x by b. c=x/b is :")
            c=k/b
        except NameError:
            print("Name Error: x is not defined")

    elif num == 5:
        a = [1, 2, 3, 4, 5]
        print("The list is:")
        print(a)
        ind = int(input("Enter the index to be accessed: "))
        try:
            print("Element at {} is {}.".format(ind, a[ind]))
        except IndexError:
            print("Index Error: Index does not exist")

    elif num == 6:
        print("Exiting the program. ")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
            
 

