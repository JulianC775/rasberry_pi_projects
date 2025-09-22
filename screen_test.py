#!/usr/bin/env python3
"""Minimal date/time display on 128x64 OLED via I2C pins 3/5"""

import datetime
import time
from luma.core.interface.serial import i2c
from luma.core.render import canvas
from luma.oled.device import ssd1306

# Setup OLED on I2C bus 1 (pins 3/5), address 0x3C
serial = i2c(port=1, address=0x3C)
device = ssd1306(serial, width=128, height=64)

# Main loop - update display every second
while True:
    now = datetime.datetime.now()
    date_str = now.strftime("%Y-%m-%d")
    time_str = now.strftime("%H:%M:%S")

    with canvas(device) as draw:
        draw.text((0, 0), date_str, fill=255)
        draw.text((0, 16), time_str, fill=255)

    time.sleep(1)
