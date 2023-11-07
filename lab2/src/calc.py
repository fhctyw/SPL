from ..tools import *
from ..components.operators import *
from ..components.user import User
from .menu import Menu

class Calculator(BaseProgram):
    def __init__(self) -> None:
        super().__init__()
        self.menu = Menu(self)
        self.users: list[User] = []
        self.operations: list[BaseOperator] = [PlusOperator(), MinusOperator(), MultOperator(), DivOperator()]
        
        self.current_user = None
        self.current_operation = None
            
        self.number1 = None
        self.number2 = None
            
        self.result = None

    @property
    def list_sign(self) -> str:
        return ", ".join([op.sign for op in self.operations]) if hasattr(self.operations, '__iter__') else self.operations[0]

    def input(self) -> None:
        self.menu.choose_option()

    def process(self) -> None:
        self.menu.do_option()

    def output(self) -> None:
        self.menu.show_menu()
        