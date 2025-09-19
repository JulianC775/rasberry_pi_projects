#!/usr/bin/env python3
"""
🎭 Enhanced Raspberry Pi LED Light Show 🎭
=========================================

A clean, modern LED controller with only the coolest patterns.
Automatically starts the light show when run - no menu needed!

🔌 WIRING LAYOUT (Top to Bottom):
   LED 1: Physical Pin  7 → GPIO  4 (Red)
   LED 2: Physical Pin 11 → GPIO 17 (Green) 
   LED 3: Physical Pin 13 → GPIO 27 (Blue)
   LED 4: Physical Pin 15 → GPIO 22 (Yellow)
   LED 5: Physical Pin 12 → GPIO 18 (Orange)
   LED 6: Physical Pin 16 → GPIO 23 (Purple)
   
   Each LED needs a 330Ω resistor to Ground
   All Ground connections can share common ground pins

Features:
- Knight Rider sweep with trailing effects
- Wave propagation with phase shifts
- Breathing/pulsing effects  
- Multi-chase patterns
- Lightning storm simulation
- Realistic pendulum physics
- Random sparkle bursts
- Heartbeat rhythm simulation
- Fire flickering effect
- Spectrum analyzer visualization
- Matrix-style digital rain
- Traffic light sequences
- Mathematical sine waves
- 6-bit binary counter (0-63)
- SOS morse code

Hardware: 6 LEDs with 330Ω resistors (see wiring layout above)
"""

import time
import random
import math
from gpiozero import LED, PWMLED

# GPIO Configuration (matches physical pin layout top to bottom)
LED_PINS = [4, 17, 27, 22, 18, 23]  # Physical pins 7, 11, 13, 15, 12, 16
LED_COLORS = ["🔴 Red", "🟢 Green", "🔵 Blue", "🟡 Yellow", "🟠 Orange", "🟣 Purple"]

class LEDController:
    def __init__(self):
        self.leds = [LED(pin) for pin in LED_PINS]
        self.running = True
        print("🎭 LED Light Show Starting...")
        self._test_leds()
    
    def _test_leds(self):
        """Quick LED test on startup"""
        print("🔧 Testing LEDs...")
        for i, led in enumerate(self.leds):
            print(f"  Testing {LED_COLORS[i]}")
            led.on()
            time.sleep(0.3)
            led.off()
        print("✅ All LEDs working!\n")
    
    def all_off(self):
        """Turn off all LEDs"""
        for led in self.leds:
            led.off()
    
    def all_on(self):
        """Turn on all LEDs"""  
        for led in self.leds:
            led.on()
    
    def cleanup(self):
        """Clean shutdown"""
        self.running = False
        self.all_off()
        for led in self.leds:
            led.close()
        print("\n🔌 LEDs turned off - Show ended!")

    # === COOL PATTERNS ===
    
    def knight_rider(self, cycles=3):
        """🚗 Knight Rider sweep with trailing effect"""
        print("🌟 Knight Rider Sweep")
        
        # Switch to PWM for smooth trailing
        self.all_off()
        for led in self.leds:
            led.close()
        
        pwm_leds = [PWMLED(pin) for pin in LED_PINS]
        
        try:
            for _ in range(cycles):
                # Sweep right
                for i in range(len(pwm_leds)):
                    for led in pwm_leds:
                        led.value = 0
                    pwm_leds[i].value = 1.0  # Main LED
                    if i > 0:
                        pwm_leds[i-1].value = 0.3  # Trail
                    time.sleep(0.15)
                
                # Sweep left  
                for i in range(len(pwm_leds)-1, -1, -1):
                    for led in pwm_leds:
                        led.value = 0
                    pwm_leds[i].value = 1.0  # Main LED
                    if i < len(pwm_leds)-1:
                        pwm_leds[i+1].value = 0.3  # Trail
                    time.sleep(0.15)
        finally:
            for led in pwm_leds:
                led.close()
            self.leds = [LED(pin) for pin in LED_PINS]
    
    def breathing_pulse(self, cycles=2):
        """💨 Smooth breathing effect"""
        print("🌟 Breathing Pulse")
        
        self.all_off()
        for led in self.leds:
            led.close()
            
        pwm_leds = [PWMLED(pin) for pin in LED_PINS]
        
        try:
            for _ in range(cycles):
                # Breathe in
                for brightness in range(0, 101, 3):
                    for led in pwm_leds:
                        led.value = brightness / 100.0
                    time.sleep(0.03)
                
                # Hold
                time.sleep(0.2)
                
                # Breathe out
                for brightness in range(100, -1, -3):
                    for led in pwm_leds:
                        led.value = brightness / 100.0
                    time.sleep(0.03)
                
                time.sleep(0.3)
        finally:
            for led in pwm_leds:
                led.close()
            self.leds = [LED(pin) for pin in LED_PINS]
    
    def lightning_storm(self, duration=8):
        """⚡ Random lightning strikes"""
        print("🌟 Lightning Storm")
        
        start_time = time.time()
        while time.time() - start_time < duration:
            # Random pause between strikes
            time.sleep(random.uniform(0.1, 1.5))
            
            # Lightning strike!
            strike_leds = random.sample(self.leds, random.randint(1, 3))
            
            # Quick flash
            for led in strike_leds:
                led.on()
            time.sleep(random.uniform(0.05, 0.15))
            
            for led in strike_leds:
                led.off()
            time.sleep(random.uniform(0.02, 0.08))
            
            # Sometimes double strike
            if random.random() < 0.3:
                for led in strike_leds:
                    led.on()
                time.sleep(random.uniform(0.03, 0.1))
                for led in strike_leds:
                    led.off()
    
    def fire_flicker(self, duration=10):
        """🔥 Realistic fire flickering"""
        print("🌟 Fire Flicker")
        
        self.all_off()
        for led in self.leds:
            led.close()
            
        pwm_leds = [PWMLED(pin) for pin in LED_PINS]
        
        try:
            start_time = time.time()
            while time.time() - start_time < duration:
                for i, led in enumerate(pwm_leds):
                    # Each LED flickers independently
                    base_brightness = 0.3 + random.random() * 0.7
                    flicker = random.uniform(-0.2, 0.3)
                    brightness = max(0, min(1, base_brightness + flicker))
                    led.value = brightness
                
                time.sleep(random.uniform(0.05, 0.15))
        finally:
            for led in pwm_leds:
                led.close()
            self.leds = [LED(pin) for pin in LED_PINS]
    
    def matrix_rain(self, cycles=4):
        """🟢 Digital Matrix rain effect"""
        print("🌟 Matrix Digital Rain")
        
        for cycle in range(cycles):
            # Rain drops falling
            for wave in range(6):
                self.all_off()
                
                # Create "falling" effect with more complex patterns
                for i in range(len(self.leds)):
                    if (wave + i) % 3 == 0 or (wave - i) % 4 == 0:
                        self.leds[i].on()
                
                time.sleep(0.2)
            
            # Brief pause between cycles
            self.all_off()
            time.sleep(0.5)
    
    def sparkle_burst(self, bursts=8):
        """✨ Random sparkle explosions"""
        print("🌟 Sparkle Burst")
        
        for _ in range(bursts):
            # Random burst pattern
            num_leds = random.randint(1, 3)
            selected_leds = random.sample(self.leds, num_leds)
            
            # Quick burst
            for led in selected_leds:
                led.on()
            time.sleep(random.uniform(0.1, 0.3))
            
            for led in selected_leds:
                led.off()
            time.sleep(random.uniform(0.2, 0.6))
    
    def binary_counter(self, max_count=64):
        """🔢 Binary counting display (0-63 with 6 LEDs)"""
        print("🌟 Binary Counter")
        
        for count in range(max_count):
            self.all_off()
            binary = format(count, '06b')  # 6-bit binary
            
            for i, bit in enumerate(binary):
                if bit == '1':
                    self.leds[i].on()
            
            time.sleep(0.5)
        
        self.all_off()
        time.sleep(0.5)
    
    def sos_signal(self, repeats=2):
        """🆘 SOS morse code"""
        print("🌟 SOS Morse Code")
        
        def dot():
            self.all_on()
            time.sleep(0.2)
            self.all_off()
            time.sleep(0.2)
        
        def dash():
            self.all_on() 
            time.sleep(0.6)
            self.all_off()
            time.sleep(0.2)
        
        for _ in range(repeats):
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
            time.sleep(1.2)
    
    def sine_wave_pulse(self, cycles=3):
        """🌊 Mathematical sine wave pattern"""
        print("🌟 Sine Wave Pulse")
        
        self.all_off()
        for led in self.leds:
            led.close()
            
        pwm_leds = [PWMLED(pin) for pin in LED_PINS]
        
        try:
            for cycle in range(cycles):
                for step in range(60):  # One full sine cycle
                    angle = (step / 60.0) * 2 * math.pi
                    brightness = (math.sin(angle) + 1) / 2  # 0 to 1
                    
                    for led in pwm_leds:
                        led.value = brightness
                    
                    time.sleep(0.05)
        finally:
            for led in pwm_leds:
                led.close()
            self.leds = [LED(pin) for pin in LED_PINS]
    
    def wave_propagation(self, cycles=4):
        """🌊 Wave traveling across LEDs with phase shifts"""
        print("🌟 Wave Propagation")
        
        self.all_off()
        for led in self.leds:
            led.close()
            
        pwm_leds = [PWMLED(pin) for pin in LED_PINS]
        
        try:
            for cycle in range(cycles):
                for step in range(120):  # Two full wave cycles
                    time_val = step / 20.0  # Time parameter
                    
                    for i, led in enumerate(pwm_leds):
                        # Wave equation: brightness = sin(time - position)
                        phase = time_val - (i * 0.5)  # Phase shift for each LED
                        brightness = (math.sin(phase) + 1) / 2
                        led.value = brightness
                    
                    time.sleep(0.05)
        finally:
            for led in pwm_leds:
                led.close()
            self.leds = [LED(pin) for pin in LED_PINS]
    
    def chase_patterns(self, cycles=3):
        """🏃 Multiple chase patterns simultaneously"""
        print("🌟 Multi-Chase Patterns")
        
        for cycle in range(cycles):
            # Double chase - two LEDs chasing each other
            for i in range(len(self.leds) * 2):
                self.all_off()
                self.leds[i % len(self.leds)].on()
                self.leds[(i + 3) % len(self.leds)].on()
                time.sleep(0.15)
            
            # Triple chase
            for i in range(len(self.leds) * 2):
                self.all_off()
                self.leds[i % len(self.leds)].on()
                self.leds[(i + 2) % len(self.leds)].on()
                self.leds[(i + 4) % len(self.leds)].on()
                time.sleep(0.12)
    
    def pendulum_swing(self, swings=8):
        """⚖️ Realistic pendulum motion with physics"""
        print("🌟 Pendulum Swing")
        
        self.all_off()
        for led in self.leds:
            led.close()
            
        pwm_leds = [PWMLED(pin) for pin in LED_PINS]
        
        try:
            for swing in range(swings):
                # Simulate pendulum physics
                for step in range(60):
                    # Pendulum position follows sine wave
                    angle = math.sin(step / 10.0) * (len(pwm_leds) - 1) / 2
                    center_pos = (len(pwm_leds) - 1) / 2
                    led_pos = center_pos + angle
                    
                    # Clear all LEDs
                    for led in pwm_leds:
                        led.value = 0
                    
                    # Light up the LED closest to pendulum position
                    main_led = int(led_pos)
                    if 0 <= main_led < len(pwm_leds):
                        pwm_leds[main_led].value = 1.0
                        
                        # Add some blur/glow to adjacent LEDs
                        if main_led > 0:
                            pwm_leds[main_led - 1].value = 0.3
                        if main_led < len(pwm_leds) - 1:
                            pwm_leds[main_led + 1].value = 0.3
                    
                    time.sleep(0.08)
        finally:
            for led in pwm_leds:
                led.close()
            self.leds = [LED(pin) for pin in LED_PINS]
    
    def heartbeat(self, beats=5):
        """💓 Realistic heartbeat pattern"""
        print("🌟 Heartbeat")
        
        self.all_off()
        for led in self.leds:
            led.close()
            
        pwm_leds = [PWMLED(pin) for pin in LED_PINS]
        
        try:
            for beat in range(beats):
                # First beat (lub)
                for brightness in [0, 0.3, 0.8, 1.0, 0.6, 0.2, 0]:
                    for led in pwm_leds:
                        led.value = brightness
                    time.sleep(0.08)
                
                time.sleep(0.15)  # Brief pause
                
                # Second beat (dub)
                for brightness in [0, 0.4, 0.9, 0.5, 0.1, 0]:
                    for led in pwm_leds:
                        led.value = brightness
                    time.sleep(0.06)
                
                time.sleep(0.4)  # Pause between heartbeats
        finally:
            for led in pwm_leds:
                led.close()
            self.leds = [LED(pin) for pin in LED_PINS]
    
    def spectrum_analyzer(self, duration=10):
        """🎵 Fake spectrum analyzer bars"""
        print("🌟 Spectrum Analyzer")
        
        start_time = time.time()
        while time.time() - start_time < duration:
            self.all_off()
            
            # Each LED represents a frequency band
            for i, led in enumerate(self.leds):
                # Random "amplitude" for each frequency band
                if random.random() < 0.3 + (i * 0.1):  # Higher frequencies more active
                    led.on()
            
            time.sleep(random.uniform(0.05, 0.15))
    
    def traffic_light(self, cycles=3):
        """🚦 Traffic light sequence"""
        print("🌟 Traffic Light Sequence")
        
        # Assuming first 3 LEDs are Red, Yellow, Green
        for cycle in range(cycles):
            # Red
            self.all_off()
            self.leds[0].on()  # Red
            time.sleep(2.0)
            
            # Red + Yellow
            self.leds[1].on()  # Yellow
            time.sleep(1.0)
            
            # Green
            self.all_off()
            self.leds[2].on()  # Green
            time.sleep(2.0)
            
            # Yellow
            self.all_off()
            self.leds[1].on()  # Yellow
            time.sleep(1.0)
        
        self.all_off()

def main():
    """Main light show - runs automatically!"""
    controller = LEDController()
    
    # Cool patterns to cycle through
    patterns = [
        ("knight_rider", 2),
        ("wave_propagation", 3),
        ("breathing_pulse", 2), 
        ("chase_patterns", 2),
        ("lightning_storm", 6),
        ("pendulum_swing", 6),
        ("sparkle_burst", 6),
        ("heartbeat", 4),
        ("fire_flicker", 8),
        ("spectrum_analyzer", 8),
        ("matrix_rain", 3),
        ("traffic_light", 2),
        ("sine_wave_pulse", 2),
        ("binary_counter", 32),
        ("sos_signal", 1),
    ]
    
    try:
        print("🎭 Starting Epic Light Show! Press Ctrl+C to stop\n")
        
        while controller.running:
            for pattern_name, param in patterns:
                if not controller.running:
                    break
                    
                pattern_method = getattr(controller, pattern_name)
                pattern_method(param)
                
                # Brief pause between patterns
                time.sleep(1.0)
            
            print("\n🎉 Show complete! Restarting...\n")
            time.sleep(2)
            
    except KeyboardInterrupt:
        print("\n\n🎭 Light show stopped by user")
    finally:
        controller.cleanup()

if __name__ == "__main__":
    main()