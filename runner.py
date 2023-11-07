from consolemenu import *
from consolemenu.console_menu import ConsoleMenu
from consolemenu.items import *

import lab1.main
import lab2.main
import lab3.main
import lab4.main
#import lab5.main
import lab6.main
import lab7.main


def main():
    menu = ConsoleMenu("Runner")
    menu.append_item(FunctionItem("Calculator", lab1.main.main))
    menu.append_item(FunctionItem("OOP Calculator", lab2.main.main))
    menu.append_item(FunctionItem("ASCII Art", lab3.main.main))
    menu.append_item(FunctionItem("2D ASCII Art without additional libraries", lab4.main.main))
    #menu.append_item(FunctionItem("3D ASCII Arts", lab5.main.main))
    menu.append_item(FunctionItem("Unit tests", lab6.main.main))
    menu.append_item(FunctionItem("API requests", lab7.main.main))

    menu.show()

if '__main__' == __name__:
    main()