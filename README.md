# python-iothub-cosmos

[![N|Azure Portal](https://github.com/eladtpro/python-iothub-cosmos/blob/main/.readme/azure-logo.png?raw=true)](https://ms.portal.azure.com/) [![N|Azure IoT Hub](https://github.com/eladtpro/python-iothub-cosmos/blob/main/.readme/iot-hub.png?raw=true)](https://azure.microsoft.com/en-us/services/iot-hub) [![N|CosmosDB](https://github.com/eladtpro/python-iothub-cosmos/blob/main/.readme/cosmos-db.png?raw=true)](https://azure.microsoft.com/en-us/services/cosmos-db) [![N|Python](https://github.com/eladtpro/python-iothub-cosmos/blob/main/.readme/python-logo.png?raw=true)](https://www.python.org/)

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

Python Azure IoT Hub event client &amp; subscriber with events stored in Cosmos DB
In this sample we will:
  - Create Azure IoT hub.
  - Create Azure Cosmos DB single instance.
  - Build Python sample code that will create random events and send then to the IoT hub as client device.
  - Build another python module that will read the events from the hub and store them in Cosmos DB.

$~$

## Creating Azure artifacts
 using the Azure CLI
 
### Create an Azure IoT Hub
1. create a resource group:
```sh
az group create --name {resource group name} --location westeurope
```
2. create an IoT hub:
```sh
az iot hub create --name {iot hub name} --resource-group {resource group name} --sku S1
```
### Register a device
3. create the device identity:
```sh
az iot hub device-identity create --hub-name {iot hub name} --device-id {chosen device name}
```
4. get the device connection string for the device you registered:
```sh
az iot hub device-identity connection-string show --hub-name {iot hub name} --device-id {chosen device name} --output table
```
> Make a note of the device connection string, which looks like:
> HostName={iot hub name}.azure-devices.net;DeviceId={chosen device name};SharedAccessKey={YourSharedAccessKey}

5. You also need the Event Hubs-compatible [endpoint], Event Hubs-compatible [path], and service [primary key] from your IoT hub
```sh
az iot hub show --query properties.eventHubEndpoints.events.endpoint --name {iot hub name}
az iot hub show --query properties.eventHubEndpoints.events.path --name {iot hub name}
az iot hub policy show --name service --query primaryKey --hub-name {iot hub name}
```


### Create Cosmos DB

6. Create Cosmos DB client instance:
```sh
az cosmosdb create \
    --name {cosmos db account name} \
    --resource-group {resource group name} \
    --default-consistency-level Session \
    --locations regionName=westeurope failoverPriority=0 isZoneRedundant=False \
    --locations regionName=easteurope failoverPriority=1 isZoneRedundant=False
```

7. Create database:
>check deprecated:
>This command has been deprecated and will be removed in a future release. Use 'cosmosdb sql database, cosmosdb mongodb database, cosmosdb cassandra keyspace or cosmosdb gremlin database' instead.
```sh
az cosmosdb gremlin database create --name {database name} --account-name {cosmos db account name} --resource-group {resource group name}
```


8. Create containers:
```sh
az cosmosdb sql container create --resource-group {resource group name} --account {cosmos db account name} \ 
--database-name MyDatabase -n MyContainer --partition-key-path "/my/path" --idx @policy-file.json --ttl 1000 --throughput "700"
```

$~$

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


### Python Configuration File (.ini)
create [.ini] file with the kes extracted from the two last azure shell command - [connectionstring], [endpoint], [path], and [primary key]:
```ini
[default]
port=80
[iot]
connectionstring={connectionstring}
endpoint={endpoint}
path={path}
primarykey={primary key}
deviceid={chosen device name}
```

$~$

## Running the simulation

first - running client device simulation:
```python
python3 iot.py --mode run
```


next (while the client is running) and sending *simulated telemetry* - initiate the IoT hub consumer part:
```python
python3 iot.py --mode listen
```

***

$~$

$~$



### External Links
The solution based on external resources:

* [Azure CLI: Create an IoT hub] - How to create an IoT hub using Azure CLI.
* [Azure CLI: Create and manage Cosmos DB] - Common commands to automate management of your Azure Cosmos DB accounts
* [Python: Send telemetry to IoT hub] - Send telemetry from a device to an IoT hub and read it with a back-end application (Python)
* [Python: Cosmos DB read and write data] - Create and manage an Azure Cosmos DB SQL API account from the Azure portal, and from Visual Studio Code with a Python app.
* [Windows Subsystem for Linux Installation Guide for Windows 10] - installing Windows Subsystem for Linux (WSL).
* [configparser] - Handling Configuration Files in Python.


### Tools

Useful tooling

| Tool | Reference |
| ------ | ------ |
| *Azure (Portal)* | https://azure.microsoft.com/en-us/features/azure-portal |
| *python* | https://www.python.org/downloads |
| *Visual Studio Code* | https://code.visualstudio.com/download |
| *Windows Terminal* | https://docs.microsoft.com/en-us/windows/terminal/get-started |

License
----

MIT


**Elad Tal (CE @ Microsoft)**

[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)


   [Azure CLI: Create an IoT hub]: <https://docs.microsoft.com/en-us/azure/iot-hub/iot-hub-create-using-cli>
   [Azure CLI: Create and manage Cosmos DB]: <https://docs.microsoft.com/en-us/azure/cosmos-db/manage-with-cli>
   [Python: Send telemetry to IoT hub]: <https://docs.microsoft.com/en-us/azure/iot-hub/quickstart-send-telemetry-python>
   [Python: Cosmos DB read and write data]:<https://docs.microsoft.com/en-us/azure/cosmos-db/create-sql-api-python>
   [Windows Subsystem for Linux Installation Guide for Windows 10]:<https://docs.microsoft.com/en-us/windows/wsl/install-win10>
   [configparser]: <https://docs.python.org/3/library/configparser.html>
