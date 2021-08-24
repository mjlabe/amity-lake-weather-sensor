import adafruit_am2320
import board


# create the I2C shared bus
i2c = board.I2C()  # uses board.SCL and board.SDA
am = adafruit_am2320.AM2320(i2c)


def read_temp_am2320() -> dict:
    return am.temperature


def read_hum_am2320() -> dict:
    return am.relative_humidity
