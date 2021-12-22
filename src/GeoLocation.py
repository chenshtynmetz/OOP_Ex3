import math


class GeoLocation:

    def __init__(self, location: tuple = None):
        pos = location.split(",")
        self.x = pos[0]
        self.y = pos[1]
        self.z = pos[2]

    def distance(self, other):
        x_pow = math.pow(self.x - other.x)
        y_pow = math.pow(self.y - other.y)
        z_pow = math.pow(self.z - other.z)
        return math.sqrt(x_pow + y_pow + z_pow)
