# python-iothub-cosmos

[![N|Azure Portal](https://github.com/eladtpro/python-iothub-cosmos/blob/main/.readme/azure-logo.png?raw=true)](https://ms.portal.azure.com/) [![N|Azure IoT Hub](https://github.com/eladtpro/python-iothub-cosmos/blob/main/.readme/iot-hub.png?raw=true)](https://azure.microsoft.com/en-us/services/iot-hub) [![N|CosmosDB](https://github.com/eladtpro/python-iothub-cosmos/blob/main/.readme/cosmos-db.png?raw=true)](https://azure.microsoft.com/en-us/services/cosmos-db) [![N|Python](https://github.com/eladtpro/python-iothub-cosmos/blob/main/.readme/python-logo.png?raw=true)](https://www.python.org/)

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

Python Azure IoT Hub event client &amp; subscriber with events stored in Cosmos DB
In this sample we will:
  - Create Azure IoT hub.
  - Create Azure Cosmos DB single instance.
  - Build Python sample code that will create random events and send then to the IoT hub as client device.
  - Build another python module that will read the events from the hub and store them in Cosmos DB.



### Creating Azure artifacts
Using the Azure CLI
 
#### Create an Azure IoT Hub
1. create a resource group:
```sh
az group create --name {resource group name} --location westeurope
```
2. create an IoT hub:
```sh
az iot hub create --name {iot hub name} --resource-group {resource group name} --sku S1
```
#### Client Device Registration
3. create the device identity:
```sh
az iot hub device-identity create --hub-name {iot hub name} --device-id {device identifier}
```
4. Get the IoT device connection string for the device you registered:
```sh
az iot hub device-identity connection-string show --hub-name {iot hub name} --device-id {device identifier} --output table
```
> Make a note of the device connection string, which looks like:
> HostName={iot hub name}.azure-devices.net;DeviceId={device identifier};SharedAccessKey={YourSharedAccessKey}

5. You also need the Event Hubs-compatible [endpoint], Event Hubs-compatible [path], and service [primary key] from your IoT hub
```sh
az iot hub show --query properties.eventHubEndpoints.events.endpoint --name {iot hub name}
az iot hub show --query properties.eventHubEndpoints.events.path --name {iot hub name}
az iot hub policy show --name service --query primaryKey --hub-name {iot hub name}
```


#### Create Cosmos DB account, database and container

6. Create Cosmos DB account:
```sh

az cosmosdb create --name {cosmos db account name} --resource-group {resource group name} --subscription {subscription id}
```

7. Create database:
```sh
az cosmosdb sql database create  --name {database name} --account-name {cosmos db account name} --resource-group {resource group name}
```


8. Create container:
> Azure Cosmos DB is a schema-agnostic database that allows you to iterate on your application without having to deal with schema or index management. By default, Azure Cosmos DB automatically indexes every property for all items in your container without having to define any schema or configure secondary indexes. more info can be found [here](#external-links).

```sh
az cosmosdb sql container create --name {container name} --database-name {database name} --account-name {cosmos db account name} --partition-key-path "/device/deviceid" --resource-group {resource group name}
```

9. Retrieve access key and connection string 
>Get the values Respectively `Primary SQL Connection String` and `primaryMasterKey`


```sh
az cosmosdb keys list --name {cosmos db account name} --resource-group {resource group name} --type keys
az cosmosdb keys list --name {cosmos db account name} --resource-group {resource group name} --type connection-strings --output table
```



### Local Environment

#### Preparing VSCode
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
4. install the azure cosmos db library:
```sh
pip3 install --upgrade azure-cosmos
```


#### Python Configuration File (.ini)
Create [.ini] file with the keys extracted from both:
- [Device Registration](#client-device-registration) section - `connectionstring`, `endpoint`, `path`, and `primary key`
- [Create CosmosDb](#create-cosmos-db-account-database-and-container) section - `Primary SQL Connection String`, `primaryMasterKey`, `database name` and `container name`
```ini
[default]
port=80
[iot]
connectionstring={connectionstring}
endpoint={endpoint}
path={path}
primarykey={primary key}
deviceid={device identifier}
[cosmosdb]
endpoint={Primary SQL Connection String}
primarykey={primaryMasterKey}
database={database name}
container={container name}
path=/device/deviceid
throughput=400
```



### Running the simulation

first - running client device simulation:
```python
python3 iot.py --mode run
```

next (while the client is running) and sending *simulated telemetry* - initiate the IoT hub consumer part, use the *--save* flag for saving items into Cosmos DB:
```python
python3 iot.py --mode listen [--save]
```

read cosmosdb item (all saved items):
```python
python3 iot.py --mode read [--print]
```

clear cosmosdb telemetries (all saved items):
```python
python3 iot.py --mode clear
```

[![N|Running Sample](https://github.com/eladtpro/python-iothub-cosmos/blob/main/.readme/running-sample.jpg?raw=true)](https://github.com/eladtpro/python-iothub-cosmos)




### Clean up resources

Using the Azure CLI

The following PowerShell script deletes a resource group:

```sh
az group delete --name {resource group name}
```


***



### Further Readings

#### External Links
The solution based on external resources:

* [Azure CLI: Create an IoT hub] - How to create an IoT hub using Azure CLI.
* [Azure CLI: Create and manage Cosmos DB] - Common commands to automate management of your Azure Cosmos DB accounts
* [Azure CLI: Create an Azure Cosmos Core (SQL) API account, database and container using Azure CLI]
* [Azure: Indexing in Azure Cosmos DB - Overview] - 
* [Azure: Understand data store models] - Selecting the right data store for your requirements is a key design decision
* [Azure: Use the Azure Table API to store IoT data] - Moving your database from Azure Table Storage into Azure Cosmos DB with a low throughput could have considerable cost savings.
* [Python: Send telemetry to IoT hub] - Send telemetry from a device to an IoT hub and read it with a back-end application (Python)
* [Python: Cosmos DB read and write data] - Create and manage an Azure Cosmos DB SQL API account from the Azure portal, and from Visual Studio Code with a Python app.
* [Windows Subsystem for Linux Installation Guide for Windows 10] - installing Windows Subsystem for Linux (WSL).
* [Python: configparser] - Handling Configuration Files in Python.
* [Python: TemplateEngine] - Python template engine.


#### Tools

Useful tooling

| Tool | Reference |
| ------ | ------ |
| *Azure (Portal)* | https://azure.microsoft.com/en-us/features/azure-portal |
| *python* | https://www.python.org/downloads |
| *Visual Studio Code* | https://code.visualstudio.com/download |
| *Windows Terminal* | https://docs.microsoft.com/en-us/windows/terminal/get-started |

####License

MIT

----

**Elad Tal (CE @ Microsoft)**

[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)


   [Azure CLI: Create an IoT hub]: <https://docs.microsoft.com/en-us/azure/iot-hub/iot-hub-create-using-cli>
   [Azure CLI: Create and manage Cosmos DB]:<https://docs.microsoft.com/en-us/azure/cosmos-db/manage-with-cli>
   [Azure CLI: Create an Azure Cosmos Core (SQL) API account, database and container using Azure CLI]: <https://docs.microsoft.com/en-us/azure/cosmos-db/scripts/cli/sql/create>
   [Azure: Understand data store models]:<https://docs.microsoft.com/en-us/azure/architecture/guide/technology-choices/data-store-overview>
   [Azure: Indexing in Azure Cosmos DB - Overview]:<https://docs.microsoft.com/en-us/azure/cosmos-db/index-overview>
   [Azure: Use the Azure Table API to store IoT data]: <https://docs.microsoft.com/en-us/learn/modules/choose-api-for-cosmos-db/8-use-the-azure-table-api-to-store-iot-data>
   [Python: Send telemetry to IoT hub]:<https://docs.microsoft.com/en-us/azure/iot-hub/quickstart-send-telemetry-python>
   [Python: Cosmos DB read and write data]:<https://docs.microsoft.com/en-us/azure/cosmos-db/create-sql-api-python>
   [Windows Subsystem for Linux Installation Guide for Windows 10]:<https://docs.microsoft.com/en-us/windows/wsl/install-win10>
   [Python: configparser]: <https://docs.python.org/3/library/configparser.html>
   [Python: TemplateEngine]: <https://github.com/vrash/PythonTemplateEngine>


