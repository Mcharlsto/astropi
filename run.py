from sense_hat import SenseHat
sense = SenseHat()
import time
import threading
numberofPassings = 0
#def displayData():
#    while True:
 #       global numberOfPassings
#        sense.show_message("Number of movements: " + numberOfPassings)

def checkHumidity():
    while True:
        global timespassed
        global timer
        global numberofPassings
        global humiditystart
        timer = 0
        humiditystart = sense.get_humidity()
        while True:
            humiditycurrent = sense.get_humidity()
            if humiditystart < humiditycurrent:
                humiditycurrent = sense.get_humidity()
                print("Higher")
                print(humiditycurrent)
                numberofPassings =  numberofPassings + 1
                time.sleep(10)
            elif timer > 10:
                timer = 0
                humiditystart = sense.get_humidity()
            else:
                timer = timer + 1
            time.sleep(1)
            sense.show_message("Number of movements: " + numberOfPassings)

inputThread = threading.Thread(target=checkHumidity())
outputThread = threading.Thread(target=displayData())

