#Write a python program to read marks of 3 subjects of 10 students and print 5 Marks total marks and average of each student. Also print the message if average is greater than 50 they are “pass”

for student in range(1, 11):
    marks = []

    for subject in range(1, 4):
        mark = float(input(f"Enter the marks of student {student}, subject {subject} (out of 100): "))
        marks.append(mark)
    
    total = sum(marks)
    avg = total / 3
    
    print(f"Total marks of student {student} (out of 300): {total}")
    print(f"Average marks of student {student}: {avg:.2f}")
    
    if avg >= 50:
        print("Result: PASS\n")
    else:
        print("Result: FAIL\n")
