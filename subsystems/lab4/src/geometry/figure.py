from abc import ABC, abstractmethod
from .rect import Rect
from ..abc.outputter import Outputter
from ..abc.inputter import Inputter
from ..core.color import Color

class Figure(ABC):
    @abstractmethod
    def __init__(self, inputter: Inputter, graphic:Outputter, rect: Rect = Rect(0, 0, 0, 0), color: str='white', symbol: str='*') -> None:
        super().__init__()
        self.inputter = inputter
        self.graphic = graphic

        self.rect = rect
        self.color = color
        self.symbol = symbol

    @abstractmethod
    def display(self) -> None:
        pass

    def input(self) -> None:
        idx, color = self.inputter.choose("Choose color", Color.color_list)
        self.color = color
        self.symbol = self.inputter.get_symbol("Enter symbol: ")
    
    @abstractmethod
    def __repr__(self) -> str:
        return f"[{self.color,self.symbol,self.rect}]"
    
    def __str__(self) -> str:
        return self.__repr__()