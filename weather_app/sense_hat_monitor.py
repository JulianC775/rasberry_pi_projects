#!/usr/bin/env python3
"""Simple system stats display on 128x64 OLED via I2C pins 3/5"""

import time
from luma.core.interface.serial import i2c
from luma.core.render import canvas
from luma.oled.device import ssd1306

# Import configuration
try:
    from config import WEATHER_API_KEY, CITY_NAME, COUNTRY_CODE, WEATHER_API_URL
except ImportError:
    print("Error: config.py not found!")
    print("Please copy config_template.py to config.py and add your API key.")
    print("See config_template.py for instructions.")
    exit(1)

# Setup OLED
serial = i2c(port=1, address=0x3C)
device = ssd1306(serial, width=128, height=64)

#get weather info
def get_weather_stats():
    try:
        


def get_sense_hat_data():
    try: