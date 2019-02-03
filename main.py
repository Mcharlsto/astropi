from sense_hat import SenseHat
sense = SenseHat()
import time
numberOfPassings = 0
import logging
from logzero import logger
import logzero
import os
import datetime
dir_path = os.path.dirname(os.path.realpath(__file__))

now_time = datetime.datetime.now()
start_time = datetime.datetime.now()
logzero.logfile(dir_path+"/data01.csv")
formatter = logging.Formatter('%(name)s - %(asctime)-15s - %(levelname)s: %(message)s');
logzero.formatter(formatter)
sense.flip_v()
sense.flip_h()

while (now_time < start_time + datetime.timedelta(minutes=17)):
    global timespassed
    global timer
    global numberOfPassings
    global humiditystart
    timer = 0
    humiditystart = sense.get_humidity()
    while True:
        humiditycurrent = sense.get_humidity()
        if humiditystart + 1 < humiditycurrent:
            humiditystart = sense.get_humidity()
            print("Higher")
            print(humiditycurrent)
            numberOfPassings =  numberOfPassings + 1
            time.sleep(10)
        elif timer > 10:
            timer = 0
            humiditystart = sense.get_humidity()
        else:
            timer = timer + 1
        time.sleep(1)
        sense.show_message("Number of Passing: ")
        sense.show_message(str(numberOfPassings))
        logger.info("%s,%s", numberOfPassings, "%s,%s")
    now_time = datetime.datetime.now()
            
