
# add button to pin 2 and pin 10
# add buzzer to pin 11 and ground

from picamera2 import Picamera2
from gpiozero import Button, LED, Buzzer
from signal import pause
from time import sleep


button = Button(17)
buzzer = Buzzer(21)
pic_counter=0

def take_photo(file_path):
	with Picamera2() as camera:
		#camera_config = camera.create_still_configuration(main={"size": (1920, 1080)}, lores={"size": (640, 480)}, display="lores")
		#camera.configure(camera_config)
		camera_config=camera.create_still_configuration()
		camera.configure(camera_config)
		camera.start()
		sleep(2)
		camera.capture_file(file_path)
		# image = camera.capture_mage("main") # capture PIL images
		camera.close()

def pressed_button():
	global pic_counter
	buzzer.on()
	sleep(0.15)
	buzzer.off()
	file_name="pic"+str(pic_counter)+".jpg"
	take_photo(file_name)
	print("File "+file_name+" created")
	pic_counter=pic_counter+1



button.when_pressed=pressed_button
pause()
	
