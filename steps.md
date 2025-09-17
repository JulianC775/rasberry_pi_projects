# Raspberry Pi 3-LED Cycle Project - Wiring Instructions

## Breadboard Setup Overview

### Hub Distribution Layout

- **Breadboard 1**: Power Supply Module + Button + Pi GPIO connections (Control Hub)
- **Breadboard 2**: Red LED circuit (powered from BB1)
- **Breadboard 3**: Green & Blue LED circuits (powered from BB1)
- **Power Flow**: BB1 (PSM) → BB2 & BB3 (direct hub distribution, no daisy-chaining)

---

## SECTION 1: Breadboard Power Distribution

### Step 1: Understanding Your Power Supply Module

Your breadboard power supply module typically has:

- **2x 3.3V pins** (usually labeled "3.3V" or "3V3")
- **2x 5V pins** (usually labeled "5V" or "VCC")
- **4x GND pins** (usually labeled "GND" or "-")
- **Power input** (barrel jack or screw terminals)
- **Power switch** and **voltage selection jumpers**

### Step 2: Configure Power Supply Module

- **Set voltage jumpers** to 3.3V position (check module documentation)
- **Connect power adapter** to module's input (usually 7-12V DC)
- **Turn on power switch** - LED indicators should light up
- **Verify 3.3V output** with multimeter if available

### Step 3: Mount Power Supply Module

- **Insert module** onto Breadboard 1 (usually fits on the side rails)
- **Alternative**: Place module next to breadboards if it doesn't fit

### Step 4: Connect Power Supply to Breadboards

- **3.3V Distribution**:

  - Use **red jumper wires** from **both 3.3V pins** on module to red power rails
  - Connect **Breadboard 1 red rail** to one 3.3V pin
  - Connect **Breadboard 2 red rail** to other 3.3V pin
  - Use **red jumper wire** to connect Breadboard 3 red rail to Breadboard 1 or 2

- **Ground Distribution**:
  - Use **black jumper wires** from **GND pins** on module to blue ground rails
  - Connect all 3 breadboard blue rails together
  - Use 2-3 GND pins from module for solid ground connections

### Step 5: Connect Pi Ground to Breadboard System

- **Common Ground**: **Male-to-female jumper wire** from Pi **GND (Pin 6)** to any blue ground rail
- **Purpose**: Creates common ground reference between Pi and breadboard circuits
- **Important**: This is the ONLY power-related connection between Pi and breadboards

---

## SECTION 2: LED Circuits (Distributed Across Boards)

### Step 6: Red LED Circuit (Breadboard 2)

- **Red LED Placement**:
  - **Long leg (anode)** → Row 10a (Breadboard 2)
  - **Short leg (cathode)** → Row 10b (Breadboard 2)
- **Current Limiting Resistor**: 330Ω from Row 10c to Row 12c
- **Ground Connection**: Male-to-male jumper wire from Row 12a to blue ground rail (BB2)
- **Control Connection**: Row 10e ready for Pi GPIO connection from BB1

### Step 7: Green LED Circuit (Breadboard 3)

- **Green LED Placement**:
  - **Long leg (anode)** → Row 15a (Breadboard 3)
  - **Short leg (cathode)** → Row 15b (Breadboard 3)
- **Current Limiting Resistor**: 330Ω from Row 15c to Row 17c
- **Ground Connection**: Male-to-male jumper wire from Row 17a to blue ground rail (BB3)
- **Control Connection**: Row 15e ready for Pi GPIO connection from BB1

### Step 8: Blue LED Circuit (Breadboard 3)

- **Blue LED Placement**:
  - **Long leg (anode)** → Row 20a (Breadboard 3)
  - **Short leg (cathode)** → Row 20b (Breadboard 3)
- **Current Limiting Resistor**: 330Ω from Row 20c to Row 22c
- **Ground Connection**: Male-to-male jumper wire from Row 22a to blue ground rail (BB3)
- **Control Connection**: Row 20e ready for Pi GPIO connection from BB1

---

## SECTION 3: Button Circuit (Breadboard 1)

### Step 9: Push Button Setup

- **Button Placement**: 4-pin button spanning center gap
  - Pins in rows 25e, 25f, 27e, 27f (Breadboard 1)
- **Purpose**: Input device to cycle through LED states

### Step 10: Button Pull-down Circuit

- **Pull-down Resistor**: 10kΩ from Row 24b to Row 26b (Breadboard 1)
- **Ground Connection**: Male-to-male jumper wire from Row 26a to blue ground rail
- **Input Wire**: Male-to-male jumper wire from Row 24a to Row 25c (connects to button)
- **Purpose**: Ensures clean digital signal (LOW when not pressed, HIGH when pressed)

### Step 11: Button Power Connection

- **Power Wire**: Male-to-male jumper wire from Row 25g to red power rail
- **Purpose**: Provides 3.3V to button when pressed

### Step 12: Button Input Signal

- **Signal Wire**: Male-to-male jumper wire from Row 24c to Row 30a (Breadboard 1)
- **Purpose**: Creates connection point for Pi GPIO input wire

---

## SECTION 4: Raspberry Pi GPIO Connections

### Step 13: Pi GPIO Pin Assignments

#### LED Control Pins (Digital Output)

- **GPIO 18 (Pin 12)** → Red LED control
- **GPIO 24 (Pin 18)** → Green LED control
- **GPIO 25 (Pin 22)** → Blue LED control

#### Button Input Pin (Digital Input)

- **GPIO 2 (Pin 3)** → Button input signal

### Step 14: Final Pi GPIO Wiring

Connect **Male-to-female jumper wires** from Raspberry Pi to breadboards:

#### Signal Connections Only (Power comes from power supply module)

- **Pi Pin 6 (GND)** → BB1 blue ground rail (common ground - already done in Step 5)
- **Pi Pin 12 (GPIO 18)** → BB2, Row 10e (Red LED control)
- **Pi Pin 18 (GPIO 24)** → BB3, Row 15e (Green LED control)
- **Pi Pin 22 (GPIO 25)** → BB3, Row 20e (Blue LED control)
- **Pi Pin 3 (GPIO 2)** → BB1, Row 30b (Button input signal)

#### Hub Distribution Benefits:

- **Clean signal routing** - each LED gets dedicated control wire
- **Easy troubleshooting** - isolate problems by breadboard
- **Professional layout** - organized like real electronics projects
- **NO power wires** from Pi - PSM handles all power safely
- **Expandable design** - easy to add more LEDs/features later

---

## SECTION 5: Connection Verification

### Step 15: Power System Check

1. **Visual Inspection**: Verify all power rails connected (red-to-red, blue-to-blue)
2. **Power Module**: Confirm power supply module 3.3V pins connect to red power rails
3. **Ground System**: Check power module GND pins and Pi GND connect to blue ground rails
4. **LED Grounds**: Check all LED cathode circuits connect to ground rail
5. **Button Ground**: Verify button pull-down resistor connects to ground

### Step 16: Signal Path Verification

1. **LED Controls**: Trace each GPIO pin to corresponding LED anode
2. **Button Input**: Verify GPIO 2 connects to button input circuit
3. **Resistor Placement**: Confirm all resistors are in correct positions
4. **No Short Circuits**: Ensure no unintended connections between 3.3V and ground

---

## Raspberry Pi GPIO Pin Summary

```python
# Pin definitions for Python code
RED_LED_PIN = 18      # Physical pin 12 → Red LED
GREEN_LED_PIN = 24    # Physical pin 18 → Green LED
BLUE_LED_PIN = 25     # Physical pin 22 → Blue LED
BUTTON_PIN = 2        # Physical pin 3 → Button input
```

### Physical Pin Layout Reference

```
Pi GPIO Header (looking at Pi from above):
    3.3V  [ 1] [ 2]  5V
   GPIO2  [ 3] [ 4]  5V
   GPIO3  [ 5] [ 6]  GND
   GPIO4  [ 7] [ 8]  GPIO14
     GND  [ 9] [10]  GPIO15
  GPIO17  [11] [12]  GPIO18  ← Red LED
  GPIO27  [13] [14]  GND
  GPIO22  [15] [16]  GPIO23
    3.3V  [17] [18]  GPIO24  ← Green LED
  GPIO10  [19] [20]  GND
   GPIO9  [21] [22]  GPIO25  ← Blue LED
  GPIO11  [23] [24]  GPIO8
     GND  [25] [26]  GPIO7
```

## Component Layout Summary

### Breadboard 1: Power & Button

- **Power distribution** from Pi to all breadboards
- **Rows 24-26**: Button input circuit with 10kΩ pull-down
- **Rows 25-27**: Push button placement
- **Row 30**: Button signal connection point

### Breadboard 2: LED Circuits

- **Rows 10-12**: Red LED + 330Ω resistor + ground
- **Rows 15-17**: Green LED + 330Ω resistor + ground
- **Rows 20-22**: Blue LED + 330Ω resistor + ground

### Breadboard 3: Expansion Space

- Available for future components
- Connected to power/ground rails
- Space for sensors, displays, or additional circuits

## Expected Behavior After Wiring

- **Before Python code**: All LEDs OFF when Pi is powered
- **Button has no effect** until Python program is running
- **Pi boots normally** with green power LED on Pi board
- **No smoke, sparks, or heat** indicates successful wiring

---

## Troubleshooting Common Wiring Issues

### LEDs Don't Light Up

- **Check LED polarity**: Long leg = anode = positive side
- **Verify 330Ω resistors** are in the circuit
- **Confirm ground connections** to blue ground rail
- **Test with multimeter**: Should read ~3.3V from anode to ground

### Button Doesn't Respond

- **Check 4-pin button orientation** across center gap
- **Verify 10kΩ pull-down resistor** placement
- **Confirm GPIO 2 connection** from Pi Pin 3
- **Test button continuity** with multimeter

### Power Issues

- **Ensure Pi 3.3V** connects to red power rail
- **Check all ground connections** to blue ground rail
- **Verify breadboard interconnections** (rail-to-rail jumpers)
- **Measure voltage**: Should read 3.3V on power rails

### Pi Won't Boot

- **Check power supply** (proper Pi power adapter)
- **Verify no short circuits** between 3.3V and ground
- **Remove all connections** and test Pi alone first

## Testing Individual Components

### Test LEDs Individually

```bash
# Test Red LED
python3 -c "from gpiozero import LED; led=LED(18); led.on(); input('Press Enter'); led.off()"

# Test Green LED
python3 -c "from gpiozero import LED; led=LED(24); led.on(); input('Press Enter'); led.off()"

# Test Blue LED
python3 -c "from gpiozero import LED; led=LED(25); led.on(); input('Press Enter'); led.off()"
```

### Test Button

```bash
# Test Button (press button while running)
python3 -c "from gpiozero import Button; btn=Button(2); print('Press button...'); btn.wait_for_press(); print('Button pressed!')"
```

**Ready for Python code!** 🐍🔴🟢🔵
