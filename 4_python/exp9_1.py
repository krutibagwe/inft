#duck typing polymorphism
class Duck:
    def talk(self):
        print("Quack... Quack")
class Dog:
    def talk(self):
        print("Bow... Bow")
class Cat:
    def talk(self):
        print("Meow... Meow")

def m(obj):
    obj.talk()
duck = Duck()
m(duck)
cat = Cat()
m(cat)
dog = Dog()
m(dog)
