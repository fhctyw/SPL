from tools.base_program import BaseProgram
from tools.base_menu import BaseMenu

class Menu(BaseMenu):
    def __init__(self, program: BaseProgram) -> None:
        super().__init__(program)
        self.choice: int = -1

    def show_menu(self):
        for index, option in enumerate(self._get_menu()):
            print(f'{index + 1} {option.name}')
        print(f'0 {"Back" if self._is_prev else "Exit"}')

    def choose_option(self):
        self.choice = int(input(f'Enter choice(0-{len(self._get_menu())}): '))
        print()

    def do_option(self):
        if self.choice == 0:
            if self._is_prev:
                self._go_prev()
            else:
                self._program.running = False
        elif self.choice - 1 < len(self._get_menu()) and self.choice - 1 >= 0:
            self.choice -= 1
            self._make_choice(self.choice)
            self._execute_option()
            self._go_next()
        