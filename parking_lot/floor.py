from parking_lot.vehicle import VehicleType
from parking_lot.spot_type import SpotType

vehicle_type_to_spot_type = {
    VehicleType.CAR: SpotType.MEDIUM,   
    VehicleType.MOTORCYCLE: SpotType.SMALL,
    VehicleType.TRUCK: SpotType.LARGE
}


class Floor:
    def __init__(self, floor_number):
        self.floor_number = floor_number
        self.parking_spots = []  # List of ParkingSpot objects

    def add_parking_spot(self, parking_spot):
        self.parking_spots.append(parking_spot)

    def get_available_spots(self, vehicle_type: VehicleType):
        for spot in self.parking_spots:
            if spot.is_available() and spot.spot_type == vehicle_type_to_spot_type[vehicle_type]:
                return spot
        return None
    