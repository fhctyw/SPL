from ..abc.inputter import Inputter

class ConsoleInputter(Inputter):
    def get_text(self, prompt: str) -> str:
        return input(prompt)

    def choose(self, prompt: str, choices: list[str]) -> (int, str):
        print(prompt)
        for i, choice in enumerate(choices):
            print(f"{i}. {choice}")
        index = int(input("Your choice: "))
        return index, choices[index]

    def get_symbol(self, prompt: str) -> str:
        return input(prompt)

    def get_number(self, prompt: str) -> int:
        return int(input(prompt))
