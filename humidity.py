from sense_hat import SenseHat
sense = SenseHat()
sense.clear()

humiditystart = sense.get_humidity()
while True:
    humiditycurrent = sense.get_humidity()
    if humiditystart < humiditycurrent:
        print("Higher")
    print(humiditycurrent)