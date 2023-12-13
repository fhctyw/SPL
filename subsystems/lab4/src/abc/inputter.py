from abc import ABC, abstractmethod

class Inputter(ABC):
    @abstractmethod
    def get_text(self, prompt: str) -> str:
        pass

    @abstractmethod
    def choose(self, prompt: str, choises: list[str]) -> (int, str):
        pass

    @abstractmethod
    def get_symbol(self, prompt: str) -> str:
        pass

    @abstractmethod
    def get_number(self, prompt: str) -> int:
        pass