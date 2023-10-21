import network
import urequests
import gc
import settings


class Request:
    def __init__(self, ssid=settings.SSID, password=settings.PASSWORD):
        station = network.WLAN(network.STA_IF)

        station.active(True)
        station.connect(ssid, password)

        while station.isconnected() == False:
            pass

        print('Connection successful')
        print(station.ifconfig())

    @staticmethod
    def post(url, data):
        urequests.post(url, data)
