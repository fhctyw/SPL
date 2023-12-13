import math

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def distance(self, other_point):
        return math.sqrt((self.x - other_point.x)**2 + (self.y - other_point.y)**2)

    def __repr__(self):
        return f"({self.x}, {self.y})"
