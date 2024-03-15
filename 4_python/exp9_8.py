class Demo:
    def __init__(self):
        print("No-arg Constructor")
    def __init__(self,a):
        print("One-arg Constructor")
    def __init__(self,a,b):
        print("Two-arg Constructor")

#d1 = Demo()
#d1 = Demo(10)
d1 = Demo(10,20)
