import time

import network
import urequests
import gc
import settings


class Request:
    def __init__(self, ssid=settings.SSID, password=settings.PASSWORD):
        station = network.WLAN(network.STA_IF)

        station.active(True)
        station.connect(ssid, password)

        # try to connect for 30s
        for _ in range(1, 30):
            if not station.isconnected():
                print("Connecting...")
                time.sleep_ms(1000)
                pass
            print('Connection successful')
            print(station.ifconfig())
            return

        print('Error: Connection unsuccessful')
        print(station.ifconfig())

    @staticmethod
    def post(url, data):
        try:
            urequests.post(url, data)

        except Exception as error:
            print("Error: Unable to post request")
            print(str(error))
