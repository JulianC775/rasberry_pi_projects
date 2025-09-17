# Raspberry Pi 3-LED Cycle Project

A simple Raspberry Pi project that cycles through 3 LEDs (Red, Green, Blue) using a button press.

## Quick Start

1. **Wire your hardware** following the detailed instructions in `steps.md`
2. **Test your hardware** by running: `python3 test_hardware.py`
3. **Run the main program**: `python3 led_cycle.py`

## GPIO Pin Assignments

| Component | GPIO Pin | Physical Pin |
| --------- | -------- | ------------ |
| Red LED   | GPIO 4   | Pin 7        |
| Green LED | GPIO 18  | Pin 12       |
| Blue LED  | GPIO 23  | Pin 16       |
| Button    | GPIO 2   | Pin 3        |
| Power     | 3.3V     | Pin 1        |
| Ground    | GND      | Pin 6        |

## How It Works

- **Red LED** is on by default when the program starts
- **Button press** cycles through: Red → Green → Blue → Red
- **Press Ctrl+C** to exit the program safely

## Files in This Project

- `instructions.md` - Complete project overview and hardware requirements
- `steps.md` - Detailed step-by-step wiring instructions
- `led_cycle.py` - Main program for LED cycling
- `test_hardware.py` - Hardware testing script (run this first!)
- `README.md` - This quick reference guide

## Troubleshooting

If something doesn't work:

1. Run `python3 test_hardware.py` to diagnose issues
2. Check your wiring against the diagrams in `steps.md`
3. Verify all connections are secure
4. Ensure LEDs are inserted with correct polarity (long leg = positive)

## Hardware Requirements

- Raspberry Pi (3, 4, or Zero with GPIO)
- 3x LEDs (Red, Green, Blue)
- 3x 330Ω resistors (for LEDs)
- 1x 10kΩ resistor (for button pull-down)
- 1x momentary push button
- Breadboards and jumper wires

---

**Ready to build? Start with the detailed instructions in `instructions.md`!**
