from machine import Pin
import onewire
import ds18x20
import settings


class DS18B20Sensor:
    def __init__(self):
        # select_rom(rom)
        # Send the message to select a specific device based on the rom number. This number will be obtained by scan().
        # The selected device will respond to further read and write calls.
        # devices = scan()
        # Return the list of rom numbers of all devices on the onwire bus.
        # self.rom = rom
        ds_pin = Pin(settings.DS_PIN)
        self.ds_sensor = ds18x20.DS18X20(onewire.OneWire(ds_pin))
        self.rom = self.ds_sensor.scan()[0]

    def read_ds_sensor(self) -> float:
        self.ds_sensor.convert_temp()
        temp = self.ds_sensor.read_temp(self.rom)
        if isinstance(temp, float):
            msg = round(temp, 2)
            print(temp, end=' ')
            print('Valid temperature')
            return msg
        return 0.0
