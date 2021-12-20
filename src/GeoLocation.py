import math


class GeoLocation(tuple):

    def __init__(self, location: tuple = None):
        self.x = location[0]
        self.y = location[1]
        self.z = location[2]

    def distance(self, other):
        x_pow = math.pow(self.x - other.x)
        y_pow = math.pow(self.y - other.y)
        z_pow = math.pow(self.z - other.z)
        return math.sqrt(x_pow + y_pow + z_pow)
