f = open("abc.txt", "w+")
while (str != "$"):
    str = input("enter string: ")
    if (str !="$"):
        f.write(str)
f.close()
