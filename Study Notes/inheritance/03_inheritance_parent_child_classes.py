"""
Inheritance - one of the pillars of OOP
It is a mechanism where you can derive a class from another class that share a set of attributes and behaviors
Inheritance is based on a hierarchical relationship between classes
The key to understanding Inheritance is that it provides code re-usability.
Instead of writing the same code repeatedly, we can simply inherit the properties of an existing class into the other.

# IS-A Relationship

Example:
    Vehicle
        - Car
            - Sedan
            - Hatchbacks
            - SUV
            - Pickup
        - Truck
            - Cargo
            - Dump
            - Tanker
            - Pickup
        - Motorcycle
            - Sports bike
            - Scooter
        - Bus
            - Single-decker
            - Double-decker
        - Van
            -

Super class or Parent class - the class whose attributes and behaviors are inherited
Subclass or Child class - the class inherits the attributes and behaviors of the Super or Parent class
"""


# Vehicle is the parent class of Car, Truck, and Motorcycle
class Vehicle:
    # @classmethod
    # def set_attributes(cls, color, body_type, model_name, wheels):
    #     cls.color = color
    #     cls.body_type = body_type
    #     cls.model_name = model_name
    #     cls.number_of_wheels = wheels
    #     cls.is_engine_off = True
    #     cls.is_brake_applied = False

    def __init__(self, color, body_type, model_name, wheels):
        self.color = color
        self.body_type = body_type
        self.model_name = model_name
        self.number_of_wheels = wheels
        self.is_engine_off = True
        self.is_brake_applied = False

    def engine_turn_on(self):
        self.is_engine_off = False

    def engine_turn_off(self):
        self.is_engine_off = True

    def run(self):
        if not self.is_engine_off:
            self.is_brake_applied = False
            print(f"{self.model_name} is running.")
        else:
            print(f"{self.model_name} engine is off.")

    def stop(self):
        self.is_brake_applied = True


# Car is a child class of Vehicle
class Car(Vehicle):

    def __init__(self, color, body_type, seat_capacity, model_name):
        self.color = color
        self.body_type = body_type
        self.seating_capacity = seat_capacity
        self.model_name = model_name
        self.number_of_wheels = 4
        self.is_engine_off = True
        self.is_brake_applied = False
        self.passenger_count = 0

    def aboard_passenger(self, passenger_count):
        if self.passenger_count < self.seating_capacity:
            remaining_seats = self.seating_capacity - self.passenger_count
            if remaining_seats >= passenger_count:
                self.passenger_count += passenger_count
            else:
                print(f"Remaining seats are not enough for {passenger_count}.")
        else:
            print("Car in full capacity.")


# Truck is a child class of Vehicle
class Truck(Vehicle):
    def __init__(self, color, body_type, load_capacity, model_name, wheels):
        self.color = color
        self.body_type = body_type
        self.load_capacity = load_capacity
        self.model_name = model_name
        self.number_of_wheels = wheels
        self.is_engine_off = True
        self.is_brake_applied = False
        self.load_count = 0

    def load(self, load_amount):
        if self.load_count < self.load_capacity:
            remaining_load = self.load_capacity - self.load_count
            if remaining_load >= self.load_count:
                self.load_count += load_amount
            else:
                print(f"Not enough load capacity for {load_amount}. Current load is {self.load_count} tons.")
        else:
            print("Truck in full capacity.")


# Motorcycle is a child class of Vehicle
class Motorcycle(Vehicle):
    def __init__(self, color, body_type, model_name):
        self.color = color
        self.body_type = body_type
        self.model_name = model_name
        self.is_engine_off = True
        self.is_brake_applied = False

    def flip(self):
        self.run()
        print(f"{self.model_name} is approaching a ramp at maximum speed!")
        print(f"Yes! It's a double back flip!")


# create objects for each child class
my_car = Car("red", "sedan", 5, "Toyota Vios")
my_truck = Truck("white", "Dump", 10, "FUSO FJ28C", 10)
my_motorcycle = Motorcycle("black", "sports bike", "Kawasaki Ninja 400")

# my_car object has Vehicle attributes and behaviors
my_car.aboard_passenger(2)
my_car.engine_turn_on()
my_car.run()
my_car.stop()
my_car.aboard_passenger(4)
my_car.engine_turn_off()

# my_truck object has Vehicle attributes and behaviors
my_truck.load(7)
my_truck.engine_turn_on()
my_truck.run()
my_truck.stop()
my_truck.load(5)
my_truck.engine_turn_off()

# my_motorcycle object has Vehicle attributes and behaviors
my_motorcycle.engine_turn_on()
my_motorcycle.run()
my_motorcycle.stop()
my_motorcycle.flip()
my_motorcycle.stop()
my_motorcycle.engine_turn_off()

"""
Amazing, isn't it?
But have you notice something? There are still duplication / code-repetition, can you identify it? 
"""