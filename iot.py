# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project root for full license information.

from simulateddevice import run
from sys import argv
from utils.args import extract
from models.options import RUN, LISTEN
from hublistener import listen, listenasync
from models.configuration import Configuration

def main(options):
    config = Configuration()

    if RUN == options.mode:
        run(config)
    elif LISTEN == options.mode:
        if options.async == True:
            listenasync(config)
        else: 
            listen(config)

if __name__ == '__main__':
    options = extract(argv[1:])
    main(options)
