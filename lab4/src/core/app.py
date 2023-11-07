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

    def choose_figure(self) -> Figure:
        idx, fig = self.inputter.choose("Choose figure", App.figures)
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
                break
        
        return figures

    def run(self) -> None:
        while True:
            figures: list[Figure] = self.generate_art()
            self.outputter.clear()
            for f in figures:
                f.display()
            
            if 'y' == self.inputter.get_symbol("Save art?(y/n): "):
                with open('art.txt', 'w') as file:
                    for f in figures:
                        file.write(str(f))    

            if 'n' == self.inputter.get_symbol('Continue create arts(y/n): '):
                break