#Create a class Student to input data members roll number, name, age
#with a display method to print their details,using pickle module.

class Student:
    def __init__(self, r, n, a):
        self.rollno = r
        self.name = n
        self.age = a

    def disp(self):
        print(f"\nName: {self.name}\nRoll no: {self.rollno}\nAge: {self.age}")


#to demonstrate pickling
import pickle

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
  
