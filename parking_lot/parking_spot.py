import uuid

class ParkingSpot:
    def __init__(self, floor_number, spot_type):
        self.spot_id = str(uuid.uuid4()) 
        self.floor_number = floor_number  # This will be set when the spot is added to a floor
        self.spot_type = spot_type
        self.occupied = False

    def is_available(self):
        return not self.occupied

    def occupy(self):
        if self.is_available():
            self.occupied = True
            return True
        return False

    def vacate(self):
        if not self.is_available():
            self.occupied = False
            return True
        return False    