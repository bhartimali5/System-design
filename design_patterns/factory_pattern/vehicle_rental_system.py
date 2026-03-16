from abc import ABC, abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def get_rental_price(self):
        pass

class Car(Vehicle):
    def start_engine(self):
        return "Car engine started."

    def get_rental_price(self):
        return 50
    
class Bike(Vehicle):

    def start_engine(self):
        return "Bike engine started."

    def get_rental_price(self):
        return 20

class Truck(Vehicle):
    def start_engine(self):
        return "Truck engine started."

    def get_rental_price(self):
        return 100



## Factory method wit abstract factory class

class rentalAgency(ABC):

    def create_vehicle(self):
        pass

    def process_rental(self, days):
        vehicle = self.create_vehicle()
        print(vehicle.start_engine())
        print(f"Rental price: ${vehicle.get_rental_price() * days}")



class CarRentalAgency(rentalAgency):
    def create_vehicle(self):
        return Car()
    

class BikeRentalAgency(rentalAgency):

    def create_vehicle(self):
        return Bike()
    
    
class TruckRentalAgency(rentalAgency):
    def create_vehicle(self):
        return Truck()
     
## Sol 2 ------------Most optimized way without creating multiple factory classes, just using the base class to create vehicles based on type----------------------
"""
class rentalAgency():

    def create_vehicle(self, vehicle_type):
        return vehicle_type()
        

    def process_rental(self, days):
        vehicle = self.create_vehicle()
        print(vehicle.start_engine())
        print(f"Rental price: ${vehicle.get_rental_price() * days}")



agency = rentalAgency()
car = agency.create_vehicle(Car)
car.process_rental(3)

bike = agency.create_vehicle(Bike)
bike.process_rental(2)

"""
 
## Sol 3
"""
## SImple Factory class to create vehicles based on type
class VehicleFactory:
    @staticmethod
    def create_vehicle(vehicle_type):
        if vehicle_type == "car":
            return Car()
        elif vehicle_type == "bike":
            return Bike()
        elif vehicle_type == "truck":
            return Truck()
        else:
            raise ValueError("Unknown vehicle type")



# Usage of simple factory
if __name__ == "__main__":
    factory = VehicleFactory()
    vehicle_type = "car"
    vehicle = factory.create_vehicle(vehicle_type)
    print(vehicle.start_engine())
    print(f"Rental price: ${vehicle.get_rental_price() * 3}")  # Renting for 3 days
        
"""


## Sol 4 
## ## Using a registry to manage vehicle types
"""
class VehicleFactory:
    _registry = {}

    @classmethod
    def register_vehicle(cls, vehicle_type, vehicle_class):
        cls._registry[vehicle_type] = vehicle_class

    @classmethod
    def create_vehicle(cls, vehicle_type):
        if vehicle_type in cls._registry:
            return cls._registry[vehicle_type]()
        else:
            raise ValueError("Unknown vehicle type")    

# Registering vehicle types
VehicleFactory.register_vehicle("car", Car)
VehicleFactory.register_vehicle("bike", Bike)
VehicleFactory.register_vehicle("truck", Truck)

# Usage of registry-based factory
if __name__ == "__main__":
    factory = VehicleFactory()
    vehicle_type = "bike"
    vehicle = factory.create_vehicle(vehicle_type)
    print(vehicle.start_engine())
    print(f"Rental price: ${vehicle.get_rental_price() * 2}")  # Renting for 2 days
"""