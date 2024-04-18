def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

n = int(input("Enter the number of years you want to check: "))

years = [] #empty list to store years 

for i in range(n):
    year = int(input(f"Enter year {i + 1}: "))
    years.append(year)
    if is_leap_year(year):
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")
