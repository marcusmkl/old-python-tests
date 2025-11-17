"""
Different Forms of Inheritance

Single Inheritance
    - a child class only inherits one parent class
Multiple Inheritance
    - a child class inherits more than one parent class
Multi-level Inheritance
    - a child class inherits a parent class; this parent class is a child of another parent class
    - therefore, all attributes and behaviors of the parent of the parent class are also inherited to the child class
"""


class Mammal:
    def mammal_info(self):
        print("Mammals can give direct birth.")

    def eat(self):
        print("Mammal is eating")


class WingedAnimal:
    def winged_animal_info(self):
        print("Winged animals can flap.")

    def eat(self):
        print("WingedAnimal is eating")


class NocturnalAnimal:
    def nocturnal_animal_info(self):
        print("Nocturnal animal is active during night")

    def eat(self):
        print("Nocturnal animal is eating.")

class Bat(Mammal, WingedAnimal, NocturnalAnimal): # MRO - Method Resolution Order
    def fly(self):
        print(f"I am flying...")

    # method overriding
    def eat(self):
        WingedAnimal.eat(self)


# create an object of Bat class
my_bat = Bat()
my_bat.mammal_info()
my_bat.winged_animal_info()
my_bat.fly()
my_bat.eat()

# the diamond problem
# let A = Vehicle
# let B = Car
# let C = Truck
# let D = Pickup


# import Vehicle
#
#
# class Pickup(Vehicle.Truck, Vehicle.Car): # MRO
#     def __init__(self, color, body_type, seat_capacity, model_name, load_capacity):
#         super().__init__(color, body_type, load_capacity, model_name, 4)
#         Vehicle.Car.__init__(self, color, body_type, seat_capacity, model_name)
#
#
# my_pickup = Pickup("black", "pickup", 3, "FORD Truck", 10)
# print(my_pickup.seating_capacity)
# print(my_pickup.load_capacity)





