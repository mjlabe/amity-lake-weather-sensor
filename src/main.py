from requests.requests import Request
from sensors.ds18b20 import DS18B20Sensor
from sensors.am2320 import AM2320Sensor

from settings import WEATHER_STATION_URL


if __name__ == "__main__":
    requests = Request()
    ds18b20 = DS18B20Sensor()
    am2320 = AM2320Sensor()
    while True:
        data_ds18b20 = {
            "temperature": ds18b20.read_ds_sensor()
        }
        data_am2320 = {
            "temperature": am2320.read_temp_am2320(),
            "humidity": am2320.read_hum_am2320(),
        }
        data = {
            "temperature": {
                "water": data_ds18b20["temperature"],
                "air": data_am2320["temperature"],
            },
            "humidity": {
                "air": data_am2320["humidity"],
            }
        }
        requests.post(data=data, url=WEATHER_STATION_URL)