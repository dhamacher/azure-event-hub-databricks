import os
from time import sleep
from src.data_generator.generator import DataGenerator
from azure.eventhub.aio import EventHubProducerClient
from azure.eventhub import EventData


async def run(number_of_devices, interval, max_events):
    try:
        # Create a producer client to send messages to the event hub.
        # Specify a connection string to your event hubs namespace and
        # the event hub name.
        gen = DataGenerator(number_of_devices, interval)
        event_hub_connection = os.getenv('AZURE_EH_CON_STR')
        event_hub_name = os.getenv('AZURE_EH_NAME')
        producer = EventHubProducerClient.from_connection_string(conn_str=event_hub_connection, eventhub_name=event_hub_name)
        async with producer:
            # Create a batch.
            event_data_batch = await producer.create_batch()

            for t in range(max_events):
                for device in gen.devices:
                    # Add events to the batch.
                    event_data_batch.add(EventData(gen.generate_payload(device)))
                print(f'Sending batch {t} of {max_events}')
                # Send the batch of events to the event hub.
                await producer.send_batch(event_data_batch)
                sleep(interval)
        print('All batches complete!')
    except Exception as e:
        print(str(e))


def test_run(number_of_devices, interval, max_events):
    try:
        # Create a producer client to send messages to the event hub.
        # Specify a connection string to your event hubs namespace and
        # the event hub name.
        gen = DataGenerator(number_of_devices, interval)

        for t in range(max_events):
            for device in gen.devices:
                # Add events to the batch.
                print(gen.generate_payload(device))
            print(f'Sending batch {t} of {max_events}')

            sleep(interval)
        print('All batches complete!')
    except Exception as e:
        print(str(e))