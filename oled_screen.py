#!/usr/bin/env python3
"""Simple system stats display on 128x64 OLED via I2C pins 3/5"""

import time
from luma.core.interface.serial import i2c
from luma.core.render import canvas
from luma.oled.device import ssd1306

# Setup OLED
serial = i2c(port=1, address=0x3C)
device = ssd1306(serial, width=128, height=64)

# Get system info
def get_system_stats():
    try:
        import psutil
        cpu = psutil.cpu_percent(interval=1)
        mem = psutil.virtual_memory()
        disk = psutil.disk_usage('/')

        return {
            'cpu': f"{cpu:.0f}%",
            'mem': f"{mem.used/1e9:.1f}G/{mem.total/1e9:.1f}G",
            'disk': f"{disk.used/1e9:.1f}G/{disk.total/1e9:.1f}G"
        }
    except ImportError:
        return {
            'cpu': "??%",
            'mem': "??G/??G",
            'disk': "??G/??G"
        }

# Main display loop
while True:
    stats = get_system_stats()

    with canvas(device) as draw:
        # Header
        draw.text((0, 0), "System Stats", fill=255)

        # CPU
        draw.text((0, 16), f"CPU:  {stats['cpu']}", fill=255)

        # Memory
        draw.text((0, 28), f"MEM:  {stats['mem']}", fill=255)

        # Disk
        draw.text((0, 40), f"DISK: {stats['disk']}", fill=255)

    time.sleep(2)  # Update every 2 seconds
