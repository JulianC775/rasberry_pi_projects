# Raspberry Pi 3-LED Cycle - Hardware Wiring Steps

## Overview

This guide will walk you through wiring 3 LEDs and a button to your Raspberry Pi for a cycling LED project. The system will:

- Start with the Red LED on
- Cycle through Red → Green → Blue → Red when button is pressed
- Use multiple breadboards for organized layout

## GPIO Pin Assignments

| Component  | GPIO Pin | Physical Pin | Wire Color (Suggested) |
| ---------- | -------- | ------------ | ---------------------- |
| Red LED    | GPIO 4   | Pin 7        | Red                    |
| Green LED  | GPIO 18  | Pin 12       | Green                  |
| Blue LED   | GPIO 23  | Pin 16       | Blue                   |
| Button     | GPIO 2   | Pin 3        | Yellow                 |
| 3.3V Power | -        | Pin 1        | Red (Power)            |
| Ground     | -        | Pin 6        | Black (Ground)         |

## Step-by-Step Wiring Instructions

### Step 1: Prepare Your Workspace

1. **Power off** your Raspberry Pi completely
2. Set up 3 breadboards side by side
3. Connect breadboards together using jumper wires:
   - Connect power rails (+) across all 3 breadboards
   - Connect ground rails (-) across all 3 breadboards

### Step 2: Power Distribution Setup

1. **Main Power Connection (Breadboard 1)**:

   - Connect Pi Pin 1 (3.3V) to breadboard 1 positive rail (red line)
   - Connect Pi Pin 6 (GND) to breadboard 1 negative rail (blue/black line)

2. **Power Bridge to Other Breadboards**:
   - Use red jumper wire to connect positive rails: Breadboard 1 → Breadboard 2
   - Use red jumper wire to connect positive rails: Breadboard 2 → Breadboard 3
   - Use black jumper wire to connect negative rails: Breadboard 1 → Breadboard 2
   - Use black jumper wire to connect negative rails: Breadboard 2 → Breadboard 3

### Step 3: LED Circuit Setup

**Breadboard 1 - Red LED Circuit**:

1. Insert Red LED in breadboard 1:
   - Long leg (anode) in row 10, column E
   - Short leg (cathode) in row 11, column E
2. Insert 330Ω resistor:
   - One end in row 10, column F (same row as LED anode)
   - Other end in positive power rail
3. Connect LED cathode to ground:
   - Jumper wire from row 11, column F to negative power rail
4. Connect to Raspberry Pi:
   - Jumper wire from Pi GPIO 4 (Pin 7) to row 10, column A

**Breadboard 2 - Green LED Circuit**:

1. Insert Green LED in breadboard 2:
   - Long leg (anode) in row 10, column E
   - Short leg (cathode) in row 11, column E
2. Insert 330Ω resistor:
   - One end in row 10, column F (same row as LED anode)
   - Other end in positive power rail
3. Connect LED cathode to ground:
   - Jumper wire from row 11, column F to negative power rail
4. Connect to Raspberry Pi:
   - Jumper wire from Pi GPIO 18 (Pin 12) to row 10, column A

**Breadboard 3 - Blue LED Circuit**:

1. Insert Blue LED in breadboard 3:
   - Long leg (anode) in row 10, column E
   - Short leg (cathode) in row 11, column E
2. Insert 330Ω resistor:
   - One end in row 10, column F (same row as LED anode)
   - Other end in positive power rail
3. Connect LED cathode to ground:
   - Jumper wire from row 11, column F to negative power rail
4. Connect to Raspberry Pi:
   - Jumper wire from Pi GPIO 23 (Pin 16) to row 10, column A

### Step 4: Button Circuit Setup (Breadboard 1)

1. **Insert Push Button**:

   - Place 4-pin push button across the center divide of breadboard 1
   - Button legs should be in rows 15-16, columns E and F

2. **Button Pull-down Resistor**:

   - Insert 10kΩ resistor from button pin (row 15, column A) to negative power rail

3. **Button Connections**:
   - Connect one button pin (row 15, column A) to Pi GPIO 2 (Pin 3)
   - Connect other button pin (row 16, column A) to positive power rail (3.3V)

### Step 5: Final Connection Check

**Power Connections**:

- [ ] Pi Pin 1 (3.3V) → Breadboard 1 positive rail
- [ ] Pi Pin 6 (GND) → Breadboard 1 negative rail
- [ ] All breadboards have connected power rails

**LED Connections**:

- [ ] Red LED: Pi GPIO 4 → Resistor → LED → Ground
- [ ] Green LED: Pi GPIO 18 → Resistor → LED → Ground
- [ ] Blue LED: Pi GPIO 23 → Resistor → LED → Ground

**Button Connections**:

- [ ] Pi GPIO 2 → Button → 3.3V
- [ ] Button → 10kΩ resistor → Ground

## Circuit Diagram (Text Representation)

```
Raspberry Pi GPIO Layout:
    3.3V (Pin 1) ●─────┐
    GPIO 2 (Pin 3) ●───┼─── Button ─── 3.3V
    GND (Pin 6) ●──────┼─── Ground Rails
    GPIO 4 (Pin 7) ●──┼─── Red LED Circuit
    GPIO 18 (Pin 12) ●─┼─── Green LED Circuit
    GPIO 23 (Pin 16) ●─┘    Blue LED Circuit

LED Circuit (each LED):
GPIO Pin → 330Ω Resistor → LED Anode → LED Cathode → Ground

Button Circuit:
GPIO 2 → Button → 3.3V
       └─ 10kΩ Resistor → Ground
```

## Safety Check Before Power-On

1. **Visual Inspection**:

   - All LEDs inserted with correct polarity (long leg to resistor/positive)
   - No loose wires or short circuits
   - All resistors properly placed

2. **Connection Verification**:

   - Use multimeter to check continuity if available
   - Ensure no GPIO pins are accidentally connected to 5V
   - Verify ground connections are solid

3. **Component Check**:
   - 330Ω resistors for LEDs (Orange-Orange-Brown-Gold bands)
   - 10kΩ resistor for button (Brown-Black-Orange-Gold bands)
   - Button is momentary type (springs back when released)

## Troubleshooting Common Issues

**LEDs Not Lighting**:

- Check LED polarity (long leg = anode = positive)
- Verify resistor connections
- Test with multimeter for continuity

**Button Not Responding**:

- Check pull-down resistor (10kΩ) connection
- Verify button is momentary type
- Test button with multimeter for continuity when pressed

**Power Issues**:

- Ensure Pi is properly powered
- Check all power rail connections between breadboards
- Verify 3.3V is reaching all breadboards

---

**Next Step**: Once wiring is complete, proceed to upload and run the Python code for LED cycling functionality.
