#MAKE SURE YOU INSTALL THIS PACKAGE: sudo apt-get install python3-picamera
#ENABLE CAMERA IN RAPSI-CONFIG
from picamera import PiCamera
from time import sleep
camera = PiCamera()
camera.start_preview()
sleep(10)
camera.stop_preview()





