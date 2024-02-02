units = int(input("Enter the number of units: "))

if units <= 10:
    bill = 0

elif units <= 110:
    bill = (units - 10) * 5

elif units <= 210:
    bill = 100 * 5 + (units - 110) * 10

print("The electricity bill for {} units is Rs {}.".format(units, bill))
