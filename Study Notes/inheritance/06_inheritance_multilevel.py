from Vehicle import Car


class Sedan(Car):
    def __init__(self, color, model_name, transmission_type):
        super().__init__(color, "Sedan", 5, model_name)
        self.transmission = transmission_type

    def get_transmission_type(self):
        return self.transmission


my_taxi = Sedan("White", "Toyota Vios", "Manual")

my_taxi.aboard_passenger(1)
my_taxi.engine_turn_on()
my_taxi.run()
my_taxi.stop()
my_taxi.aboard_passenger(5)
transmission = my_taxi.get_transmission_type()
my_taxi.display_info()
print(f"Transmission type: {transmission}")

# if my_taxi.__class__ is Sedan:
#     print("my_taxi is a Sedan")
# else:
#     print("Not a Sedan")

if isinstance(my_truck, Truck):
    print("my_taxi is a Sedan")
else:
    print("Not a Sedan")