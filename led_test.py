#!/usr/bin/env python3
"""
Individual LED Test Script
Tests each LED one by one to verify wiring

Hardware connections:
- RED LED: GPIO18 (pin 12)
- GREEN LED: GPIO24 (pin 18) 
- BLUE LED: GPIO25 (pin 22)
"""

from gpiozero import LED
import time

# Set up LEDs
red_led = LED(18)    # GPIO18
green_led = LED(24)  # GPIO24
blue_led = LED(25)   # GPIO25

def test_leds():
    """Test each LED individually"""
    print("LED Test Starting...")
    print("=" * 20)
    
    try:
        # Test RED LED
        print("🔴 Testing RED LED...")
        red_led.on()
        time.sleep(2)
        red_led.off()
        time.sleep(0.5)
        
        # Test GREEN LED
        print("🟢 Testing GREEN LED...")
        green_led.on()
        time.sleep(2)
        green_led.off()
        time.sleep(0.5)
        
        # Test BLUE LED
        print("🔵 Testing BLUE LED...")
        blue_led.on()
        time.sleep(2)
        blue_led.off()
        time.sleep(0.5)
        
        # Test all together
        print("🌈 Testing ALL LEDs together...")
        red_led.on()
        green_led.on()
        blue_led.on()
        time.sleep(2)
        
        # Turn off all
        red_led.off()
        green_led.off()
        blue_led.off()
        
        print("✅ LED test complete!")
        
    except KeyboardInterrupt:
        print("\nTest interrupted")
        
    finally:
        # Make sure all LEDs are off
        red_led.off()
        green_led.off()
        blue_led.off()
        print("All LEDs turned off")

if __name__ == "__main__":
    test_leds()
