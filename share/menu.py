"""Required classes from "console-menu"""
from consolemenu import ConsoleMenu
from consolemenu.items import FunctionItem

# Decorator to register a method as a menu item
def menu_item(title):
    def decorator(func):
        def wrapper(self, *args, **kwargs):
            return func(self, *args, **kwargs)
        wrapper._menu_title = title  # Storing the title in the function attributes
        return wrapper
    return decorator

class Menu:
    """Menu Base class"""
    def __init__(self, title=None, subtitle=None):
        self.menu_registry = {}
        self.menu = ConsoleMenu(title=title, subtitle=subtitle)
        self._initialize_menu_items()

    def _initialize_menu_items(self):
        # Add registered methods as menu items with titles
        for attr_name in dir(self):
            attr = getattr(self, attr_name)
            if callable(attr) and hasattr(attr, '_menu_title'):
                menu_item_instance = FunctionItem(attr._menu_title, attr, menu=self.menu)
                self.menu.append_item(menu_item_instance)

    def show(self):
        """Show the menu"""
        self.menu.show()
        