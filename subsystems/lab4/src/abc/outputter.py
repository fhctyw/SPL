from abc import ABC, abstractmethod

class Outputter(ABC):
    @abstractmethod
    def text(self, text: str) -> None:
        pass

    @abstractmethod
    def options(self, options: list[str]) -> None:
        pass


