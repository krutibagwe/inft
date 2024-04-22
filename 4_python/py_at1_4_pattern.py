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
