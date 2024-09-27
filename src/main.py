import time

import settings

from requests.requests import Request
from sensors.ds18b20 import DS18B20Sensor
from sensors.am2320 import AM2320Sensor


if __name__ == "__main__":
    """
    Keep capturing sensor data and posting to the server
    
    Capture rate is defined in settings.INTERVAL_MIN (minutes) - default is 10
    Server URL is defined in settings.WEATHER_STATION_URL
    """
    capture_interval_min = settings.INTERVAL_MIN if hasattr(settings, "INTERVAL_MIN") else 10
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
        requests.post(data=data, url=settings.WEATHER_STATION_URL)

        time.sleep_us(capture_interval_min * 1000)
