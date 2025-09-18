#!/usr/bin/env python3
"""
Raspberry Pi 3-LED Cool Flashing Sequence
==========================================

This script creates awesome flashing light sequences with 3 LEDs.
Features multiple patterns and effects:
- Chase sequences
- Breathing effects
- Random flashing
- Synchronized patterns
- And more!

Hardware Requirements:
- 3 LEDs with 330Ω resistors
- Breadboards and jumper wires

GPIO Pin Assignments:
- LED 1: GPIO 4 (Physical Pin 7)
- LED 2: GPIO 17 (Physical Pin 11)  
- LED 3: GPIO 27 (Physical Pin 13)
"""

from gpiozero import LED
import time
import random
import threading

# GPIO Pin definitions (Physical pins 7, 11, 13)
LED1_PIN = 4   # Physical pin 7
LED2_PIN = 17  # Physical pin 11
LED3_PIN = 27  # Physical pin 13

# Initialize LED objects
led1 = LED(LED1_PIN)
led2 = LED(LED2_PIN)
led3 = LED(LED3_PIN)

# LED arrays for easy manipulation
leds = [led1, led2, led3]
led_names = ["LED1 (Red)", "LED2 (Green)", "LED3 (Blue)"]

# Global control variables
running = True
current_pattern = 0

def turn_off_all():
    """Turn off all LEDs"""
    for led in leds:
        led.off()

def turn_on_all():
    """Turn on all LEDs"""
    for led in leds:
        led.on()

def pattern_chase_left_to_right():
    """Chase pattern from left to right"""
    print("🌟 Pattern: Chase Left to Right")
    for i in range(len(leds)):
        turn_off_all()
        leds[i].on()
        time.sleep(0.3)

def pattern_chase_right_to_left():
    """Chase pattern from right to left"""
    print("🌟 Pattern: Chase Right to Left")
    for i in range(len(leds)-1, -1, -1):
        turn_off_all()
        leds[i].on()
        time.sleep(0.3)

def pattern_bounce():
    """Bouncing ball effect"""
    print("🌟 Pattern: Bounce")
    # Go right
    for i in range(len(leds)):
        turn_off_all()
        leds[i].on()
        time.sleep(0.2)
    # Go left
    for i in range(len(leds)-2, 0, -1):
        turn_off_all()
        leds[i].on()
        time.sleep(0.2)

def pattern_flash_all():
    """Flash all LEDs together"""
    print("🌟 Pattern: Flash All")
    for _ in range(4):
        turn_on_all()
        time.sleep(0.2)
        turn_off_all()
        time.sleep(0.2)

def pattern_alternating():
    """Alternating pattern"""
    print("🌟 Pattern: Alternating")
    for _ in range(6):
        # Odd LEDs
        turn_off_all()
        leds[0].on()
        leds[2].on()
        time.sleep(0.3)
        # Even LED
        turn_off_all()
        leds[1].on()
        time.sleep(0.3)

def pattern_breathing():
    """Breathing effect using PWM"""
    print("🌟 Pattern: Breathing Effect")
    
    global led1, led2, led3, leds
    
    # First, turn off and close the regular LEDs to free up the pins
    turn_off_all()
    for led in leds:
        led.close()
    
    # Convert to PWM LEDs for breathing effect
    from gpiozero import PWMLED
    pwm_leds = [PWMLED(LED1_PIN), PWMLED(LED2_PIN), PWMLED(LED3_PIN)]
    
    try:
        for cycle in range(3):
            # Fade in
            for brightness in range(0, 101, 5):
                for pwm_led in pwm_leds:
                    pwm_led.value = brightness / 100.0
                time.sleep(0.05)
            
            # Fade out
            for brightness in range(100, -1, -5):
                for pwm_led in pwm_leds:
                    pwm_led.value = brightness / 100.0
                time.sleep(0.05)
    finally:
        # Clean up PWM LEDs
        for pwm_led in pwm_leds:
            pwm_led.close()
        
        # Recreate the regular LED objects for other patterns
        global led1, led2, led3, leds
        led1 = LED(LED1_PIN)
        led2 = LED(LED2_PIN)
        led3 = LED(LED3_PIN)
        leds = [led1, led2, led3]

def pattern_random_sparkle():
    """Random sparkling effect"""
    print("🌟 Pattern: Random Sparkle")
    for _ in range(15):
        turn_off_all()
        # Randomly select 1-2 LEDs to light up
        num_leds = random.randint(1, 2)
        selected_leds = random.sample(leds, num_leds)
        for led in selected_leds:
            led.on()
        time.sleep(0.15)

def pattern_wave():
    """Wave effect"""
    print("🌟 Pattern: Wave")
    for _ in range(4):
        # Forward wave
        for i in range(len(leds)):
            turn_off_all()
            for j in range(i + 1):
                leds[j].on()
            time.sleep(0.2)
        
        # Backward wave
        for i in range(len(leds)-2, -1, -1):
            turn_off_all()
            for j in range(i + 1):
                leds[j].on()
            time.sleep(0.2)

def pattern_binary_count():
    """Binary counting pattern"""
    print("🌟 Pattern: Binary Counter")
    for count in range(8):  # 0-7 in binary (3 bits)
        turn_off_all()
        # Convert to binary and light up corresponding LEDs
        binary = format(count, '03b')
        for i, bit in enumerate(binary):
            if bit == '1':
                leds[i].on()
        time.sleep(0.5)

def pattern_knight_rider():
    """Knight Rider style sweep"""
    print("🌟 Pattern: Knight Rider")
    
    # First, turn off and close the regular LEDs to free up the pins
    turn_off_all()
    for led in leds:
        led.close()
    
    # Use PWM LEDs for the dimming trail effect
    from gpiozero import PWMLED
    pwm_leds = [PWMLED(LED1_PIN), PWMLED(LED2_PIN), PWMLED(LED3_PIN)]
    
    try:
        for _ in range(3):
            # Sweep right
            for i in range(len(pwm_leds)):
                # Turn off all
                for pwm_led in pwm_leds:
                    pwm_led.value = 0
                # Main LED full brightness
                pwm_leds[i].value = 1.0
                # Trail effect
                if i > 0:
                    pwm_leds[i-1].value = 0.3
                time.sleep(0.15)
            
            # Sweep left
            for i in range(len(pwm_leds)-1, -1, -1):
                # Turn off all
                for pwm_led in pwm_leds:
                    pwm_led.value = 0
                # Main LED full brightness
                pwm_leds[i].value = 1.0
                # Trail effect
                if i < len(pwm_leds)-1:
                    pwm_leds[i+1].value = 0.3
                time.sleep(0.15)
    finally:
        # Clean up PWM LEDs
        for pwm_led in pwm_leds:
            pwm_led.close()
        
        # Recreate the regular LED objects for other patterns
        global led1, led2, led3, leds
        led1 = LED(LED1_PIN)
        led2 = LED(LED2_PIN)
        led3 = LED(LED3_PIN)
        leds = [led1, led2, led3]

def pattern_sos():
    """SOS morse code pattern"""
    print("🌟 Pattern: SOS Morse Code")
    
    def dot():
        turn_on_all()
        time.sleep(0.2)
        turn_off_all()
        time.sleep(0.2)
    
    def dash():
        turn_on_all()
        time.sleep(0.6)
        turn_off_all()
        time.sleep(0.2)
    
    # S (dot dot dot)
    for _ in range(3):
        dot()
    time.sleep(0.4)
    
    # O (dash dash dash)
    for _ in range(3):
        dash()
    time.sleep(0.4)
    
    # S (dot dot dot)
    for _ in range(3):
        dot()
    time.sleep(1.0)

# List of all patterns
patterns = [
    pattern_chase_left_to_right,
    pattern_chase_right_to_left,
    pattern_bounce,
    pattern_flash_all,
    pattern_alternating,
    pattern_breathing,
    pattern_random_sparkle,
    pattern_wave,
    pattern_binary_count,
    pattern_knight_rider,
    pattern_sos
]

def run_light_show():
    """Run the complete light show"""
    print("🎭 Starting Awesome LED Light Show! 🎭")
    print("=" * 50)
    print("Press Ctrl+C to stop the show")
    print()
    
    try:
        while running:
            for i, pattern in enumerate(patterns):
                if not running:
                    break
                    
                print(f"\n[Pattern {i+1}/{len(patterns)}]")
                pattern()
                time.sleep(0.5)  # Brief pause between patterns
                
                if not running:
                    break
            
            print("\n🎉 Show complete! Starting over...\n")
            time.sleep(2)
            
    except KeyboardInterrupt:
        print("\n\n🎭 Light show stopped by user")
    finally:
        cleanup()

def run_single_pattern(pattern_num):
    """Run a single pattern repeatedly"""
    if 1 <= pattern_num <= len(patterns):
        pattern = patterns[pattern_num - 1]
        print(f"🌟 Running Pattern {pattern_num} repeatedly")
        print("Press Ctrl+C to stop")
        
        try:
            while running:
                pattern()
                time.sleep(0.3)
        except KeyboardInterrupt:
            print(f"\n🌟 Pattern {pattern_num} stopped")
        finally:
            cleanup()
    else:
        print(f"❌ Invalid pattern number. Choose 1-{len(patterns)}")

def cleanup():
    """Clean up GPIO resources"""
    global running
    running = False
    
    # Ensure all LEDs are turned off
    try:
        turn_off_all()
    except:
        pass  # Ignore errors if LEDs already closed
    
    # Close all LED objects to properly release GPIO pins
    for led in leds:
        try:
            led.off()  # Extra safety - turn off before closing
            led.close()
        except:
            pass  # Ignore errors if already closed
    
    # Final safety check - try to turn off pins directly if needed
    try:
        from gpiozero import LED
        safety_leds = [LED(LED1_PIN), LED(LED2_PIN), LED(LED3_PIN)]
        for led in safety_leds:
            led.off()
            led.close()
    except:
        pass  # Ignore if pins already released
        
    print("🔌 All LEDs turned off - GPIO cleaned up")

def show_menu():
    """Display the main menu"""
    print("🎭 Raspberry Pi LED Light Show 🎭")
    print("=" * 40)
    print("Available patterns:")
    for i, pattern in enumerate(patterns, 1):
        pattern_name = pattern.__doc__.strip()
        print(f"  {i}. {pattern_name}")
    print()
    print("Options:")
    print("  A. Run complete light show (all patterns)")
    print("  1-11. Run specific pattern repeatedly")
    print("  Q. Quit")
    print("=" * 40)

def main():
    """Main program"""
    global running
    
    # Initial LED test
    print("🔧 Testing LEDs...")
    for i, led in enumerate(leds):
        print(f"  Testing {led_names[i]}...")
        led.on()
        time.sleep(0.5)
        led.off()
    
    print("✅ LED test complete!\n")
    
    while True:
        show_menu()
        choice = input("Enter your choice: ").upper().strip()
        
        if choice == 'Q':
            print("👋 Goodbye!")
            break
        elif choice == 'A':
            running = True
            run_light_show()
        elif choice.isdigit():
            pattern_num = int(choice)
            running = True
            run_single_pattern(pattern_num)
        else:
            print("❌ Invalid choice. Please try again.\n")
    
    cleanup()

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        print("🔧 Performing emergency cleanup...")
        cleanup()
    finally:
        # Final cleanup to ensure LEDs are off
        cleanup()
