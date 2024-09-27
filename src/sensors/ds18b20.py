from machine import Pin
import onewire
import ds18x20
import settings


class DS18B20Sensor:
    def __init__(self):
        """
        Set up device to read with a One Wire protocol

        The pin the sensor is connected to is defined in settings.DS18X20_PIN
        """
        try:
            # select_rom(rom)
            # Send the message to select a specific device based on the rom number. This number will be obtained by scan().
            # The selected device will respond to further read and write calls.
            # devices = scan()
            # Return the list of rom numbers of all devices on the onwire bus.
            # self.rom = rom
            ds_pin = Pin(settings.DS18X20_PIN)
            self.ds_sensor = ds18x20.DS18X20(onewire.OneWire(ds_pin))
            self.rom = self.ds_sensor.scan()[0]

        except Exception as error:
            print("Error: Unable to initialize DS18B20 sensor")
            print(str(error))

    def read_ds_sensor(self) -> float:
        try:
            self.ds_sensor.convert_temp()
            temp = self.ds_sensor.read_temp(self.rom)
            if isinstance(temp, float):
                msg = round(temp, 2)
                print(temp, end=' ')
                print('Valid temperature')
                return msg
            return 0.0

        except Exception as error:
            print("Error: Unable to read DS18B20 sensor")
            print(str(error))
