#!/usr/bin/env python3
"""
3-LED Cycle Controller
Press button to cycle through Red → Green → Blue → Off → repeat

Hardware connections:
- RED LED: GPIO18 (pin 12)
- GREEN LED: GPIO24 (pin 18) 
- BLUE LED: GPIO25 (pin 22)
- Button: GPIO2 (pin 3)
- Power: Pi 3.3V (pin 1) to breadboard red rail
- Ground: Pi GND (pin 6) to breadboard blue rail
"""

from gpiozero import LED, Button
from signal import pause
import time

# Set up LEDs
red_led = LED(18)    # GPIO18
green_led = LED(24)  # GPIO24
blue_led = LED(25)   # GPIO25

# Set up button
button = Button(2)   # GPIO2

# LED cycle state (0=off, 1=red, 2=green, 3=blue)
led_state = 0

def all_leds_off():
    """Turn off all LEDs"""
    red_led.off()
    green_led.off()
    blue_led.off()

def cycle_leds():
    """Cycle through LED states when button is pressed"""
    global led_state
    
    # Turn off all LEDs first
    all_leds_off()
    
    # Advance to next state
    led_state = (led_state + 1) % 4
    
    # Turn on appropriate LED based on state
    if led_state == 1:
        red_led.on()
        print("🔴 RED LED ON")
    elif led_state == 2:
        green_led.on()
        print("🟢 GREEN LED ON")
    elif led_state == 3:
        blue_led.on()
        print("🔵 BLUE LED ON")
    else:  # led_state == 0
        print("⚫ ALL LEDs OFF")

def main():
    print("3-LED Cycle Controller")
    print("=" * 25)
    print("Press button to cycle: Red → Green → Blue → Off")
    print("Press Ctrl+C to exit")
    print()
    
    # Make sure all LEDs start off
    all_leds_off()
    print("⚫ ALL LEDs OFF (starting state)")
    
    # Set up button press event
    button.when_pressed = cycle_leds
    
    try:
        # Keep program running and wait for button presses
        pause()
        
    except KeyboardInterrupt:
        print("\n\nProgram interrupted by user")
        
    finally:
        # Clean up - turn off all LEDs
        all_leds_off()
        print("All LEDs turned off. Goodbye! 👋")

if __name__ == "__main__":
    main()
