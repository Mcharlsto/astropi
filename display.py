from sense_hat import SenseHat
sense = SenseHat()

def displayData():
    global numberOfPassings
    sense.show_message("Number of movements: " + numberOfPassings)
    ]