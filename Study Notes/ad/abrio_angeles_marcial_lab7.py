from abc import ABC, abstractmethod

class Vehicles(ABC):

    @abstractmethod
    def calculate_rental_hours(self, hours):
        pass

    @abstractmethod
    def get_vehicle_type(self):
        pass

class Car(Vehicles):

    def calculate_rental_hours(self, hours):
        hourly_rate = 310
        if hours > 5:
            hourly_rate *= 0.90
        return hours * hourly_rate

    def get_vehicle_type(self):
        return "Car"

class Truck(Vehicles):

    def calculate_rental_hours(self, hours):
        hourly_rate = 500
        if hours > 6:
            hourly_rate *= 0.90
        return hours * hourly_rate

    def get_vehicle_type(self):
        return "Truck"

class Bike(Vehicles):
    
    def calculate_rental_hours(self, hours):
        hourly_rate = 125
        if hours > 2:
            hourly_rate *= 0.90
        return hours * hourly_rate
    
    def get_vehicle_type(self):
        return "Bike"

class RentalService():

    def __init__(self):
        self.vehicles = {
            "Car": Car(),
            "Truck": Truck(),
            "Bike": Bike()
        }

    def calculate_rental_cost(self, vehicle_type, hours):
        if vehicle_type in self.vehicles:
            vehicle = self.vehicles[vehicle_type]
            return vehicle.calculate_rental_hours(hours)
        
    def get_vehicle_type(self, vehicle_type):
        if vehicle_type in self.vehicles:
            vehicle = self.vehicles[vehicle_type]
            return vehicle.get_vehicle_type()

def main():
    rental_service = RentalService()
    
    print("\nVehicle Rental Services\n")

    print("Here is a list of the vehicles you can rent:")
    for vehicle in rental_service.vehicles.keys():
        print(f"- {vehicle}")

    vehicle_type = input("Enter the type of vehicle you want to rent: ")
    hours = int(input("Enter the number of hours you are going to rent the vehicle: "))
    
    cost = rental_service.calculate_rental_cost(vehicle_type, hours)
    print(f"You have rented a {vehicle_type} for {hours} hour(s) which costs {cost} PHP.")

if __name__ == "__main__":
    main()
