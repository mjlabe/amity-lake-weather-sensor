import adafruit_am2320
import board


class AM2320:
    def __init__(self):
        # create the I2C shared bus
        i2c = board.I2C()  # uses board.SCL and board.SDA
        self.am = adafruit_am2320.AM2320(i2c)

    def read_temp_am2320(self) -> dict:
        return self.am.temperature

    def read_hum_am2320(self) -> dict:
        return self.am.relative_humidity
