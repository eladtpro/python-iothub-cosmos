# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project root for full license information.

"""
This sample demonstrates how to use the Microsoft Azure Event Hubs Client for Python async API to
read messages sent from a device. Please see the documentation for @azure/event-hubs package
for more details at https://pypi.org/project/azure-eventhub/
"""

import asyncio
from azure.eventhub import TransportType
from azure.eventhub.aio import EventHubConsumerClient
from azure.eventhub import EventHubConsumerClient


# Define callbacks to process events

def on_event_batch(partition_context, events):
    for event in events:
        print(f"Received Event: partition-{partition_context.partition_id}. Telemetry-{event.body_as_str()}.")
        #print(f"Received event from partition: {partition_context.partition_id}. Telemetry received: {event.body_as_str()}.	Properties (set by device): {event.properties}.	System properties (set by IoT Hub): {event.system_properties}.\n")
    partition_context.update_checkpoint()


def on_error(partition_context, error):
    # Put your code here. partition_context can be None in the on_error callback.
    if partition_context:
        print(f"An exception: {partition_context.partition_id} occurred during receiving from Partition: {error}.")
    else:
        print(f"An exception: {error} occurred during the load balance process.")


async def on_event_batch_async(partition_context, events):
    for event in events:
        print(f"Received Event: partition-{partition_context.partition_id}. Telemetry-{event.body_as_str()}.")
        #print(f"Received event from partition: {partition_context.partition_id}. Telemetry received: {event.body_as_str()}.	Properties (set by device): {event.properties}.	System properties (set by IoT Hub): {event.system_properties}.\n")
    await partition_context.update_checkpoint()


async def on_error_async(partition_context, error):
    # Put your code here. partition_context can be None in the on_error callback.
    if partition_context:
        print(
            f"An exception: {partition_context.partition_id} occurred during receiving from Partition: {error}.")
    else:
        print(
            f"An exception: {error} occurred during the load balance process.")


def get_connection_string(config):
    return f'Endpoint={config.endpoint}/;SharedAccessKeyName=service;SharedAccessKey={config.primarykey};EntityPath={config.path}'


def listenasync(config):
    connectionstring = get_connection_string(config)

    loop = asyncio.get_event_loop()
    client = EventHubConsumerClient.from_connection_string(conn_str=connectionstring, consumer_group="$default",
                                                           # transport_type=TransportType.AmqpOverWebsocket,  # uncomment it if you want to use web socket
                                                           # http_proxy={  # uncomment if you want to use proxy
                                                           #     'proxy_hostname': '127.0.0.1',  # proxy hostname.
                                                           #     'proxy_port': 3128,  # proxy port.
                                                           #     'username': '<proxy user name>',
                                                           #     'password': '<proxy password>'
                                                           # }
                                                           )
    try:
        loop.run_until_complete(client.receive_batch(
            on_event_batch=on_event_batch_async, on_error=on_error_async))
    except KeyboardInterrupt:
        print("Receiving has stopped.")
    finally:
        loop.run_until_complete(client.close())
        loop.stop()


def listen(config):
    connectionstring = get_connection_string(config)

    client = EventHubConsumerClient.from_connection_string(conn_str=connectionstring, consumer_group="$default",
                                                           # transport_type=TransportType.AmqpOverWebsocket,  # uncomment it if you want to use web socket
                                                           # http_proxy={  # uncomment if you want to use proxy
                                                           #     'proxy_hostname': '127.0.0.1',  # proxy hostname.
                                                           #     'proxy_port': 3128,  # proxy port.
                                                           #     'username': '<proxy user name>',
                                                           #     'password': '<proxy password>'
                                                           # }
                                                           )
    try:
        with client:
            client.receive_batch(
                on_event_batch=on_event_batch,
                on_error=on_error
            )
    except KeyboardInterrupt:
        print("Receiving has stopped.")
