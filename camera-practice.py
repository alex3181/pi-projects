
# add button to pin 2 and pin 10
# add buzzer to pin 11 and ground


import picamera
import RPi.GPIO as GPIO
import time

def take_photo(file_path):
	with picamera.PiCamera() as camera:
        	camera.resolution = (1280, 720)  # Set the resolution as needed
        	camera.start_preview()
        	camera.capture(file_path)
        	camera.stop_preview()

def clicked_button(channel):
	print ("Button clicked")
	GPIO.output(buzzer_pin, True)
	time.sleep(0.3)
	GPIO.output(buzzer_pin, False)	


if __name__ == "__main__":
	
	button_pin=10 
	buzzer_pin=12

	GPIO.setmode(GPIO.BOARD) #Set GPIO mode
	GPIO.setup(button_pin,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
	GPIO.setup(buzzer_pin,GPIO.OUT)
	GPIO.add_event_detect(button_pin, GPIO.RISING, callback=clicked_button, bouncetime=1000)

	try:
		print ("Waiting for button press...")
		while True:
			pass
	except KeyboardInterrupt:
		print (KeyboardInterrupt)
	
	GPIO.cleanup() #Clean up
