# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project root for full license information.

# Using the Python Device SDK for IoT Hub:
#   https://github.com/Azure/azure-iot-sdk-python
# The sample connects to a device-specific MQTT endpoint on your IoT Hub.
from azure.iot.device import IoTHubDeviceClient, Message
import random
import time

DELAY_SCONDS = 2
def init(config):
    # The device connection string to authenticate the device with your IoT hub.
    # Using the Azure CLI:
    # az iot hub device-identity connection-string show --hub-name {your iot hub name} --device-id {your chosen device name} --output table

    # Create an IoT Hub client
    client = IoTHubDeviceClient.create_from_connection_string(
        config.connectionstring)
    return client


def run(config):

	try:
		client = init(config)
		print("IoT Hub device sending periodic messages, press Ctrl-C to exit")
		count = 0
		while True:
			# Build the message with simulated telemetry values.
			temperature = 20.0 + (random.random() * 15)
			humidity = 60 + (random.random() * 20)

			message = Message(f'{{"temperature": {temperature},"humidity": {humidity}}}')

			# Add a custom application property to the message.
			# An IoT hub can filter on these properties without access to the message body.
			if temperature > 30:
			    message.custom_properties["temperatureAlert"] = "true"
			else:
			    message.custom_properties["temperatureAlert"] = "false"

			count += 1
			# Send the message.
			client.send_message(message)
			print(f'{count}. Message successfully sent: {message}')
			time.sleep(DELAY_SCONDS)

	except KeyboardInterrupt:
	    print("IoTHubClient sample stopped")
	except:
	    print("IoTHubClient - Unexpected error")
	finally:
		client.disconnect()
