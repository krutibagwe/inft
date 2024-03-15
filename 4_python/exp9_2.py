class Book:
    def __init__(self, pages):
        self.pages = pages
    def __add__(self,others):
        return self.pages + others.pages

b1 = Book(100)
b2 = Book(200)

print(type(b1))
print(type(b2))
print(type(b1.pages))
print(type(b2.pages))
print(b1.pages + b2.pages)
print((b1.pages).__add__(b2.pages))

print(b1+b2)
