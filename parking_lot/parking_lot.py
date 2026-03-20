import datetime

from parking_lot.vehicle import VehicleType, Vehicle
from .config import default_parking_capacity, default_parking_floors
from .fare import CarFareCalculator, MotorcycleFareCalculator, TruckFareCalculator
from .parking_spot import ParkingSpot
from .floor import Floor
from .ticket import Ticket


class ParkingLot:

    ## Singelton implementation
    _instance = None
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(ParkingLot, cls).__new__(cls)
            cls.floors = cls._instance._create_floors()
        
        return cls._instance
    
    def _create_floors(self):
        floors = []
        for i in range(1,  default_parking_floors):
            floor = Floor(floor_number=i)
            floors.append(floor)
            self._create_parking_spots(floor)
        return floors

    def _create_parking_spots(self, floor: Floor):
        for spot_type, capacity in default_parking_capacity.items():
            for _ in range(capacity):
                parking_spot = ParkingSpot(floor_number=floor.floor_number, spot_type=spot_type)
                floor.parking_spots.append(parking_spot)


    def checkin_vehicle(self, vehicle: Vehicle):
        parking_spot = self.get_available_spot(vehicle.vehicle_type)
        ticket = None
        try:
            if parking_spot:
                checkin_time = datetime.datetime.now()
                ticket = self.generate_ticket(vehicle, parking_spot, checkin_time)
                parking_spot.occupy()
                print(f"Vehicle checked in at spot {parking_spot.spot_id} on floor {parking_spot.floor_number}.")
                print(f"Ticket ID: {ticket.ticket_id}, Check-in Time: {ticket.checkin_time}")
            else:
                print("No available spots for this vehicle type.")
            return ticket
        except Exception as e:
            print(f"Error during check-in: {e}")
            return None


    def checkout_vehicle(self, ticket):
        if ticket:  
            ticket.checkout_time = datetime.datetime.now()
            self.calculate_fare(ticket)
            ticket.spot.vacate()
            print(f"Vehicle checked out. Fare: ${ticket.fare:.2f}")
        else:
            print("Invalid ticket. Cannot checkout vehicle.")


    def get_available_spot(self, vehicle_type: VehicleType):
        available_spots = []
        for floor in self.floors:
            available_spots.append(floor.get_available_spots(vehicle_type))
        if available_spots:
            return available_spots[0]  # Return the first available spot
        return None


    def generate_ticket(self, vehicle, spot, checkin_time):
        return Ticket( vehicle=vehicle, spot=spot, checkin_time=checkin_time)
        

    def calculate_fare(self, ticket):
        duration = (ticket.checkout_time - ticket.checkin_time).total_seconds() / 3600  # duration in hours
        if ticket.vehicle.vehicle_type == VehicleType.CAR:
            fare_calculator = CarFareCalculator()
        elif ticket.vehicle.vehicle_type == VehicleType.MOTORCYCLE:
            fare_calculator = MotorcycleFareCalculator()
        elif ticket.vehicle.vehicle_type == VehicleType.TRUCK:
            fare_calculator = TruckFareCalculator()
        else:
            raise ValueError("Unknown vehicle type")
        
        ticket.fare = fare_calculator.calculate_fare(duration)
        print(f"Calculated fare for {ticket.vehicle.vehicle_type}: ${ticket.fare:.2f}")
