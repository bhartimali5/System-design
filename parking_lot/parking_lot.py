import datetime

from parking_lot.vehicle import VehicleType, Vehicle
from .config import default_parking_capacity, default_parking_floors
from .fare import FareCalculatorFactory
from .parking_spot import ParkingSpot
from .floor import Floor
from .ticket import Ticket
from .manager import Manager


class ParkingLot:

    ## Singelton implementation
    _instance = None
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(ParkingLot, cls).__new__(cls)
            cls.floors = cls._instance._create_floors()
            cls.manager = Manager(cls._instance)
        
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
        parking_spot = self.manager.get_available_spot(vehicle.vehicle_type)
        ticket = None
        try:
            if parking_spot:
                checkin_time = datetime.datetime.now()
                ticket = self.manager.generate_ticket(vehicle, parking_spot, checkin_time)
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
            self.manager.calculate_fare(ticket)
            ticket.spot.vacate()
            print(f"Vehicle checked out. Fare: ${ticket.fare:.2f}")
        else:
            print("Invalid ticket. Cannot checkout vehicle.")


    