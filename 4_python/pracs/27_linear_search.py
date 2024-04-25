#Write a python program to implement Linear Search Algorithm

def linearSearch(array,key):
    for i in range(len(array)):
        if array[i]==key:
            return i
    return -1

lst=[]
length = int(input("enter the number of elements in the list: "))

for i in range(length):
    elem= int(input(f"enter element {i+1}: "))
    lst.append(elem)

key = int(input("enter the number to be searched: "))
result = linearSearch(lst,key)

if result != -1:
    print(f"Element {key} is found at index: {result}")
else:
    print(f"Element {key} is not found in the list.")
