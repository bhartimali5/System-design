## Test the code by creating parking lot & vehicles

from parking_lot.parking_lot import ParkingLot
from parking_lot.vehicle import VehicleType, Vehicle

if __name__ == "__main__":
    parking_lot = ParkingLot()

    # Create some vehicles
    car = Vehicle(VehicleType.CAR)
    motorcycle = Vehicle(VehicleType.MOTORCYCLE)
    truck = Vehicle(VehicleType.TRUCK)  

    # Check in vehicles
    car_ticket = parking_lot.checkin_vehicle(car)
    motorcycle_ticket = parking_lot.checkin_vehicle(motorcycle)
    truck_ticket = parking_lot.checkin_vehicle(truck)

    # Simulate some time passing (e.g., 2 hours)
    import time
    time.sleep(2 * 10)  # Sleep for 20 secs

    # Check out vehicles
    parking_lot.checkout_vehicle(car_ticket)
    parking_lot.checkout_vehicle(motorcycle_ticket)
    parking_lot.checkout_vehicle(truck_ticket)