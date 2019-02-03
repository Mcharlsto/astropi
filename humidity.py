from sense_hat import SenseHat
import time
sense = SenseHat()
sense.clear()
humiditystart = sense.get_humidity()
while True:
    humiditycurrent = sense.get_humidity()
    if humiditystart < humiditycurrent:
        humiditystart = sense.get_humidity()
        print("Higher")
        print(humiditycurrent)
    time.sleep(1)