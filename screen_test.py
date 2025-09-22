#!/usr/bin/env python3
"""Simple date and time display on a 128x64 SSD1306 OLED using I2C pins 3/5.

Requirements on Raspberry Pi:
  sudo apt-get install -y python3-pip python3-pil fonts-dejavu
  pip3 install luma.oled
  Enable I2C in raspi-config, wire SDA to pin 3, SCL to pin 5.
"""

import datetime
import sys
import time

try:
    from luma.core.interface.serial import i2c  # type: ignore[import-not-found]
    from luma.core.render import canvas  # type: ignore[import-not-found]
    from luma.oled.device import ssd1306  # type: ignore[import-not-found]
    from PIL import ImageFont  # type: ignore[import-not-found]
except Exception:
    print("Missing dependencies. Install with: pip3 install luma.oled Pillow", file=sys.stderr)
    sys.exit(1)


def main() -> int:
    serial = i2c(port=1, address=0x3C)
    device = ssd1306(serial, width=128, height=64)

    # Use default bitmap font for simplicity
    try:
        font = ImageFont.load_default()
    except Exception:
        font = None

    try:
        while True:
            now = datetime.datetime.now()
            date_str = now.strftime("%Y-%m-%d")
            time_str = now.strftime("%H:%M:%S")

            with canvas(device) as draw:
                # Clear and display date and time
                draw.text((0, 0), date_str, fill=255, font=font)
                draw.text((0, 16), time_str, fill=255, font=font)

            time.sleep(1)  # Update every second
    except KeyboardInterrupt:
        # Clear on exit
        try:
            device.clear()
        except Exception:
            pass
        return 0


if __name__ == "__main__":
    sys.exit(main())
