from ..abc.inputter import Inputter
from .rect import Rect
from .figure import Figure
from ..core.graphic import Graphic

class Rectangle(Figure):
    def __init__(self, inputter: Inputter, graphic: Graphic, rect: Rect = ..., color: str = 'white', symbol: str = '*') -> None:
        super().__init__(inputter, graphic, rect, color, symbol)

    def input(self) -> None:
        super().input()

        x1 = self.inputter.get_number("Enter x1: ")
        y1 = self.inputter.get_number("Enter y1: ")

        x2 = self.inputter.get_number("Enter x2: ")
        y2 = self.inputter.get_number("Enter y2: ")

        self.rect = Rect(x1, y1, x2, y2)

    def display(self) -> None:
        # Draw the top and bottom horizontal lines
        for x in range(self.rect.top_left.x, self.rect.bottom_right.x + 1):
            self.graphic._write_at_pos(x, self.rect.top_left.y, self.symbol, self.color)
            self.graphic._write_at_pos(x, self.rect.bottom_right.y, self.symbol, self.color)

        # Draw the left and right vertical lines
        for y in range(self.rect.top_left.y + 1, self.rect.bottom_right.y):  # +1 and -1 to avoid double-drawing corners
            self.graphic._write_at_pos(self.rect.top_left.x, y, self.symbol, self.color)
            self.graphic._write_at_pos(self.rect.bottom_right.x, y, self.symbol, self.color)

        self.graphic._move_cursor(0, self.graphic.height - 1)

    def __repr__(self) -> str:
        return super().__repr__()
 