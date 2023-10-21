# Complete project details at https://RandomNerdTutorials.com
import settings

from requests import requests

try:
    import usocket as socket
except:
    import socket

from time import sleep
from machine import Pin, deepsleep

import network

import esp
import gc

import onewire
import ds18x20

import settings

esp.osdebug(None)

gc.collect()

ds_pin = Pin(4)
ds_sensor = ds18x20.DS18X20(onewire.OneWire(ds_pin))

roms = ds_sensor.scan()
print('Found DS devices: ', roms)

while True:
    ds_sensor.convert_temp()
    sleep(1)
    for rom in roms:
        print(rom)
        print(ds_sensor.read_temp(rom))
    sleep(5)
    # deepsleep(5000)

    request = requests.Request()
    try:
        response = request.post(url=settings.URL, data={})
        if response.status_code != 200:
            print("Failed to POST:", response)
    except Exception as error:
        print("Failed to POST:", error)
