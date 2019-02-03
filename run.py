from sense_hat import SenseHat
sense = SenseHat()
import time
import threading

def displayData():
    global numberOfPassings
    sense.show_message("Number of movements: " + numberOfPassings)
    ]

def checkHumidity():
    global timespassed = 0
    global timer = 0
    global humiditystart = sense.get_humidity()
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

inputThread