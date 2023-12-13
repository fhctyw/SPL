from ..abc.inputter import Inputter
from ..abc.outputter import Outputter
from ..abc.menu import Menu
from .menu_item import MenuItem

class Menu(Menu):
    def __init__(self, inputter: Inputter, outputter: Outputter) -> None:
        super().__init__(inputter, outputter)

        self.root = MenuItem("Root")
        # self.add("Exit", lambda: print('EXIT PROGRAM'))

    def add(self, name: str, action=None):
        return self.root.add(name, action)

    def __getitem__(self, key: str):
        return self.root[key]

    def display_options(self, menu_item: MenuItem):
        options = list(menu_item.sub_menu.keys())
        #self.outputter.options(options)
        index, choice = self.inputter.choose("Please choose an option:", options)
        return choice

    def excecute(self, menu_item=None):
        if menu_item is None:
            menu_item = self.root

        while True:
            choice = self.display_options(menu_item)
            selected_item: MenuItem = menu_item[choice]

            selected_item.execute()

            if selected_item.sub_menu:
                self.excecute(selected_item)
                break





