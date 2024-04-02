#to demonstrate pickling
import pickle
from pickle11_test1 import Student

f = open("sd.dat", "wb" ) #write binary
n = int(input("enter number of students"))
for i in range(n):
    s_rollno = int(input("enter roll no: "))
    s_name = input("enter name: ")
    s_age = int(input("enter age: "))
    s = Student(s_rollno, s_name, s_age)
    pickle.dump(s,f)
f.close()

#unpickling
f = open("sd.dat", "rb") #read binary
while(True):
    try:
        obj = pickle.load(f)
        obj.disp()
    except:
        print("End of File")
        break
f.close()
  
