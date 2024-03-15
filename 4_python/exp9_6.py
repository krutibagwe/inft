class Demo:
    def sum(self, *a):
        total = 0
        for x in a:
            total+=x
        print("Sum: ", total)

d = Demo()
d.sum(10,20,30)
d.sum(10,20)
d.sum(10)
