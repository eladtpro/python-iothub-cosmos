from azure.cosmos import exceptions, CosmosClient, PartitionKey
from json import loads
container = None
client = None


def init(config):
    # Initialize the Cosmos client
    global container
    global client
    if container is None:
        client = CosmosClient(config.cosmos.endpoint, config.cosmos.primarykey)

        # Create a database if not exists
        database = client.create_database_if_not_exists(
            id=config.cosmos.database)

        # Create a container
        # Using a good partition key improves the performance of database operations.
        container = database.create_container_if_not_exists(
            id=config.cosmos.container,
            partition_key=PartitionKey(path=config.cosmos.path),
            offer_throughput=config.cosmos.throughput
        )

    return container


def clear(config):
    container = init(config)
    items = read(config)
    counter = len(items)
    for telemetry in items:
        container.delete_item(telemetry, config.iot.deviceid)
        print(f"Deleted [{counter}]: {telemetry['device']['deviceid']} - timestamp: {telemetry['data']['timestamp']} | temperature: {telemetry['data']['temperature']} | humidity: {telemetry['data']['humidity']}")
        counter -= 1


def save(container, telemetry):
    item = loads(telemetry)
    container.create_item(body=item)


def read(config, printItems=False):
    container = init(config)
    query = f"SELECT * FROM c WHERE c.device.deviceid IN ('{config.iot.deviceid}')"
    telemetries = list(container.query_items(query=query, enable_cross_partition_query=False))
    request_charge = container.client_connection.last_response_headers['x-ms-request-charge']
    print('Query returned {0} telemetries. Operation consumed {1} request units'.format(
        len(telemetries), request_charge))
    #items_response = container.read_items(partition_key=deviceid)
    if(True == printItems):
        for telemetry in telemetries:
            print(
                f"Telemetry: {telemetry['device']['deviceid']} - timestamp: {telemetry['data']['timestamp']} | temperature: {telemetry['data']['temperature']} | humidity: {telemetry['data']['humidity']}")
    return telemetries
