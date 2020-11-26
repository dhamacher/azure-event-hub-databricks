from faker import Faker
from faker.providers import geo, internet, python
import json

Faker.seed(0)

class Device:
    def __init__(self):
        fake = Faker()
        fake.add_provider(geo)
        fake.add_provider(python)
        fake.add_provider(internet)
        self._device_id = fake.uuid4()
        self._device_ip_address = fake.ipv4_private()
        self._device_status = fake.pybool()
        self._device_location = json.dumps(fake.local_latlng(country_code='CA'))

    @property
    def device_id(self):
        return self._device_id

    @property
    def device_ip(self):
        return self._device_ip_address

    @property
    def device_status(self):
        return self._device_status

    @device_status.setter
    def device_status(self, val: bool):
        self._device_status = val

    @property
    def device_location(self):
        return self._device_location

    @property
    def to_string(self) -> str:
        return f'Device ID: {self._device_id} ' \
               f'| Device IP: {self._device_ip_address}  ' \
               f'| Device Status: {self._device_status} ' \
               f'| Device Location: {self._device_location}'
