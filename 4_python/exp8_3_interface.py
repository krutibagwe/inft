from abc import ABC,abstractmethod

class Car(ABC):
    @abstractmethod
    def mileage(self):
        pass
    def color(self):
        print("white")

class Maruti_Suzuki(Car):
    #def mileage(self):
        pass
        #print("Mileage is 30 kmph")

class Tata(Car):
    def mileage(self):
        print("Mileage is 35 kmph")
        
class Duster(Car):
    def mileage(self):
        print("Mileage is 40 kmph")

m1=Maruti_Suzuki()
t1=Tata()
d1=Duster()
t1.mileage()
d1.mileage()
m1.mileage()
