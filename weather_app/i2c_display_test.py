#!/usr/bin/env python3
"""
I2C Display Test for Dual OLED Setup
Tests both OLED displays at addresses 0x3C (Weather) and 0x3D (Sensor)
Run this before implementing the full weather station to verify hardware setup
"""

from luma.core.interface.serial import i2c
from luma.core.render import canvas
from luma.oled.device import ssd1306
import time

def test_oled_display(address, name):
    """Test a single OLED display"""
    try:
        print(f"Testing {name} OLED at address 0x{address:02X}...")
        serial = i2c(port=1, address=address)
        device = ssd1306(serial, width=128, height=64)

        # Test pattern 1: Display name
        with canvas(device) as draw:
            draw.text((0, 0), f"{name} Display", fill=255)
            draw.text((0, 16), f"Address: 0x{address:02X}", fill=255)
            draw.text((0, 32), "Test Pattern 1", fill=255)
            draw.text((0, 48), "SUCCESS!", fill=255)
        time.sleep(2)

        # Test pattern 2: Full screen
        with canvas(device) as draw:
            draw.text((0, 0), f"{name} OLED", fill=255)
            draw.text((0, 16), "Ready for Weather", fill=255)
            draw.text((0, 32), "Station Project", fill=255)
            draw.text((0, 48), f"Time: {time.strftime('%H:%M:%S')}", fill=255)
        time.sleep(2)

        print(f"✅ {name} OLED test PASSED")
        return True

    except Exception as e:
        print(f"❌ {name} OLED test FAILED: {e}")
        return False

def main():
    """Main test function"""
    print("🧪 Dual OLED Display Test")
    print("=" * 40)

    # Test Weather OLED (0x3C)
    weather_ok = test_oled_display(0x3C, "Weather")

    print()

    # Test Sensor OLED (0x3D)
    sensor_ok = test_oled_display(0x3D, "Sensor")

    print()
    print("=" * 40)

    if weather_ok and sensor_ok:
        print("🎉 ALL TESTS PASSED!")
        print("✅ Both OLED displays are working correctly")
        print("✅ Ready to implement the weather station")
    elif weather_ok:
        print("⚠️  PARTIAL SUCCESS")
        print("✅ Weather OLED is working")
        print("❌ Sensor OLED failed - check connections")
    elif sensor_ok:
        print("⚠️  PARTIAL SUCCESS")
        print("❌ Weather OLED failed - check connections")
        print("✅ Sensor OLED is working")
    else:
        print("❌ ALL TESTS FAILED")
        print("❌ Check I2C connections and addresses")
        print("💡 Try running: i2cdetect -y 1")

if __name__ == "__main__":
    main()
