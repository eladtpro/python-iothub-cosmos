# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project root for full license information.

from configparser import ConfigParser
from types import SimpleNamespace
from simulateddevice import run
from sys import argv
from args import extract
from constants import RUN, LISTEN
from hublistener import listen, listenasync

def bootstrap():
    configuration = ConfigParser()
    configuration.read('.ini')
    config = SimpleNamespace(
        # iot
        port=configuration['default'].getint('port'),
        deviceid=configuration['iot']['deviceid'],
        connectionstring=configuration['iot']['connectionstring'],
        endpoint=configuration['iot']['endpoint'],
        path=configuration['iot']['path'],
        primarykey=configuration['iot']['primarykey'])
    return config


def main(options):
    config = bootstrap()

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
