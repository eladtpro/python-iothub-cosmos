# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project root for full license information.

from sys import argv
from utils.args import extract
from simulateddevice import run
from hublistener import listen
from models.configuration import Configuration
from models.options import Mode
from cosmos import read, clear

def main(options):
    config = Configuration()

    if Mode.RUN == options.mode:
        run(config)
    elif Mode.LISTEN == options.mode:
        listen(config, options)
    elif Mode.READ == options.mode:
        read(config, options.print)
    elif Mode.CLEAR == options.mode:
        clear(config)

if __name__ == '__main__':
    options = extract(argv[1:])
    main(options)
