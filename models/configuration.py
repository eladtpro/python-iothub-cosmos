# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project root for full license information.
from configparser import ConfigParser

class IoT:
    def __init__(self, configuration):
        self.port = configuration['default'].getint('port')
        self.deviceid = configuration['iot']['deviceid']
        self.connectionstring = configuration['iot']['connectionstring']
        self.endpoint = configuration['iot']['endpoint']
        self.path = configuration['iot']['path']
        self.primarykey = configuration['iot']['primarykey']

class Cosmos:
    def __init__(self, configuration):
        self.endpoint = configuration['cosmosdb']['endpoint']
        self.primarykey = configuration['cosmosdb']['primarykey']
        self.database = configuration['cosmosdb']['database']
        self.container = configuration['cosmosdb']['container']
        self.path = configuration['cosmosdb']['path']
        self.throughput = configuration['cosmosdb']['throughput']


class Configuration():
    def __init__(self):
        config = ConfigParser()
        config.read('.ini')
        self.iot = IoT(config)
        self.cosmos = Cosmos(config)

#    @staticmethod
#    def init():
#        configuration = ConfigParser()
#        configuration.read('.ini')
#        if(Configuration.iot is None):
#            Configuration.iot = IoT(configuration)
#        if(Configuration.cosmos is None):
#            Configuration.cosmos = Cosmos(configuration)


#Configuration.init()
