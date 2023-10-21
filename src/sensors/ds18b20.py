from machine import Pin
import onewire
import ds18x20
import settings


class DS18B20Sensor:
    def __init__(self, rom):
        self.rom = rom
        ds_pin = Pin(settings.DS_PIN)
        self.ds_sensor = ds18x20.DS18X20(onewire.OneWire(ds_pin))

    def read_ds_sensor(self):
        self.ds_sensor.convert_temp()
        temp = self.ds_sensor.read_temp(self.rom)
        if isinstance(temp, float):
            msg = round(temp, 2)
            print(temp, end=' ')
            print('Valid temperature')
            return msg
        return b'0.0'
