class Student:
    def __init__ (self,name,marks):
        self.name= name
        self.marks = marks
    def __gt__ (self, other):
        return self.marks>other.marks
    def __lt__ (self, other):
        return self.marks<other.marks

s1 = Student("Alice", 100)
s2 = Student("Bob", 200)
print("s1>s2 = ", s1>s2)
print("s1<s2 = ", s1<s2)
