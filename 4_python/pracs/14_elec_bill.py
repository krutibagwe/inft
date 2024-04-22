''' Write a program to calculate electricity bill according to following criteria
i. first 10 units then no charge
ii. next 100 units - 5 rs per unit
iii. next 200 units - 10 rs per unit
iv. Above this - 15 rs per unit '''

while True:
    units = int(input("Enter the units: "))

    if units <= 10:
            print("No charge.")
    elif units <= 110:
        charge = (units - 10) * 5
        print(f"Electricity Bill Amount: {charge}")
    elif units <= 310:
        charge = (100 * 5) + ((units - 110) * 10)
        print(f"Electricity Bill Amount: {charge}")
    else:
        charge = (100 * 5) + (200 * 10) + ((units - 310) * 15)
        print(f"Electricity Bill Amount: {charge}")
