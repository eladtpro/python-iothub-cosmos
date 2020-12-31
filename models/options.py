from enum import Enum

RUN = 'run'
LISTEN = 'listen'
READ = 'read'
CLEAR = 'clear'
ASYNC = 'async'


class Mode(Enum):
    RUN = 1
    LISTEN = 2
    READ = 4
    CLEAR = 8


class Options:
    def __init__(self):
        self.mode = Mode.RUN
        self.async = False
        self.save = False
        self.print = False

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)
