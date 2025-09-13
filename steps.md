# Button-Controlled 3-LED Cycle Project

## Complete Circuit Build - 3 LEDs + Button:

### Step 1: Insert RED LED (Left)

- **RED LED long leg (anode)** → Row 1a
- **RED LED short leg (cathode)** → Row 1b
- **Purpose**: Left LED - Red color

### Step 2: Insert GREEN LED (Center)

- **GREEN LED long leg (anode)** → Row 3a
- **GREEN LED short leg (cathode)** → Row 3b
- **Purpose**: Center LED - Green color

### Step 3: Insert BLUE LED (Right)

- **BLUE LED long leg (anode)** → Row 5a
- **BLUE LED short leg (cathode)** → Row 5b
- **Purpose**: Right LED - Blue color

### Step 4: Add LED Resistors

- **330Ω resistor** → From 1c to 2c (RED LED)
- **330Ω resistor** → From 3c to 4c (GREEN LED)
- **330Ω resistor** → From 5c to 6c (BLUE LED)
- **Purpose**: Current limiting for each LED

### Step 5: LED Ground Connections

- **Male-to-male jumper wire** → From 2a to blue ground rail (RED LED)
- **Male-to-male jumper wire** → From 4a to blue ground rail (GREEN LED)
- **Male-to-male jumper wire** → From 6a to blue ground rail (BLUE LED)
- **Purpose**: Common ground for all LEDs

### Step 6: Insert Button

- **4-pin button** → Legs in 10e, 12e, 10f, 12f (spans 2 rows and center gap)
- **Purpose**: Cycles through LEDs

### Step 7: Pi Power to Breadboard

- **Male-to-female jumper wire** → From Pi 3.3V (pin 1) to red power rail (any hole)
- **Male-to-female jumper wire** → From Pi GND (pin 6) to blue ground rail (any hole)
- **Purpose**: Powers breadboard rails from Pi instead of PSU

### Step 8: Button Power Connection

- **Male-to-male jumper wire** → From 10g to red power rail (any hole)
- **Purpose**: Connects button to Pi's 3.3V via power rail

### Step 9: Button Input Wire

- **Male-to-male jumper wire** → From 9c to 10c
- **Purpose**: Connects input circuit to left side of button

### Step 10: Pull-down Resistor

- **10kΩ resistor** → From 9c to 11c
- **Purpose**: Pulls input LOW when button not pressed

### Step 11: Pull-down Ground

- **Male-to-male jumper wire** → From 11a to blue ground rail (any hole)
- **Purpose**: Completes pull-down resistor to ground

### Step 12: Pi LED Controls

- **Male-to-female jumper wire** → From Pi GPIO18 (pin 12) to 1e (RED LED)
- **Male-to-female jumper wire** → From Pi GPIO24 (pin 18) to 3e (GREEN LED)
- **Male-to-female jumper wire** → From Pi GPIO25 (pin 22) to 5e (BLUE LED)
- **Purpose**: Pi controls each LED individually

### Step 13: Pi Button Input

- **Male-to-female jumper wire** → From Pi GPIO2 (pin 3) to 9c
- **Purpose**: Pi reads button press to cycle LEDs

## GPIO Pin Summary:

- **Pin 1**: 3.3V → Red power rail
- **Pin 3**: GPIO2 → Button input (9c)
- **Pin 6**: GND → Blue ground rail
- **Pin 12**: GPIO18 → RED LED (1e)
- **Pin 18**: GPIO24 → GREEN LED (3e)
- **Pin 22**: GPIO25 → BLUE LED (5e)

## Component Layout:

- **Rows 1-2**: RED LED + resistor + ground
- **Rows 3-4**: GREEN LED + resistor + ground
- **Rows 5-6**: BLUE LED + resistor + ground
- **Rows 9-11**: Button input circuit
- **Rows 10-12**: Button placement

## Ready for Python Code!
