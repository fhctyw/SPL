from abc import ABC, abstractmethod

class BaseProgram(ABC):
    def __init__(self) -> None:
        super().__init__()
        self.running: bool = True

    @abstractmethod
    def input(self) -> None:
        pass

    @abstractmethod
    def process(self) -> None:
        pass
    
    @abstractmethod
    def output(self) -> None:
        pass
    
    def run(self) -> None:
        while self.running:
            self.output()
            self.input()
            self.process()