#!/usr/bin/python

from getopt import getopt, GetoptError
from sys import exit
from models.options import Options, Mode, RUN, LISTEN, READ

COMMAND_LINE = 'iot.py --mode<-m> run\\listen [--async<-a>] [--save<-s>] [--read<-r>]'


def extract(argv):
    options = Options()

    try:
        opts, args = getopt(argv, 'hasm:', ['help', 'async', 'save', 'mode='])
    except GetoptError:
        print(f'Command {argv} not found.')
        print(COMMAND_LINE)
        exit(2)
    for opt, arg in opts:
        if opt == '-h' or opt == '--help':
            print(COMMAND_LINE)
            exit()
        elif opt in ("-m", "--mode"):
            mode = arg.replace('=', '')
            if mode not in (RUN, LISTEN, READ):
                print(f'Missing or invalid required argument mode. {args}')
                print(COMMAND_LINE)
                exit(1)
            elif RUN == mode:
                options.mode = Mode.RUN 
            elif LISTEN == mode:
                options.mode = Mode.LISTEN
            elif READ == mode:
                options.mode = Mode.READ

        elif opt in ("-a", "--async"):
            options.async = True
        elif opt in ("-s", "--save"):
            options.save = True

    print(f'options: [{options}]')
    return options
