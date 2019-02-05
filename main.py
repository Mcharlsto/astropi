# Astro Pi Submission for Matthew Charlston, Owen Cole and James Cook for Phase 2 of Mission Space Lab 2018

# Import libraries needed for experiment
from sense_hat import SenseHat # For outputting to the hat
import time # For timing and sleeping
import logging # For logging
from logzero import logger # For the csv output
import logzero # For logging
import os # For getting current directory
import datetime # For getting the current time

# Initiate Sense Hat
sense = SenseHat() # Initiate
sense.flip_v() # Flip the screen so it is visible to the astronauts
sense.flip_h() # Continued

# Set up libraries, timing, logging and variables
numberOfPassings = 0 # Variable to store the number of times an astronaut has passed
dirPath = os.path.dirname(os.path.realpath(__file__)) # Get current directory
nowTime = datetime.datetime.now() # Get current time
startTime = datetime.datetime.now() # Get start time
logzero.logfile(dirPath+"/data01.csv") # Set file to output data to
formatter = logging.Formatter('%(name)s - %(asctime)-15s - %(levelname)s: %(message)s'); # Create custom formatter
logzero.formatter(formatter) # Use custom formatter

# Loop for 170 minutes so the program is not terminated by the pi uncleanly
while (nowTime < startTime + datetime.timedelta(minutes=17)):

    # Declare variables
    timer = 0 # Variable to store timer
    baseHumidity = sense.get_humidity() # Humidity value to compare against

    # Get current humidity
    currentHumidity = sense.get_humidity()

    # Check if humidity has gone up more than one
    if baseHumidity + 1 < currentHumidity:
        baseHumidity = sense.get_humidity()
        print("Higher humidity detected.")
        print(currentHumidity)
        numberOfPassings =  numberOfPassings + 1 # Add another passing
        time.sleep(10) # Sleep for ten seconds before getting next reading
    elif timer > 10:
        timer = 0 # Reset timer
        baseHumidity = sense.get_humidity() # Get new base reading if not exceeded for ten seconds
    else:
        timer = timer + 1 # Add one on to timer for above elif

    # Sleep for a second !!Why is this necessary!!
    time.sleep(1)

    # Output and log the value 
    sense.show_message("Number of Passing: ") # Output onto matrix for Columbus viewing
    sense.show_message(str(numberOfPassings)) # Continued output
    logger.info("%s,%s", numberOfPassings, "%s,%s") # Add to logger output csv

    # Get new now time for 170 min timer
    nowTime = datetime.datetime.now()
