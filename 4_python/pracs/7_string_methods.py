#Write a Python program to demonstrate any 10 inbuilt String methods

sample = "hello world Good morning"
print(sample, "\n")

#1 length of string (len)
print("length: ", len(sample), "\n")

#2 capitalize first character
print("first char capital: ", sample.capitalize(), "\n")

#3 all uppercase
print("Uppercase: ", sample.upper(), "\n")

#4 all lowercase
print("Lowercase: ", sample.lower(), "\n")

#5 title case
print("Title case: ", sample.title(), "\n")

#6 Find: lowest index of
word = "Good"
print(word, sample.find(word), "\n")

#7 splits string into list
word_list = sample.split()
print(word_list, "\n")

#8 all chars are alphabet (not including spaces)
print("Is alpha: ", sample.isalpha(), "\n")

#9 starts with
startw = "hello"
print(startw, sample.startswith(startw), "\n")

#10 check if all lower
sample2 = "good night"
print("Is lower")
print(sample2, sample2.islower(), "\n")
