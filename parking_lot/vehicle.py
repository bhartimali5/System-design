from enum import Enum

class VehicleType(Enum):
    CAR = 1
    MOTORCYCLE = 2
    TRUCK = 3   


class Vehicle:
    def __init__(self, vehicle_type: VehicleType):
        self.vehicle_type = vehicle_type

        