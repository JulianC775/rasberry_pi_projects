# Button-Controlled 3-LED Cycle Project

## Complete Circuit Build - 3 LEDs + Button:

### Step 1: Insert RED LED (Left)

- **RED LED long leg (anode)** → Row 15a
- **RED LED short leg (cathode)** → Row 15b
- **Purpose**: Left LED - Red color

### Step 2: Insert GREEN LED (Center)

- **GREEN LED long leg (anode)** → Row 17a
- **GREEN LED short leg (cathode)** → Row 17b
- **Purpose**: Center LED - Green color

### Step 3: Insert BLUE LED (Right)

- **BLUE LED long leg (anode)** → Row 19a
- **BLUE LED short leg (cathode)** → Row 19b
- **Purpose**: Right LED - Blue color

### Step 4: Add LED Resistors

- **330Ω resistor** → From 15c to 16c (RED LED)
- **330Ω resistor** → From 17c to 18c (GREEN LED)
- **330Ω resistor** → From 19c to 20c (BLUE LED)
- **Purpose**: Current limiting for each LED

### Step 5: LED Ground Connections

- **Male-to-male jumper wire** → From 16a to blue ground rail (RED LED)
- **Male-to-male jumper wire** → From 18a to blue ground rail (GREEN LED)
- **Male-to-male jumper wire** → From 20a to blue ground rail (BLUE LED)
- **Purpose**: Common ground for all LEDs

### Step 6: Insert Button

- **4-pin button** → Legs in 25e, 27e, 25f, 27f (spans 2 rows and center gap)
- **Purpose**: Cycles through LEDs

### Step 7: Button Power Connection

- **Male-to-male jumper wire** → From 25g to red power rail (any hole)
- **Purpose**: Provides +3.3V to right side of button

### Step 8: Button Input Wire

- **Male-to-male jumper wire** → From 24c to 25c
- **Purpose**: Connects input circuit to left side of button

### Step 9: Pull-down Resistor

- **10kΩ resistor** → From 24c to 26d
- **Purpose**: Pulls input LOW when button not pressed

### Step 10: Pull-down Ground

- **Male-to-male jumper wire** → From 26a to blue ground rail (any hole)
- **Purpose**: Completes pull-down resistor to ground

### Step 11: Pi LED Controls

- **Male-to-female jumper wire** → From Pi GPIO18 (pin 12) to 15e (RED LED)
- **Male-to-female jumper wire** → From Pi GPIO24 (pin 18) to 17e (GREEN LED)
- **Male-to-female jumper wire** → From Pi GPIO25 (pin 22) to 19e (BLUE LED)
- **Purpose**: Pi controls each LED individually

### Step 12: Pi Button Input

- **Male-to-female jumper wire** → From Pi GPIO2 (pin 3) to 24c
- **Purpose**: Pi reads button press to cycle LEDs

## Current Status:

- All connections now use 24c as the common input point ✅
- No conflicts - everything connects properly at 24c
