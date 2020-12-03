import os
from time import sleep
from faker import Faker
from faker.providers import python
from src.data_generator.generator import DataGenerator
from azure.eventhub import EventHubProducerClient
from azure.eventhub import EventData

# Set Faker seed.
Faker.seed(0)


def create_batch(client, generator: DataGenerator):
    """ Returns an Azure Event Hub batch with generated messages.

    Parameters:
         client: Azure Event Hub client
         generator: The gernerator objects that contains the devices and definition to create messages send to the
         Event Hub

    Returns:
        event_data_batch: Azure Event Hub batch object

    """
    try:
        event_data_batch = client.create_batch()
        for device in generator.devices:
            # event_data_batch.add(EventData(gen.generate_payload(device)))
            event_data_batch.add(EventData(generator.generate_payload(device)))
        return event_data_batch
    except Exception as e:
        print(str(e))


async def run(number_of_devices, interval, max_events):
    """ Run the simulator i.e. create the data generator, connect to the Azure Event Hub, create a batch, and
    send the batch to the Event Hub

    Parameters:
        number_of_devices: The number of devices to create.
        interval: The interval in seconds to send messages to the Azure Event Hub.
        max_events:

    """
    try:
        # Create a producer client to send messages to the event hub.
        # Specify a connection string to your event hubs namespace and
        # the event hub name.
        gen = DataGenerator(number_of_devices, interval)
        event_hub_connection = os.getenv('AZURE_EH_CON_STR')
        event_hub_name = os.getenv('AZURE_EH_NAME')
        client = EventHubProducerClient.from_connection_string(conn_str=event_hub_connection, eventhub_name=event_hub_name)
        for t in range(max_events):
            try:
                print(f'Create Batch {t} of {max_events}')
                batch_data = create_batch(client, gen)
                print(f'Sending Batch: {t}')
                client.send_batch(batch_data)
                print(f'Sleep for {interval} seconds')
                sleep(interval)
            except Exception as e:
                print(str(e))
        print('All batches complete!')
    except Exception as e:
        print(str(e))
