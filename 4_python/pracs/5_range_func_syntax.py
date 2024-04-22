#Write a Python program to implement three different syntaxes of range function

print("Method 1 ONLY STOP")
stop = 6
print("Stop: ", stop)
for i in range(stop):
    print(i, end = " ")
    

print("\n\nMethod 2 START AND STOP")
start = 2
stop = 8
print("Start: ", start)
print("Stop: ", stop)
for i in range(start, stop):
    print(i, end = " ")

print("\n\nMethod 3 START STOP AND STEP")
start = 3
stop = 13
step = 4
print("Start: ", start)
print("Stop: ", stop)
print("Step: ", step)
for i in range(start, stop, step):
    print(i, end = " ")
