"""
The super() function
    - it's a built-in function in Python that provides a convenient way to access 
    attributes and behaviors of parent classes
    - it can also call parent's constructor to initialize its attributes
    - using super().__init__(), you can initialize the attributes inherited from the parent class without typing them
    again in the __init__() function of the child class

"""


class Vehicle:
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

    def get_vehicle_info(self):
        info = f"Model name: {self.model_name}\n"
        info += f"Body type: {self.body_type}\n"
        info += f"Color: {self.color}\n"
        info += f"Number of Wheels: {self.number_of_wheels}\n"
        return info


class Car(Vehicle):
    def __init__(self, color, body_type, seat_capacity, model_name):
        super().__init__(color, body_type, model_name, 4)
        self.seating_capacity = seat_capacity
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

    def display_info(self):
        info = super().get_vehicle_info()
        info += f"Seating capacity: {self.seating_capacity}\n"
        print(info)


class Truck(Vehicle):
    def __init__(self, color, body_type, load_capacity, model_name, wheels):
        super().__init__(color, body_type, model_name, wheels)
        self.load_capacity = load_capacity
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

    def display_info(self):
        info = super().get_vehicle_info()
        info += f"Loading capacity: {self.load_capacity} tons\n"
        print(info)


class Motorcycle(Vehicle):
    def __init__(self, color, body_type, model_name):
        super().__init__(color, body_type, model_name, 2)

    def flip(self):
        self.run()
        print(f"{self.model_name} is approaching a ramp at maximum speed!")
        print(f"Yes! It's a double back flip!")

    def display_info(self):
        info = super().get_vehicle_info()
        print(info)


my_car = Car("red", "sedan", 5, "Toyota Vios")
my_truck = Truck("white", "Dump", 10, "FUSO FJ28C", 10)
my_motorcycle = Motorcycle("black", "sports bike", "Kawasaki Ninja 400")


my_car.aboard_passenger(2)
my_car.engine_turn_on()
my_car.run()
my_car.stop()
my_car.aboard_passenger(4)
my_car.engine_turn_off()
my_car.display_info()

my_truck.load(7)
my_truck.engine_turn_on()
my_truck.run()
my_truck.stop()
my_truck.load(5)
my_truck.engine_turn_off()
my_truck.display_info()

my_motorcycle.engine_turn_on()
my_motorcycle.run()
my_motorcycle.stop()
my_motorcycle.flip()
my_motorcycle.stop()
my_motorcycle.engine_turn_off()
my_motorcycle.display_info()