from .abc_console_output import AbstractConsoleOutput

class ConsoleOutput(AbstractConsoleOutput):
    def output(self, message):
        print(message)