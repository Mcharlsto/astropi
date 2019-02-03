from sense_hat import SenseHat
import time
sense = SenseHat()
r = 255
g = 255
b = 255
timespassed = 0
sense.clear((r, g, b))
timer = 0
humiditystart = sense.get_humidity()
while True:
    humiditycurrent = sense.get_humidity()
    if humiditystart < humiditycurrent:
        humiditystart = sense.get_humidity()
        print("Higher")
        print(humiditycurrent)
        timespassed = timespassed + 1
        time.sleep(10)
    elif timer > 10:
        timer = 0
        humiditystart = sense.get_humidity()
    else:
        timer = timer + 1
    time.sleep(1)