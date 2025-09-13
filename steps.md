# Button-Controlled 3-LED Cycle Project

## Complete Circuit Build - 3 LEDs + Button:

### Step 1: Insert RED LED (Left)

- **RED LED long leg (anode)** → Row 5a
- **RED LED short leg (cathode)** → Row 5b
- **Purpose**: Left LED - Red color

### Step 2: Insert GREEN LED (Center)

- **GREEN LED long leg (anode)** → Row 10a
- **GREEN LED short leg (cathode)** → Row 10b
- **Purpose**: Center LED - Green color

### Step 3: Insert BLUE LED (Right)

- **BLUE LED long leg (anode)** → Row 15a
- **BLUE LED short leg (cathode)** → Row 15b
- **Purpose**: Right LED - Blue color

### Step 4: Add LED Resistors

- **330Ω resistor** → From 5c to 7c (RED LED)
- **330Ω resistor** → From 10c to 12c (GREEN LED)
- **330Ω resistor** → From 15c to 17c (BLUE LED)
- **Purpose**: Current limiting for each LED

### Step 5: LED Ground Connections

- **Male-to-male jumper wire** → From 7a to blue ground rail (RED LED)
- **Male-to-male jumper wire** → From 12a to blue ground rail (GREEN LED)
- **Male-to-male jumper wire** → From 17a to blue ground rail (BLUE LED)
- **Purpose**: Common ground for all LEDs

### Step 6: Insert Button

- **4-pin button** → Legs in 25e, 27e, 25f, 27f (spans 2 rows and center gap)
- **Purpose**: Cycles through LEDs

### Step 7: Pi Power to Breadboard

- **Male-to-female jumper wire** → From Pi 3.3V (pin 1) to red power rail (any hole)
- **Male-to-female jumper wire** → From Pi GND (pin 6) to blue ground rail (any hole)
- **Purpose**: Powers breadboard rails from Pi instead of PSU

### Step 8: Button Power Connection

- **Male-to-male jumper wire** → From 25g to red power rail (any hole)
- **Purpose**: Connects button to Pi's 3.3V via power rail

### Step 9: Button Input Wire

- **Male-to-male jumper wire** → From 24a to 25c
- **Purpose**: Connects input circuit to left side of button

### Step 10: Pull-down Resistor

- **10kΩ resistor** → From 24b to 26b
- **Purpose**: Pulls input LOW when button not pressed

### Step 11: Pull-down Ground

- **Male-to-male jumper wire** → From 26a to blue ground rail (any hole)
- **Purpose**: Completes pull-down resistor to ground

### Step 12: Pi LED Controls

- **Male-to-female jumper wire** → From Pi GPIO18 (pin 12) to 5e (RED LED)
- **Male-to-female jumper wire** → From Pi GPIO24 (pin 18) to 10e (GREEN LED)
- **Male-to-female jumper wire** → From Pi GPIO25 (pin 22) to 15e (BLUE LED)
- **Purpose**: Pi controls each LED individually

### Step 13: Pi Button Input

- **Male-to-female jumper wire** → From Pi GPIO2 (pin 3) to 24c
- **Purpose**: Pi reads button press to cycle LEDs

## GPIO Pin Summary:

- **Pin 1**: 3.3V → Red power rail
- **Pin 3**: GPIO2 → Button input (24c)
- **Pin 6**: GND → Blue ground rail
- **Pin 12**: GPIO18 → RED LED (5e)
- **Pin 18**: GPIO24 → GREEN LED (10e)
- **Pin 22**: GPIO25 → BLUE LED (15e)

## Component Layout (Much More Spaced Out):

- **Rows 5-7**: RED LED + resistor + ground
- **Rows 10-12**: GREEN LED + resistor + ground
- **Rows 15-17**: BLUE LED + resistor + ground
- **Rows 24-26**: Button input circuit
- **Rows 25-27**: Button placement

## Ready for Python Code!
