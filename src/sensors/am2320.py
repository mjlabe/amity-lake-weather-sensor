import adafruit_am2320
import board


class AM2320Sensor:
    def __init__(self):
        try:
            # create the I2C shared bus
            i2c = board.I2C()  # uses board.SCL and board.SDA
            self.am = adafruit_am2320.AM2320(i2c)
        except Exception as error:
            print("Error: Unable to initialize AM2320 sensor")
            print(str(error))

    def read_temp_am2320(self) -> float:
        try:
            return self.am.temperature

        except Exception as error:
            print("Error: Unable to read AM2320 sensor temperature")
            print(str(error))

    def read_hum_am2320(self) -> float:
        try:
            return self.am.relative_humidity

        except Exception as error:
            print("Error: Unable to read AM2320 sensor humidity")
            print(str(error))
