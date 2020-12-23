# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project root for full license information.
from configparser import ConfigParser

class Configuration:

    #@staticmethod
    def __init__(self):
        configuration = ConfigParser()
        configuration.read('.ini')

        # iot
        self.port = configuration['default'].getint('port')
        self.deviceid = configuration['iot']['deviceid']
        self.connectionstring = configuration['iot']['connectionstring']
        self.endpoint = configuration['iot']['endpoint']
        self.path = configuration['iot']['path']
        self.primarykey = configuration['iot']['primarykey']
        # cosmosdb
        self.cosmos_endpoint = configuration['cosmosdb']['endpoint']
        self.cosmos_primarykey = configuration['cosmosdb']['primarykey']
        self.database = configuration['cosmosdb']['database']
        self.container = configuration['cosmosdb']['container']
