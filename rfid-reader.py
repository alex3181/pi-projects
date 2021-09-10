# enable SPI interface in raspi-config
# apt install python3-dev
# pip install spidev
# pip install mfrc522

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import time
reader = SimpleMFRC522()

try:
        while True:
                id, text = reader.read()
                print(id)
                print(text)
                time.sleep(1)
finally:
        GPIO.cleanup()
