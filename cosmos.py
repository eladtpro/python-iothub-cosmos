from azure.cosmos import exceptions, CosmosClient, PartitionKey
from json import loads
container = None

def init(config):
    # Initialize the Cosmos client
    global container
    if container is None:
        print('CosmosClient not exist and will be set for the first time')
        client = CosmosClient(config.cosmos.endpoint, config.cosmos.primarykey)

        # Create a database if not exists
        database = client.create_database_if_not_exists(id=config.cosmos.database)

        # Create a container
        # Using a good partition key improves the performance of database operations.
        container = database.create_container_if_not_exists(
            id=config.cosmos.container,
            partition_key=PartitionKey(path=config.cosmos.path),
            offer_throughput=config.cosmos.throughput
        )

    return container


def save(container, telemetry):
    item = loads(telemetry)
    container.create_item(body=item)


def read(config, printItems=False):
    container = init(config)
    query = f"SELECT * FROM c WHERE c.device.deviceid IN ('{config.iot.deviceid}')"
    telemetries = list(container.query_items(query=query, enable_cross_partition_query=True))
    request_charge = container.client_connection.last_response_headers['x-ms-request-charge']
    print('Query returned {0} telemetries. Operation consumed {1} request units'.format(len(telemetries), request_charge))
    #items_response = container.read_items(partition_key=deviceid)
    for telemetry in telemetries:
        print(f"Telemetry for {telemetry['device']['deviceid']} = {telemetry['data']['timestamp']}")
