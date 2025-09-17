# ESP32 3-LED Cycle Project - Wiring Instructions

## Breadboard Setup Overview

### Layout Plan

- **Breadboard 1**: ESP32 mounting and power distribution
- **Breadboard 2**: LED circuits (Red, Green, Blue)
- **Breadboard 3**: Button circuit and additional space
- **Connections**: Link breadboards with jumper wires for power/ground

---

## SECTION 1: Breadboard Power Distribution

### Step 1: Connect Breadboards Together

- **Power Rails**: Connect red power rails of all 3 breadboards with red jumper wires
- **Ground Rails**: Connect blue ground rails of all 3 breadboards with black jumper wires
- **Purpose**: Creates unified power distribution across all breadboards

### Step 2: ESP32 Power Setup (Breadboard 1)

- **ESP32 Placement**: Insert ESP32 dev board across center gap of Breadboard 1
- **3.3V Connection**: Wire from ESP32 3.3V pin to red power rail (Breadboard 1)
- **Ground Connection**: Wire from ESP32 GND pin to blue ground rail (Breadboard 1)
- **Purpose**: Powers all breadboards from ESP32's regulated 3.3V

---

## SECTION 2: LED Circuits (Breadboard 2)

### Step 3: Red LED Circuit

- **Red LED Placement**:
  - Long leg (anode) → Row 10a (Breadboard 2)
  - Short leg (cathode) → Row 10b (Breadboard 2)
- **Current Limiting Resistor**: 330Ω from Row 10c to Row 12c
- **Ground Connection**: Jumper wire from Row 12a to blue ground rail
- **Control Wire**: Jumper wire from Row 10e to ESP32 GPIO pin (will specify later)

### Step 4: Green LED Circuit

- **Green LED Placement**:
  - Long leg (anode) → Row 15a (Breadboard 2)
  - Short leg (cathode) → Row 15b (Breadboard 2)
- **Current Limiting Resistor**: 330Ω from Row 15c to Row 17c
- **Ground Connection**: Jumper wire from Row 17a to blue ground rail
- **Control Wire**: Jumper wire from Row 15e to ESP32 GPIO pin (will specify later)

### Step 5: Blue LED Circuit

- **Blue LED Placement**:
  - Long leg (anode) → Row 20a (Breadboard 2)
  - Short leg (cathode) → Row 20b (Breadboard 2)
- **Current Limiting Resistor**: 330Ω from Row 20c to Row 22c
- **Ground Connection**: Jumper wire from Row 22a to blue ground rail
- **Control Wire**: Jumper wire from Row 20e to ESP32 GPIO pin (will specify later)

---

## SECTION 3: Button Circuit (Breadboard 3)

### Step 6: Push Button Setup

- **Button Placement**: 4-pin button spanning center gap
  - Pins in rows 5e, 5f, 7e, 7f (Breadboard 3)
- **Purpose**: Input device to cycle through LED states

### Step 7: Button Pull-down Circuit

- **Pull-down Resistor**: 10kΩ from Row 4b to Row 6b
- **Ground Connection**: Jumper wire from Row 6a to blue ground rail
- **Input Wire**: Jumper wire from Row 4a to Row 5c (connects to button)
- **Purpose**: Ensures clean digital signal (LOW when not pressed)

### Step 8: Button Power Connection

- **Power Wire**: Jumper wire from Row 7g to red power rail
- **Purpose**: Provides 3.3V to button when pressed

---

## SECTION 4: ESP32 Connections

### Step 9: ESP32 GPIO Pin Assignments

#### LED Control Pins (Digital Output)

- **GPIO 18** → Red LED control (Row 10e, Breadboard 2)
- **GPIO 19** → Green LED control (Row 15e, Breadboard 2)
- **GPIO 21** → Blue LED control (Row 20e, Breadboard 2)

#### Button Input Pin (Digital Input)

- **GPIO 4** → Button input signal (Row 4c, Breadboard 3)

### Step 10: Final ESP32 Wiring

- **Male-to-Female jumper wires** from ESP32 to breadboard connections:
  - ESP32 GPIO 18 → Breadboard 2, Row 10e (Red LED)
  - ESP32 GPIO 19 → Breadboard 2, Row 15e (Green LED)
  - ESP32 GPIO 21 → Breadboard 2, Row 20e (Blue LED)
  - ESP32 GPIO 4 → Breadboard 3, Row 4c (Button input)

---

## SECTION 5: Connection Verification

### Step 11: Power System Check

1. **Visual Inspection**: Verify all power rails are connected (red-to-red, blue-to-blue)
2. **ESP32 Power**: Confirm 3.3V and GND connections from ESP32 to rails
3. **LED Grounds**: Check all LED cathode circuits connect to ground rail
4. **Button Ground**: Verify button pull-down resistor connects to ground

### Step 12: Signal Path Verification

1. **LED Controls**: Trace each GPIO pin to corresponding LED anode
2. **Button Input**: Verify GPIO 4 connects to button input circuit
3. **Resistor Placement**: Confirm all resistors are in correct positions
4. **No Short Circuits**: Ensure no unintended connections between power and ground

---

## GPIO Pin Summary for Arduino Code

```cpp
// Pin definitions for Arduino code
#define RED_LED_PIN    18
#define GREEN_LED_PIN  19
#define BLUE_LED_PIN   21
#define BUTTON_PIN     4
```

## Component Layout Summary

### Breadboard 1: ESP32 & Power

- ESP32 development board
- Power distribution connections

### Breadboard 2: LED Circuits

- **Rows 10-12**: Red LED + 330Ω resistor + ground
- **Rows 15-17**: Green LED + 330Ω resistor + ground
- **Rows 20-22**: Blue LED + 330Ω resistor + ground

### Breadboard 3: Button Circuit

- **Rows 4-6**: Button input circuit with 10kΩ pull-down
- **Rows 5-7**: Push button placement

## Expected Behavior After Wiring

- All LEDs should be OFF when ESP32 is powered (before code upload)
- Button should have no effect until Arduino code is uploaded
- ESP32 built-in LED may blink during programming
- No smoke, sparks, or heat indicates successful wiring

---

## Troubleshooting Common Wiring Issues

### LEDs Don't Light Up

- Check LED polarity (long leg = anode = positive)
- Verify 330Ω resistors are in circuit
- Confirm ground connections

### Button Doesn't Respond

- Check 4-pin button orientation
- Verify 10kΩ pull-down resistor placement
- Confirm GPIO 4 connection

### Power Issues

- Ensure ESP32 3.3V connects to red power rail
- Check all ground connections to blue ground rail
- Verify breadboard interconnections

**Ready for Arduino code upload!** 🚀
