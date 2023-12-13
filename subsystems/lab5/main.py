from .engine import Engine
from .math import Vector3D
import os

def main():
    size = os.get_terminal_size()

    engine = Engine(size.columns, size.lines)

    engine.camera.position = Vector3D(0, 0, -5)

    engine.run()

