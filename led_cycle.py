#!/usr/bin/env python3
"""
Raspberry Pi 3-LED Cycle Project
================================

This script controls 3 LEDs (Red, Green, Blue) connected to a Raspberry Pi.
- Red LED starts on by default
- Button press cycles through: Red → Green → Blue → Red
- Uses GPIO Zero library for simple hardware control

Hardware Requirements:
- 3 LEDs (Red, Green, Blue) with 330Ω resistors
- 1 Push button with 10kΩ pull-down resistor
- Breadboards and jumper wires

GPIO Pin Assignments:
- Red LED: GPIO 4 (Physical Pin 7)
- Green LED: GPIO 18 (Physical Pin 12)
- Blue LED: GPIO 23 (Physical Pin 16)
- Button: GPIO 2 (Physical Pin 3)
"""

from gpiozero import LED, Button
from signal import pause
import time

# GPIO Pin definitions
RED_LED_PIN = 4      # Physical pin 7
GREEN_LED_PIN = 18   # Physical pin 12
BLUE_LED_PIN = 23    # Physical pin 16
BUTTON_PIN = 2       # Physical pin 3

# Initialize LED objects
red_led = LED(RED_LED_PIN)
green_led = LED(GREEN_LED_PIN)
blue_led = LED(BLUE_LED_PIN)

# Initialize button with debounce
button = Button(BUTTON_PIN, bounce_time=0.1)

# LED state tracking
current_led = 0  # 0=Red, 1=Green, 2=Blue
led_list = [red_led, green_led, blue_led]
led_names = ["Red", "Green", "Blue"]

def turn_off_all_leds():
    """Turn off all LEDs"""
    red_led.off()
    green_led.off()
    blue_led.off()

def cycle_leds():
    """Cycle to the next LED in sequence"""
    global current_led
    
    # Turn off current LED
    turn_off_all_leds()
    
    # Move to next LED (cycle back to 0 after 2)
    current_led = (current_led + 1) % 3
    
    # Turn on the new current LED
    led_list[current_led].on()
    
    print(f"Switched to {led_names[current_led]} LED")

def initialize_system():
    """Initialize the system with Red LED on"""
    global current_led
    current_led = 0
    turn_off_all_leds()
    red_led.on()
    print("System initialized - Red LED is ON")
    print("Press the button to cycle through LEDs")
    print("Press Ctrl+C to exit")

def cleanup():
    """Clean up GPIO resources"""
    turn_off_all_leds()
    print("\nSystem shutdown - All LEDs turned off")

def main():
    """Main program loop"""
    try:
        # Initialize system
        initialize_system()
        
        # Set up button press event
        button.when_pressed = cycle_leds
        
        # Keep the program running
        pause()
        
    except KeyboardInterrupt:
        # Handle Ctrl+C gracefully
        cleanup()
    except Exception as e:
        print(f"An error occurred: {e}")
        cleanup()

if __name__ == "__main__":
    main()
