#!/usr/bin/python

from getopt import getopt, GetoptError
from types import SimpleNamespace
from sys import exit
from constants import RUN, LISTEN, COMMAND_LINE

def extract(argv):
    options = SimpleNamespace(
        mode='',
        async=False)

    try:
        opts, args = getopt(argv, 'ham:', ['help', 'async', 'mode='])
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
            if mode not in (RUN, LISTEN):
                print(f'Missing or invalid required argument mode. {args}')
                print(COMMAND_LINE)
                exit(1)
            else:
                options.mode=mode
        elif opt in ("-a", "--async"):
            options.async = True

    print(f'options: [{options}]')
    return options
