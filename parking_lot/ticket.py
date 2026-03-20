import uuid
from datetime import datetime


class Ticket:
    def __init__(self, vehicle, spot, checkin_time):
        self.ticket_id = str(uuid.uuid4())
        self.vehicle = vehicle
        self.spot = spot
        self.checkin_time = checkin_time
        self.checkout_time = None
        self.fare = None


