# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project root for full license information.

# Using the Python Device SDK for IoT Hub:
#   https://github.com/Azure/azure-iot-sdk-python
# The sample connects to a device-specific MQTT endpoint on your IoT Hub.
from azure.iot.device import IoTHubDeviceClient, Message
import random
import time
from models.telemetry import Telemetry, format, flatten
from utils.error import printError

DELAY_SECONDS = 2
client = None

def init(config):
    # The device connection string to authenticate the device with your IoT hub.
    # Using the Azure CLI:
    # az iot hub device-identity connection-string show --hub-name {your iot hub name} --device-id {your chosen device name} --output table
    # Create an IoT Hub client
    global client
    if client is None:
        print('IoTHubDeviceClient not exist and will be set for the first time')
        client = IoTHubDeviceClient.create_from_connection_string(config.iot.connectionstring)
    return client


def run(config):
    global client
    try:
        client = init(config)
        print("IoT Hub device sending periodic messages, press Ctrl-C to exit")
        batchid = 1
        while True:
            # Build the message with simulated telemetry values.
            temperature = 20.0 + (random.random() * 15)
            humidity = 60 + (random.random() * 20)
            data = Telemetry(config, batchid, temperature, humidity)
            msg = format(data)
            message = Message(msg)
            # Add a custom application property to the message.
            # An IoT hub can filter on these properties without access to the message body.
            if temperature > 30:
                message.custom_properties["temperatureAlert"] = "true"
            else:
                message.custom_properties["temperatureAlert"] = "false"
            batchid += 1
            # Send the message.
            client.send_message(message)
            #flat = flatten(message)
            print(f'Run: {message}')
            time.sleep(DELAY_SECONDS)
    except KeyboardInterrupt:
        print("Disconnected.")
    except:
        printError()
    finally:
        client.disconnect()
