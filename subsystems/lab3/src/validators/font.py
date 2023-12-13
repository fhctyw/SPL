from consolemenu.validators.base import BaseValidator
from art.art_param import FONT_NAMES

class FontValidator(BaseValidator):
    def __init__(self) -> None:
        super().__init__()

    def validate(self, input_string: str) -> bool:
        return input_string in FONT_NAMES