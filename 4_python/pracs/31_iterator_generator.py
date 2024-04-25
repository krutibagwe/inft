# Write a Python program to demonstrate the use of iterator and generator functions.

class MyIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        value = self.data[self.index]
        self.index += 1
        return value

def square_generator(n):
    for i in range(1, n + 1):
        yield i**2

# Using the custom iterator class
my_iterator = MyIterator([1, 2, 3, 4, 5])
print("Using custom iterator:")
for num in my_iterator:
    print(num)
print()

# Using the generator function
my_generator = square_generator(5)
print("Using generator function:")
for num in my_generator:
    print(num)
