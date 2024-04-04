import operations
while True:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    print("OPERATIONS: \n1.Add \n2.Subtract \n3.Multiply \n4.Divide")
    choice = input("Enter your choice (1/2/3/4): ")
    if choice == '1':
        print("Answer:", operations.add(num1, num2))
    elif choice == '2':
        print("Answer:", operations.subtract(num1, num2))
    elif choice == '3':
        print("Answer:", operations.multiply(num1, num2))
    elif choice == '4':
        print("Answer:", operations.divide(num1, num2))
    else:
        print("Invalid input! Enter correct choice.")
    continue_choice = input("Press 1 to continue or 0 to exit: ")
    if continue_choice == '0':
        print("Exiting the program...")
        break
