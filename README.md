# python-iothub-cosmos

[![N|Azure Portal](https://github.com/eladtpro/python-iothub-cosmos/blob/main/.readme/azure-logo.png?raw=true)](https://ms.portal.azure.com/) [![N|Azure IoT Hub](https://github.com/eladtpro/python-iothub-cosmos/blob/main/.readme/iot-hub.png?raw=true)](https://azure.microsoft.com/en-us/services/iot-hub) [![N|CosmosDB](https://github.com/eladtpro/python-iothub-cosmos/blob/main/.readme/cosmos-db.png?raw=true)](https://azure.microsoft.com/en-us/services/cosmos-db) [![N|Python](https://github.com/eladtpro/python-iothub-cosmos/blob/main/.readme/python-logo.png?raw=true)](https://www.python.org/)

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

Python Azure IoT Hub event client &amp; subscriber with events stored in Cosmos DB
In this sample we will:
  - Create Azure IoT hub.
  - Create Azure Cosmos DB single instance.
  - Build Python sample code that will create random events and send then to the IoT hub as client device.
  - Build another python module that will read the events from the hub and store them in Cosmos DB.

## Creating Azure artifacts
 using the Azure CLI
 
### Create an Azure IoT Hub
1. create a resource group:
```sh
az group create --name {your resource group name} --location westus
```
2. create an IoT hub:
```sh
az iot hub create --name {your iot hub name} --resource-group {your resource group name} --sku S1
```
### Register a device
3. create the device identity:
```sh
az iot hub device-identity create --hub-name {your iot hub name} --device-id {your chosen device name}
```
4. get the device connection string for the device you registered:
```sh
az iot hub device-identity connection-string show --hub-name {your iot hub name} --device-id {your chosen device name} --output table
```
> Make a note of the device connection string, which looks like:
> HostName={your iot hub name}.azure-devices.net;DeviceId={your chosen device name};SharedAccessKey={YourSharedAccessKey}

5. You also need the Event Hubs-compatible [endpoint], Event Hubs-compatible [path], and service [primary key] from your IoT hub
```sh
az iot hub show --query properties.eventHubEndpoints.events.endpoint --name {your iot hub name}
az iot hub show --query properties.eventHubEndpoints.events.path --name {your iot hub name}
az iot hub policy show --name service --query primaryKey --hub-name {your iot hub name}
```

## Local Environment

### Prepring VSCode
using ubuntu shell

1. if not already exists - install pip (standard package manager for python):
```sh
apt-get install python3-pip
apt-get install pythonpy
```
2. install the required azure iot library for the simulated device application:
```sh
pip3 install azure-iot-device
```

3. install the required azure event hub library for the backend application:
```sh
pip3 install azure-eventhub
```


### Configuration
create [.ini] file with the kes extracted from the two last azure shell command - [connectionstring], [endpoint], [path], and [primary key]:
```ini
[default]
port=80
[iot]
connectionstring={your connectionstring}
endpoint={your endpoint}
path={your path}
primarykey={your primary key}
deviceid={your chosen device name}
```


## Running the code

running client simulation
```python
python3 main.py --mode run
```


### External Links
The solution based on external resources:

* [Create an IoT hub using the Azure CLI] - How to create an IoT hub using Azure CLI.
* [Send Telemetry with Python] - Send telemetry from a device to an IoT hub and read it with a back-end application (Python)
* [configparser] - Handling Configuration Files in Python.




Markdown is a lightweight markup language based on the formatting conventions that people naturally use in email.  As [John Gruber] writes on the [Markdown site][df1]

> The overriding design goal for Markdown's
> formatting syntax is to make it as readable
> as possible. The idea is that a
> Markdown-formatted document should be
> publishable as-is, as plain text, without
> looking like it's been marked up with tags
> or formatting instructions.

This text you see here is *actually* written in Markdown! To get a feel for Markdown's syntax, type some text into the left window and watch the results in the right.


### Installation

Dillinger requires [Node.js](https://nodejs.org/) v4+ to run.

Install the dependencies and devDependencies and start the server.

```sh
$ cd dillinger
$ npm install -d
$ node app
```

For production environments...

```sh
$ npm install --production
$ NODE_ENV=production node app
```

### Tools

Useful tooling

| Plugin | Installation |
| ------ | ------ |
| Azure Portal | https://azure.microsoft.com/en-us/features/azure-portal/ |
| python | https://www.python.org/downloads |
| Visual Studio Code | https://code.visualstudio.com/download |
| Windows Terminal | https://docs.microsoft.com/en-us/windows/terminal/get-started |

License
----

MIT


**Elad Tal (CE @ Microsoft)**

[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)


   [Create an IoT hub using the Azure CLI]: <https://docs.microsoft.com/en-us/azure/iot-hub/iot-hub-create-using-cli>
   [Send Telemetry with Python]: <https://docs.microsoft.com/en-us/azure/iot-hub/quickstart-send-telemetry-python>
   [configparser]: <https://docs.python.org/3/library/configparser.html>
