f = open ("abc.txt", "r")
str1 = f.read()
print(str1)
f.close()

f=open("abc.txt", "w")
str2 = input("Enter a string: ")
f.write(str2)
f.close()
