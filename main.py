from fastapi import FastAPI
from sensors.ds18b20 import read_temp_ds18b20
from sensors.am2320 import read_temp_am2320, read_hum_am2320

app = FastAPI()


@app.get("/temp")
async def root():
    temp_water = read_temp_ds18b20()
    temp_air = read_temp_am2320()
    humidity_air = read_hum_am2320()
    return {
        'air': {
            'temperature': temp_air,
            'humidity': humidity_air
        },
        'water': {
            'temperature': temp_water,
        }
    }
