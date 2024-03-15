class Demo:
    def __init__(self, *a):
        print("Constructor with variable number of arguments")

d1 = Demo()
d2 = Demo(10)
d3 = Demo(10,20)
d4 = Demo(10,20,30)
d5 = Demo(10,20,30,40,50,60)
