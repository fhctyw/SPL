from .src.core.app import App
from .src.core.console_inputter import ConsoleInputter
from .src.core.graphic import Graphic
import os

def main():
    inputter = ConsoleInputter()
    size = os.get_terminal_size() 
    outputter = Graphic(size.columns, size.lines)

    app = App(inputter, outputter)
    app.run()

if __name__ == '__main__':
    main()