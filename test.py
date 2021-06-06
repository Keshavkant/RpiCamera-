from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.start_preview()
for i in range(5):
	sleep(2)
	camera.capture('/home/pi/Desktop/image%03d.jpg' % i) #Defines the name of the file.
camera.stop_preview()


