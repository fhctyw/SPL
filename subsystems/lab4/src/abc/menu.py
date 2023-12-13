from abc import ABC, abstractmethod
from .inputter import Inputter
from .outputter import Outputter

class Menu(ABC):
    def __init__(self, inputter: Inputter, outputter: Outputter) -> None:
        super().__init__()

        self.inputter = inputter
        self.outputter = outputter

    @abstractmethod
    def excecute(self):
        pass
    