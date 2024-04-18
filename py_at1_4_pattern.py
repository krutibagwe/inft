def print_pattern():
    pattern = "ACDFH"
    for i in range(len(pattern)):
        row = ""
        for j in range(len(pattern) - i):
            row += chr(ord(pattern[j]) + i)
        print(row)

print_pattern()

