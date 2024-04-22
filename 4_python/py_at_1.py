while True:
    print("A. Marks\nB. Series\nC. Prime number\nD. Pattern\nE. Leap year\nF. EXIT")
    choice = input("Enter your choice (A-F): ").upper()

    if choice == "A":
        # Option A: Marks calculation
        marks = []
        for i in range(5):
            while True:
                try:
                    subject_mark = float(input(f"Enter marks for subject {i+1}: "))
                    if subject_mark < 0 or subject_mark > 100:
                        print("Marks should be between 0 and 100. Please try again.")
                        continue
                    marks.append(subject_mark)
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid number.")

        total_marks = sum(marks)
        min_mark = min(marks)
        result = total_marks - min_mark

        print(f"Total marks: {total_marks}")
        print(f"Minimum marks: {min_mark}")
        print(f"Result (total marks - minimum mark): {result}")

    elif choice == "B":
        # Option B: Series sum
        def factorial(num):
            if num == 0 or num == 1:
                return 1
            else:
                result = 1
                for i in range(2, num + 1):
                    result *= i
                return result

        def series_sum(n):
            sum_series = 0
            for i in range(n + 1):
                term = 1 / factorial(i)
                sum_series += term
            return sum_series

        while True:
            try:
                n = int(input("Enter a positive integer n: "))
                if n < 0:
                    print("Please enter a positive integer.")
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter a valid integer.")

        result_sum = series_sum(n)
        print("Series S = 1 + 1/1! + 1/2! + 1/3! ...... 1/n!")
        print(f"The sum of the series S for n = {n} is: {result_sum}")

    elif choice == "C":
        # Option C: Prime number check
        def is_prime(number):
            if number <= 1:
                return False
            for i in range(2, int(number**0.5) + 1):
                if number % i == 0:
                    return False
            return True

        num = int(input("Enter a positive integer to check if it's prime: "))
        if is_prime(num):
            print(f"{num} is a prime number.")
        else:
            print(f"{num} is not a prime number.")

    elif choice == "D":
        # Option D: Pattern printing
        def print_pattern(rows):
        start_char = ord('a')  # ASCII value of 'a'
    
        for i in range(rows):
            current_char = start_char + i
            for j in range(rows - i):
                print(chr(current_char), end='')
                current_char += 2  # Move to the next character in the sequence
            print()  # Move to the next line after each row
    
        rows = 5
        print_pattern(rows)


    elif choice == "E":
        # Option E: Leap year check
        def is_leap_year(year):
            return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

        n = int(input("Enter the number of years you want to check: "))
        years = []

        for i in range(n):
            year = int(input(f"Enter year {i + 1}: "))
            years.append(year)
            if is_leap_year(year):
                print(f"{year} is a leap year.")
            else:
                print(f"{year} is not a leap year.")

    elif choice == "F":
        # Option F: Exit the program
        print("Exiting program...")
        break

    else:
        print("Incorrect choice entered!")
