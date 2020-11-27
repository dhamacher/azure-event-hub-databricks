import json
from src.data_generator.device import Device
from faker import Faker
from faker.providers import python
from datetime import datetime

Faker.seed(0)


class DataGenerator:
    def __init__(self, num_of_devices: int, interval_in_sec: int):
        try:
            self._fake = Faker()
            self._fake.add_provider(python)
            self._devices = []
            for x in range(num_of_devices):
                d = Device()
                self._devices.append(d)
            self._interval = interval_in_sec
        except Exception as e:
            print(str(e))

    def set_devices_status(self, status: bool):
        try:
            for d in self._devices:
                d.device_status = status
        except Exception as e:
            print(str(e))

    def display_devices(self):
        for d in self._devices:
            print(d.to_string)

    @property
    def devices(self) -> list:
        return self._devices

    def generate_payload(self, device: Device):
        try:
            payload_dict = {
                'timestamp': str(datetime.now()),
                'humidity': float('{:3.2f}'.format(self._fake.pyfloat(left_digits=2, right_digits=2, min_value=40, max_value=70, positive=True) / 100)),
                'temperature': float('{:4.2f}'.format(self._fake.pyfloat(left_digits=2, right_digits=2, min_value=19, max_value=27, positive=True))),
                'device_id': str(device.device_id),
                'device_ip': str(device.device_ip),
                'device_location': str(device.device_location)
            }
            json_dump = json.dumps(payload_dict)
            return json_dump
        except Exception as e:
            print(str(e))
