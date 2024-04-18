marks = [] #empty list to store marks

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

