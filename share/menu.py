"""Module for creating console menus.

This module provides a base class for building console-based menus using the
consolemenu package. It includes a decorator for easily adding methods as menu items.
"""

from consolemenu import ConsoleMenu
from consolemenu.items import FunctionItem

def menu_item(title):
    """
    Decorator for registering a method as a menu item.

    This decorator adds a title attribute to the method, which is used to create
    a menu item in the ConsoleMenu.

    Args:
        title (str): The title of the menu item.
    """
    def decorator(func):
        def wrapper(self, *args, **kwargs):
            return func(self, *args, **kwargs)
        wrapper._menu_title = title  # Storing the title in the function attributes
        return wrapper
    return decorator

class Menu:
    """
    Base class for creating a console menu.

    This class automates the creation of a menu with various items based on methods
    decorated with `menu_item`.

    Attributes:
        menu_registry (dict): Registry of menu items.
        menu (ConsoleMenu): Instance of ConsoleMenu.
    """

    def __init__(self, title=None, subtitle=None):
        """
        Initialize the menu with a title and subtitle.

        Args:
            title (str, optional): The title of the menu.
            subtitle (str, optional): The subtitle of the menu.
        """
        self.menu_registry = {}
        self.menu = ConsoleMenu(title=title, subtitle=subtitle)
        self._initialize_menu_items()

    def _initialize_menu_items(self):
        """
        Internal method to initialize menu items.

        This method goes through the attributes of the class, identifies methods
        decorated with `menu_item`, and adds them to the ConsoleMenu instance.
        """
        # Add registered methods as menu items with titles
        for attr_name in dir(self):
            attr = getattr(self, attr_name)
            if callable(attr) and hasattr(attr, '_menu_title'):
                menu_item_instance = FunctionItem(attr._menu_title, attr, menu=self.menu)
                self.menu.append_item(menu_item_instance)

    def show(self):
        """Display the menu to the user."""
        self.menu.show()
