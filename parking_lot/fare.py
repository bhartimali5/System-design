from abc import ABC, abstractmethod

from parking_lot.config import base_fair
from parking_lot.spot_type import SpotType

class FareCalculator(ABC):
    @abstractmethod
    def calculate_fare(self, hours: int) -> float:
        pass

class CarFareCalculator(FareCalculator):
    def calculate_fare(self, hours: int) -> float:
        base_fare = base_fair[SpotType.MEDIUM]
        hourly_rate = 2.0
        return base_fare + (hourly_rate * hours)

class MotorcycleFareCalculator(FareCalculator):
    def calculate_fare(self, hours: int) -> float:
        base_fare = base_fair[SpotType.SMALL]
        hourly_rate = 1.0
        return base_fare + (hourly_rate * hours)

class TruckFareCalculator(FareCalculator):
    def calculate_fare(self, hours: int) -> float:
        base_fare = base_fair[SpotType.LARGE]
        hourly_rate = 3.0
        return base_fare + (hourly_rate * hours)
    
class FareCalculatorFactory:
    @staticmethod
    def get_fare_calculator(spot_type: SpotType) -> FareCalculator:
        if spot_type == SpotType.SMALL:
            return MotorcycleFareCalculator()
        elif spot_type == SpotType.MEDIUM:
            return CarFareCalculator()
        elif spot_type == SpotType.LARGE:
            return TruckFareCalculator()
        else:
            raise ValueError("Invalid spot type")