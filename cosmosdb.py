from azure.cosmos import exceptions, CosmosClient, PartitionKey

container = None

def init(config):
    # Initialize the Cosmos client
    global container
    if container is None:
        print('CosmosClient not exist and will be set for the first time')
        client = CosmosClient(config.cosmos_endpoint, config.cosmos_primarykey)

        # Create a database if not exists
        database = client.create_database_if_not_exists(id=config.database)

        # Create a container
        # Using a good partition key improves the performance of database operations.
        container = database.create_container_if_not_exists(
            id=config.container,
            partition_key=PartitionKey(path="/device/deviceid"),
            offer_throughput=400
        )

    return container


def save(sample):
    container.create_item(body=sample)


def read(deviceid, printItems=False):
    query = f"SELECT * FROM c WHERE c.deviceid IN ({deviceid})"
    samples = list(container.query_items(
        query=query,
        enable_cross_partition_query=False
    ))
    request_charge = container.client_connection.last_response_headers['x-ms-request-charge']
    print('Query returned {0} samples. Operation consumed {1} request units'.format(
        len(samples), request_charge))
    #items_response = container.read_items(partition_key=deviceid)
    for sample in samples:
        print(f"Telemetry for {sample['deviceid']} = {sample['timestamp']}")
