class Demo:
    def m1(self):
        print("no-arg method")
    def m1(self,a):
        print("one-arg method")
    def m1(self,a,b):
        print("two-arg method")

d = Demo()
d.m1(10,20)
