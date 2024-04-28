#Write a Python program to create, write, read, append and close a file using File manipulating methods.

f = open ("abc.txt", "r")
str1 = f.read()
print(str1)
f.close()

f=open("abc.txt", "a")
str2 = input("Enter a string: ")
f.write(str2)
f.close()

f=open("abc.txt", "w")
str3 = input("Enter a string: ")
f.write(str3)
f.close()
