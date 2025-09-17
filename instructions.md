# ESP32 3-LED Cycle Project

## Project Overview

Build a 3-LED cycling system using an ESP32 microcontroller where:

- Red LED is on by default when powered
- Button press cycles through: Red → Green → Blue → Red
- Uses multiple breadboards for expanded workspace

## Hardware Requirements

### Electronics Components

- **1x ESP32 Development Board** (ESP32-WROOM-32 or similar)
- **3x LEDs** (Red, Green, Blue - 5mm standard)
- **3x 330Ω Resistors** (for LED current limiting)
- **1x 10kΩ Resistor** (for button pull-down)
- **1x Push Button** (momentary, 4-pin)
- **Multiple Jumper Wires** (male-to-male, male-to-female)
- **3x Breadboards** (connected together)

### Tools Needed

- Computer with Arduino IDE installed
- USB cable (typically USB-A to micro-USB or USB-C, depending on ESP32 board)

## Software Setup

### 1. Install Arduino IDE

1. Download Arduino IDE from [arduino.cc](https://www.arduino.cc/en/software)
2. Install the IDE on your computer
3. Launch Arduino IDE

### 2. Add ESP32 Board Support

1. Open Arduino IDE
2. Go to **File → Preferences**
3. In "Additional Board Manager URLs" add:
   ```
   https://dl.espressif.com/dl/package_esp32_index.json
   ```
4. Go to **Tools → Board → Boards Manager**
5. Search for "ESP32" and install "esp32 by Espressif Systems"
6. Select your ESP32 board: **Tools → Board → ESP32 Arduino → ESP32 Dev Module**

### 3. Configure Port and Upload Settings

1. Connect ESP32 to computer via USB
2. Select correct port: **Tools → Port → [Your ESP32 Port]**
3. Set upload speed: **Tools → Upload Speed → 115200**
4. Set flash frequency: **Tools → Flash Frequency → 80MHz**

### 4. Test ESP32 Connection

1. Open **File → Examples → 01.Basics → Blink**
2. Click **Upload** (arrow button)
3. Built-in LED should start blinking
4. If successful, ESP32 is ready for programming!

## ESP32 Pin Reference

### Power Pins

- **3.3V** - Power output for breadboard
- **GND** - Ground connection
- **VIN** - External power input (optional)

### GPIO Pins (Digital I/O)

- **GPIO2** - Built-in LED (for testing)
- **GPIO4, 5, 12-19, 21-23, 25-27, 32-33** - General purpose digital pins
- All GPIO pins can be used for digital input/output

### Key Features

- **Wi-Fi & Bluetooth** built-in
- **32-bit dual-core processor**
- **Flash memory** for program storage
- **Multiple PWM channels** for advanced LED control
- **ADC pins** for analog input (if needed later)

## Project Structure

This project is divided into two main sections:

### 1. Hardware Section (Wiring)

- Detailed in `steps.md`
- Step-by-step breadboard wiring instructions
- Component placement and connections
- Pin assignments and circuit diagrams

### 2. Software Section (Arduino Code)

- Arduino C++ code for ESP32
- LED control and button handling
- State management for cycling through LEDs
- Serial monitor debugging

## Safety Notes

- ESP32 operates at 3.3V logic level
- Always disconnect power when wiring
- Double-check connections before powering on
- Use appropriate resistor values to protect LEDs
- ESP32 GPIO pins can source/sink up to 12mA each

## Next Steps

1. Follow the detailed wiring instructions in `steps.md`
2. Upload and test the Arduino code
3. Troubleshoot any issues using serial monitor
4. Expand the project with additional features if desired

---

_Ready to build your ESP32 LED cycling project!_
