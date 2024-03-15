class Vehicle:
    def vehicle_info(self):
        print("The type of vehicle is none")
    def mode_transport(self):
        print("The type of transport is none")
        
class Bike(Vehicle):
    def vehicle_info(self):
        print("The type of vehicle is Bike.")
    def mode_transport(self):
        print("The type of transport is road transport.")
        
class Train(Vehicle):
    def vehicle_info(self):
        print("The type of vehicle is Train.")
    def mode_transport(self):
        print("The type of transport is rail transport.")
T = Train()
B = Bike()

print("Details of Train:")
T.vehicle_info()
T.mode_transport()

print("\nDetails of bike:")
B.vehicle_info()
B.mode_transport()
