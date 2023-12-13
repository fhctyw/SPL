from .console_outputter import Outputter
from .color import Color
import sys
import os

class Graphic(Outputter):
    def __init__(self, width, height) -> None:
        super().__init__()
        
        self.width = width
        self.height = height

    def _move_cursor(self, x, y):
        """Move the terminal cursor to the specified (x, y) coordinates."""
        sys.stdout.write(f"\033[{y};{x}H")

    def _write_at_pos(self, x, y, text, color='transparent'):
        """Move the cursor to (x, y) and write the specified text."""
        self._move_cursor(x, y)
        print(Color.colored(text, color), end='', flush=True)
        self._move_cursor(1, y + 1)

    def clear(self):
        os.system("cls")

    def options(self, options: list[str]) -> None:
        return super().options(options)
    
    def text(self, text: str) -> None:
        return super().text(text)


