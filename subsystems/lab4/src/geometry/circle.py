from .point import Point
from .rect import Rect
from .figure import Figure
from ..core.graphic import Graphic
from ..abc.inputter import Inputter

import math

class Circle(Figure):
    def __init__(self, inputter: Inputter, graphic: Graphic, center: Point = Point(0, 0), radius: int = 0, color: str='white', symbol: str='*'):
        super().__init__(inputter, graphic, color, symbol, Rect(center.x - radius, center.y - radius, center.x + radius, center.y + radius))

    def input(self) -> None:
        super().input()
        x = self.inputter.get_number("Enter center x: ")
        y = self.inputter.get_number("Enter center y: ")

        p = Point(x, y)

        r = self.inputter.get_number("Enter radius: ")
        self.rect = Rect(p.x - r, p.y - r, p.x + r, p.y + r)

    def display(self) -> None:
            # Determine aspect ratio for terminal characters (typically characters are about twice as high as they are wide)
            aspect_ratio = 2
            center_x = (self.rect.top_left.x + self.rect.bottom_right.x) // 2
            center_y = (self.rect.top_left.y + self.rect.bottom_right.y) // 2

            radius = (self.rect.bottom_right.x - self.rect.top_left.x) // 2

            for degree in range(360):
                radian = math.radians(degree)
                x_offset = int(radius * math.cos(radian))
                y_offset = int(radius * math.sin(radian) / aspect_ratio)
                
                # Calculate the actual x and y coordinates
                x = center_x + x_offset
                y = center_y + y_offset

                # Check if the point is within the bounds of the graphic
                if 0 <= x < self.graphic.width and 0 <= y < self.graphic.height:
                    self.graphic._write_at_pos(x, y, self.symbol, self.color)
                
            
            self.graphic._move_cursor(0, self.graphic.height - 1)

    def __repr__(self) -> str:
        center_x = (self.rect.top_left.x + self.rect.bottom_right.x) // 2
        center_y = (self.rect.top_left.y + self.rect.bottom_right.y) // 2

        radius = (self.rect.bottom_right.x - self.rect.top_left.x) // 2

        return f"[{center_x},{center_y},{radius}]{super().__repr__()}"
