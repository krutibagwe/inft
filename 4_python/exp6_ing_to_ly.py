words = ["playing", "reading","sunday", "writing", "jogging", "coding", "dinner"]
print ("Original list: ", words)
list_len= len(words)
for i in range(list_len):
    if words[i].endswith('ing'):
        words[i] = words[i].replace('ing', 'ly')
print("Modified list: ", words)
