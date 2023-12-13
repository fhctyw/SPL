import logging

from share.file_io.file import FileIO

from ..geometry.figure import Figure
from ..geometry.rect import Rect
from ..geometry.rectangle import Rectangle
from ..geometry.circle import Circle
from ..abc.inputter import Inputter
from ..abc.outputter import Outputter
from ..abc.app import App

class App(App):
    figures = ['Rectangle', 'Circle']
    def __init__(self, inputter: Inputter, outputter: Outputter) -> None:
        super().__init__(inputter, outputter)
        logging.info("App initialized")


    def choose_figure(self) -> Figure:
        idx, fig = self.inputter.choose("Choose figure", App.figures)
        logging.info("Figure chosen: %s", fig)
        match fig:
            case 'Rectangle':
                rect = Rectangle(self.inputter, self.outputter)
                rect.input()
                return rect
            case 'Circle':
                circle = Circle(self.inputter, self.outputter)
                circle.input()
                return circle

    def generate_art(self) -> list[Figure]:
        figures: list[Figure] = []
        while True:
            figure = self.choose_figure()
            figures.append(figure)
            self.outputter.clear()
            for f in figures:
                f.display()
            if 'n' == self.inputter.get_symbol('Continue create figure(y/n): '):
                logging.info("Exiting figure creation")
                break
        
        return figures

    def run(self) -> None:
        while True:
            logging.info("Generating art")
            figures: list[Figure] = self.generate_art()
            self.outputter.clear()
            for f in figures:
                f.display()
            
            if 'y' == self.inputter.get_symbol("Save art?(y/n): "):
                strFigures = ''
                for f in figures:
                    s += str(f) + '\n\r' 
                file = FileIO()
                file.write_file("data/lab4/art.txt", strFigures)

            if 'n' == self.inputter.get_symbol('Continue create arts(y/n): '):
                logging.info("Exiting art creation")
                break