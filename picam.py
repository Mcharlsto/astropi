from time import sleep
from picamera import PiCamera import os
dir_path = os.path.dirname(os.path.realpath(__file__))

camera = PiCamera()
camera.resolution = (1296, 972)
camera.start_preview()

sleep(2)
camera.capture(dir_path+"/image.jpg")