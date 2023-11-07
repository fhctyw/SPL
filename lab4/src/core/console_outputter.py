from ..abc.outputter import Outputter
from ..geometry.figure import Figure

class ConsoleOutputter(Outputter):
    def text(self, text: str) -> None:
        print(text)

    def options(self, options: list[str]) -> None:
        print("Available options:")
        for option in options:
            print(option)

