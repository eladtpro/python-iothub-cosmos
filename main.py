# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project root for full license information.

import configparser
import argparse
from types import SimpleNamespace
from simulateddevice import run
from hublistener import listen

RUN = 'run'
LISTEN = 'listen'


def bootstrap():
    configuration = configparser.ConfigParser()
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


def main(mode):
	config = bootstrap()

	if mode == RUN:
		run(config)
	elif mode == LISTEN:
		listen(config)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--mode')
    args = parser.parse_args()

    if args.mode is not None and args.mode in (RUN, LISTEN):
        main(args.mode)
    else:
        raise ValueError(
            f'argument --mode can be set to `{RUN}` or `{LISTEN}` only')
