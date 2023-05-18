from time import sleep
from Adafruit_CCS811 import Adafruit_CCS811

css = Adafruit_CCS811()

import busio
import adafruit_ccs811

from board import *

i2c = board.I2C()  # uses board.SCL and board.SDA

ccs = adafruit_ccs811.CCS811(i2c)

print("CO2: ", ccs.eco2, " TVOC:", ccs.tvoc)
