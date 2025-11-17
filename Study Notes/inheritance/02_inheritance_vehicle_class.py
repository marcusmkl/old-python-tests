"""
Let's try to create a more generic class called Vehicle that would represents any types of land vehicle
such as car, truck, and motorcycle
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


# now create the objects for car, truck, and motorcycle using the Vehicle class
car = Vehicle("red", "sedan", "Toyota Vios", 4)
truck = Vehicle("white", "Cargo", "ISUZU F-Series", 10)
motorcycle = Vehicle("black", "sports bike", "Kawasaki Ninja 400", 2)

"""
Now, there is only one class representing all types of vehicle and it makes our code much smaller than previous one
but how about the unique attributes and behaviors of car? truck? motorcycle?
unique attributes: passenger_count, loading_capacity
unique behaviors: aboard_passenger(), load(), flip()
where should we define these unique attributes and behaviors?
if we add these to our Vehicle class, all objects created from this class will also have these unique attributes and 
behaviors but it does not make any sense that a truck or a car can flip, or a motorcycle to load a tons of things and
even tracks passenger count

How about objects such as bus, tricycle, tractors, or military-vehicles? These also have their own unique attributes
and behaviors

If we decide to define all of these to a single class called Vehicle, the entire class will become bloated
and eventually would hard to maintain. 
"""