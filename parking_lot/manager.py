

from parking_lot.ticket import Ticket
from parking_lot.vehicle import VehicleType
from parking_lot.fare import FareCalculatorFactory

class Manager:
    def __init__(self, parking_lot):
        self.parking_lot = parking_lot

        
    def get_available_spot(self, vehicle_type: VehicleType):
        available_spots = []
        for floor in self.parking_lot.floors:
            available_spots.append(floor.get_available_spots(vehicle_type))
        if available_spots:
            return available_spots[0]  # Return the first available spot
        return None


    def generate_ticket(self, vehicle, spot, checkin_time):
        return Ticket( vehicle=vehicle, spot=spot, checkin_time=checkin_time)
        

    def calculate_fare(self, ticket):
        duration = (ticket.checkout_time - ticket.checkin_time).total_seconds() / 3600  # duration in hours
        fare_calculator = FareCalculatorFactory.get_fare_calculator(ticket.spot.spot_type)
        
        ticket.fare = fare_calculator.calculate_fare(duration)
        print(f"Calculated fare for {ticket.vehicle.vehicle_type}: ${ticket.fare:.2f}")
