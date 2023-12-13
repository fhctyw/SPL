from consolemenu.validators.base import BaseValidator
from termcolor import COLORS

class ColorValidator(BaseValidator):
    def __init__(self) -> None:
        super().__init__()
    
    def validate(self, input_string: str) -> bool:
        return input_string in list(COLORS.keys())