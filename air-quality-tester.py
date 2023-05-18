# Air Quality sensor Inland SEN-CCS811
# GND --> Ground
# Vin --> 3.3V or 5V
# SCL --> SCL (This is the I2C clock pin. Make sure it's enabled in raspi-config)
# SDA --> SDA (This is the I2C data pin. Make sure it's enabled in raspi-config)
# INT --> this is the interrupt-output pin. It is 3V logic and you can use it to detect when a new reading is ready or when a reading gets too high or too low.
# WAKE --> this is the wakeup pin for the sensor. It needs to be pulled to ground in order to communicate with the sensor. This pin is level shifted so you can use 3-5VDC logic.
# RST --> this is the reset pin. When it is pulled to ground the sensor resets itself. This pin is level shifted so you can use 3-5VDC logic.


from time import sleep
from Adafruit_CCS811 import Adafruit_CCS811


css = Adafruit_CCS811()

import busio
import adafruit_ccs811

import board

i2c = board.I2C()  # uses board.SCL and board.SDA

ccs = adafruit_ccs811.CCS811(i2c)

while True:
    sleep(5)
    print(
        f"Carbon Dioxide (CO2): {ccs.eco2} ppm, Volitile Organic Compounds (TVOC):{ccs.tvoc} ppb"
    )
