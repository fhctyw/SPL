from .point import Point

class Rect:
    def __init__(self, x1=0, y1=0, x2=0, y2=0):
        self.top_left = Point(x1, y1)
        self.bottom_right = Point(x2, y2)

    def __repr__(self) -> str:
        return f"({self.top_left},{self.bottom_right})"
    