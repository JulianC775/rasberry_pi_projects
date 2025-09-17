# Raspberry Pi 3-LED Cycle Project

## Project Overview

Build a 3-LED cycling system using a Raspberry Pi where:

- Red LED is on by default when powered
- Button press cycles through: Red → Green → Blue → Red
- Uses multiple breadboards for expanded workspace

## Hardware Requirements

### Electronics Components

- **1x Raspberry Pi** (Pi 3, Pi 4, or Pi Zero with GPIO pins)
- **3x LEDs** (Red, Green, Blue - 5mm standard)
- **3x 330Ω Resistors** (for LED current limiting)
- **1x 10kΩ Resistor** (for button pull-down)
- **1x Push Button** (momentary, 4-pin)
- **Multiple Jumper Wires** (male-to-male, male-to-female)
- **3x Breadboards** (connected together)
- **MicroSD Card** (16GB+ with Raspberry Pi OS)

### Tools Needed

- Computer for SSH/VNC or direct connection to Pi
- MicroSD card reader
- Monitor, keyboard, mouse (if not using SSH)
- Power supply for Raspberry Pi

## Software Setup

### 1. Raspberry Pi OS Setup

1. Download Raspberry Pi Imager from [rpi.org](https://www.raspberrypi.org/software/)
2. Flash Raspberry Pi OS to MicroSD card
3. Enable SSH and/or VNC if desired
4. Boot Raspberry Pi and complete initial setup

### 2. Install Required Python Libraries

```bash
# Update system packages
sudo apt update && sudo apt upgrade -y

# Install GPIO Zero library (usually pre-installed)
sudo apt install python3-gpiozero python3-pip -y

# Verify installation
python3 -c "import gpiozero; print('GPIO Zero installed successfully!')"
```

### 3. Enable GPIO and Test

```bash
# Test GPIO functionality
python3 -c "from gpiozero import LED; led = LED(2); led.on(); print('Built-in LED should be on')"
```

## Raspberry Pi GPIO Reference

### Power Pins

- **Pin 1 (3.3V)** - Power output for breadboard (max 50mA)
- **Pin 2 (5V)** - 5V power output (higher current available)
- **Pin 6 (GND)** - Ground connection
- **Pins 9, 14, 20, 25, 30, 34, 39** - Additional ground pins

### GPIO Pins (Digital I/O)

- **GPIO2-27** - General purpose digital pins (3.3V logic)
- **Pin 3 (GPIO2)** - I2C SDA (can be used for digital I/O)
- **Pin 5 (GPIO3)** - I2C SCL (can be used for digital I/O)
- **Pins 8, 10** - UART TX/RX (can be used for digital I/O)

### Key Features

- **40-pin GPIO header** with 26 usable GPIO pins
- **3.3V logic level** (compatible with most modern sensors)
- **Hardware PWM** on GPIO12, 13, 18, 19
- **SPI and I2C** interfaces available
- **Linux-based OS** with full programming environment

## Project Structure

This project is divided into three main sections:

### 1. Power Testing Section

- Detailed in `power_testing.md`
- Test hub distribution power system
- Verify power to all 3 breadboards
- LED testing on multiple boards

### 2. Hardware Section (Wiring)

- Detailed in `steps.md`
- Step-by-step hub distribution wiring
- Component placement across 3 breadboards
- GPIO pin assignments and circuit diagrams

### 3. Software Section (Python Code)

- Python code using GPIO Zero library
- LED control and button handling
- State management for cycling through LEDs
- Clean, readable code structure

## GPIO Pin Assignments for This Project

```python
# Pin definitions for Python code
RED_LED_PIN = 18      # Physical pin 12
GREEN_LED_PIN = 24    # Physical pin 18
BLUE_LED_PIN = 25     # Physical pin 22
BUTTON_PIN = 2        # Physical pin 3
POWER_PIN = 1         # Physical pin 1 (3.3V)
GROUND_PIN = 6        # Physical pin 6 (GND)
```

## Safety Notes

- Raspberry Pi operates at 3.3V logic level
- Always shutdown Pi properly before disconnecting power
- GPIO pins can source/sink up to 16mA each
- Use appropriate resistor values to protect LEDs
- Never connect 5V directly to GPIO pins
- Double-check connections before powering on

## Development Environment Options

### Option 1: Direct Connection

- Monitor, keyboard, mouse connected to Pi
- Use Thonny IDE (pre-installed) or nano/vim

### Option 2: SSH Connection

```bash
# Connect via SSH
ssh pi@[raspberry-pi-ip-address]

# Edit files with nano
nano led_cycle.py
```

### Option 3: VNC Connection

- Enable VNC in raspi-config
- Use VNC Viewer for graphical desktop access

## Next Steps

1. Follow the detailed wiring instructions in `steps.md`
2. Create and upload the Python code
3. Test the LED cycling functionality
4. Use GPIO Zero's built-in debugging features
5. Expand the project with additional features if desired

## Advantages of Raspberry Pi Setup

- **Full Linux environment** for advanced programming
- **GPIO Zero library** makes hardware control simple
- **SSH/VNC access** for remote development
- **Expandable** - can add sensors, displays, networking
- **Educational** - learn both hardware and software concepts

---

_Ready to build your Raspberry Pi LED cycling project!_
