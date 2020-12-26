from enum import Enum

RUN = 'run'
LISTEN = 'listen'
READ = 'read'
ASYNC = 'async'


class Mode(Enum):
    RUN = 1
    LISTEN = 2
    READ = 4


class Options:
    def __init__(self):
        self.mode = Mode.RUN
        self.async = False
        self.save = False
