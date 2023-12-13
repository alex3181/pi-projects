import picamera
import RPi.GPIO as gpio


def take_photo(file_path):
    with picamera.PiCamera() as camera:
        camera.resolution = (1280, 720)  # Set the resolution as needed
        camera.start_preview()
        # Add a delay if needed to stabilize the camera
        # For example: time.sleep(2)
        camera.capture(file_path)
        camera.stop_preview()

def pressed_button():

if __name__ == "__main__":
    gpio.setmode(gpio.BOARD)
    gpio.setup(10,gpio.IN,pull_up_down=gpio.PUD_DOWN)

    while True:
        if gpio.input(10) == gpio.HIGH:
            print ("Button was pushed")

