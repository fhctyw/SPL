class User:
    def __init__(self, name: str, float_precision: int) -> None:
        self.name: str = name
        self.history: list[str] = []
        self.memory: list[float] = []
        self.float_precision = float_precision