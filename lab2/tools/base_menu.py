from .base_program import BaseProgram
from abc import ABC, abstractmethod
from typing import Callable
from collections import deque

class BaseMenu(ABC):
    class Option:
        def __init__(self, func: Callable[['BaseMenu', BaseProgram], None], name: str = None) -> None:
            self.func: Callable[['BaseMenu', BaseProgram], None] = func
            self.name: str = name if name else func.__name__

    class _NodeOptions:
        def __init__(self, currents: list['BaseMenu.Option'], prev: 'BaseMenu._NodeOptions', next: list['BaseMenu._NodeOptions']) -> None:
            self.currents: list[BaseMenu.Option] = currents
            self.prev: BaseMenu._NodeOptions = prev
            self.next: list[BaseMenu._NodeOptions] = next

    def __init__(self, program: BaseProgram) -> None:
        super().__init__()
        self._program = program

        self.__node_options = self._NodeOptions(None, None, None)
        self.__option_index: int = None

        self.__maked_choice = False

    @property
    def __options(self) -> list[Option]:
        return self.__node_options.currents

    @property
    def __chosen_option(self) -> Option:
        return self.__options[self.__option_index]
    
    @property
    def _is_prev(self) -> bool:
        return self.__node_options.prev != None

    @property
    def _is_next(self) -> bool:
        return self.__node_options.next != None \
            and self.__option_index >= 0 and self.__option_index < len(self.__node_options.next) \
            and self.__node_options.next[self.__option_index] != None

    def _go_prev(self) -> None:
        if self._is_prev:
            self.__node_options = self.__node_options.prev

    def _go_next(self) -> None:
       if self._is_next and self.__maked_choice:
           self.__node_options = self.__node_options.next[self.__option_index]
           self.__maked_choice = False

    def add_option(self, option: Option, route: str = '') -> None:
        node = self.__node_options
        if route == '':
            if node.currents == None:
                node.currents: list[BaseMenu.Option] = []
            node.currents.append(option)
        else:
            routes = list(map(int, route.split()))
            if node.next == None:
                node.next: list[BaseMenu._NodeOptions] = [None] * 2
            for r in routes:
                if len(node.next) <= r:
                    node.next.extend([None] * 2 * len(node.next))
                if node.next[r] == None:
                    node.next[r] = BaseMenu._NodeOptions([option], node, None)
                else:
                    node.next[r].currents.append(option)
                node = node.next

    def _get_menu(self) -> list[Option]:
        return self.__options

    def _make_choice(self, index: int) -> None:
        self.__option_index = index 
        self.__maked_choice = True

    def _execute_option(self):
        self.__chosen_option.func(self, self._program)