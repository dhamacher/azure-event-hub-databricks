from faker import Faker
from faker.providers import geo, internet, python
import json

# Set Faker seed
Faker.seed(0)

""" Class that defines a IoT device for the simulator"""
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
        """ Returns the device ID in form of a GUID. """
        return self._device_id

    @property
    def device_ip(self):
        """ Returns the device IPv4 address. """
        return self._device_ip_address

    @property
    def device_status(self) -> bool:
        """ Returns the device status. """
        return self._device_status

    @device_status.setter
    def device_status(self, val: bool):
        """ Sets the device status. """
        self._device_status = val

    @property
    def device_location(self):
        """ Returns the geo location for this device."""
        return self._device_location

    @property
    def to_string(self) -> str:
        """ Returns device metadata as string. """
        return f'Device ID: {self._device_id} ' \
               f'| Device IP: {self._device_ip_address}  ' \
               f'| Device Status: {self._device_status} ' \
               f'| Device Location: {self._device_location}'
