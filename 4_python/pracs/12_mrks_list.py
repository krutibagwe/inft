# Write a Python program to read marks of 3 subjects of a student and check if the average marks are above 50 then print that student is passed in exam

while True:
    marks = []

    for i in range(3):
        mark = float(input(f"Enter the marks of subject {i+1} (out of 100): "))
        marks.append(mark)

    total = sum(marks)
    avg = total / 3

    if avg >= 50:
        print(f"Average marks are {avg}.\nPASS!")
    else:
        print(f"Average marks are {avg}.\nFAIL!")  

