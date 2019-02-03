from sense_hat import SenseHat
sense = SenseHat()
sense.clear()

humiditystart = sense.get_humidity()
While True:
    humiditycurrent = sense.get_humidity()
    If humiditystart < humiditycurrent:
        print("Higher")
