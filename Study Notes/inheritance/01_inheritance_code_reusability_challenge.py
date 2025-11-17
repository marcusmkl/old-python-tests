"""
THE NEED FOR CODE RE-USABILITY

Let's say we want to create a class for each type of vehicle (e.g. Car, Truck, Motorcycle)
What did you notice? Does each class has similar attributes and behaviors?
How about differences in attributes and behaviors?
"""


class Car:
    number_of_wheels = 4

    def __init__(self, color, body_type, seat_capacity, model_name):
        self.car_color = color
        self.body_type = body_type
        self.seating_capacity = seat_capacity
        self.model_name = model_name
        self.is_engine_off = True
        self.is_brake_applied = False
        self.passenger_count = 0

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

    def aboard_passenger(self, passenger_count):
        if self.passenger_count < self.seating_capacity:
            remaining_seats = self.seating_capacity - self.passenger_count
            if remaining_seats >= passenger_count:
                self.passenger_count += passenger_count
            else:
                print(f"Remaining seats are not enough for {passenger_count}.")
        else:
            print("Car in full capacity.")


class Truck:

    def __init__(self, color, body_type, load_capacity, model_name, wheels):
        self.truck_color = color
        self.body_type = body_type
        self.load_capacity = load_capacity
        self.model_name = model_name
        self.number_of_wheels = wheels
        self.is_engine_off = True
        self.is_brake_applied = False
        self.load_count = 0

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

    def load(self, load_amount):
        if self.load_count < self.load_capacity:
            remaining_load = self.load_capacity - self.load_count
            if remaining_load >= self.load_count:
                self.load_count += load_amount
            else:
                print(f"Not enough load capacity for {load_amount}. Current load is {self.load_count} tons.")
        else:
            print("Truck in full capacity.")


class Motorcycle:
    number_of_wheels = 2

    def __init__(self, color, body_type, model_name):
        self.motorcycle_color = color
        self.body_type = body_type
        self.model_name = model_name
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

    def flip(self):
        self.run()
        print(f"{self.model_name} is approaching a ramp at maximum speed!")
        print(f"Yes! It's a double back flip!")


my_car = Car("red", "sedan", 5, "Toyota Vios")
my_truck = Truck("white", "Dump", 10, "FUSO FJ28C", 10)
my_motorcycle = Motorcycle("black", "sports bike", "Kawasaki Ninja 400")

my_car.aboard_passenger(2)
my_car.engine_turn_on()
my_car.run()
my_car.stop()
my_car.aboard_passenger(4)
my_car.engine_turn_off()

my_truck.load(7)
my_truck.engine_turn_on()
my_truck.run()
my_truck.stop()
my_truck.load(5)
my_truck.engine_turn_off()

my_motorcycle.engine_turn_on()
my_motorcycle.run()
my_motorcycle.stop()
my_motorcycle.flip()
my_motorcycle.stop()
my_motorcycle.engine_turn_off()

"""
Even using classes and objects, there's a lot of duplicate codes
e.g. attributes such as color, body_type, model_name
e.g. behaviors such as run(), stop(), engine_turn_on(), engine_turn_off()
How about we create a more generic class called Vehicle? Will it solve the code duplications?
"""