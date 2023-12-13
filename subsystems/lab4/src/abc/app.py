from abc import ABC, abstractmethod
from .inputter import Inputter
from .outputter import Outputter
from ..geometry.figure import Figure
from ..geometry.rect import Rect

class App(ABC):
    def __init__(self, inputter: Inputter, outputter: Outputter) -> None:
        super().__init__()
        self.inputter = inputter
        self.outputter = outputter

    @abstractmethod
    def choose_figure(self) -> Figure:
        pass

    @abstractmethod
    def generate_art(self) -> str:
        pass

    @abstractmethod
    def run(self) -> None:
        pass
