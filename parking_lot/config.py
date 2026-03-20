
from .spot_type import SpotType

base_fair  = {
    SpotType.SMALL: 5.0,
    SpotType.MEDIUM: 2.0,
    SpotType.LARGE: 10.0
}

default_parking_capacity = {
    SpotType.SMALL: 5,
    SpotType.MEDIUM: 3,
    SpotType.LARGE  : 2
}

default_parking_floors = 3