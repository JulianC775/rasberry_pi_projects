# Button-LED Circuit Build Steps

## Complete Circuit Build - Starting Row 20:

### Step 1: Insert LED

- **LED long leg (anode)** → Row 20a
- **LED short leg (cathode)** → Row 20b
- **Purpose**: LED placement for control

### Step 2: Add LED Current-Limiting Resistor

- **330Ω resistor** → From 20c to 22c
- **Purpose**: Limits current to protect LED from burning out

### Step 3: LED Power Connection (REMOVED)

- ~~Male-to-male jumper from 20e to red power rail~~
- **REMOVED**: Pi will control LED power instead

### Step 4: LED Ground Connection

- **Male-to-male jumper** → From 22a to blue ground rail (any hole)
- **Purpose**: Completes LED circuit through resistor to ground

### Step 5: Insert Button

- **4-pin button** → Legs in 25e, 27e, 25f, 27f (spans 2 rows and center gap)
- **Purpose**: Physical switch to control circuit

### Step 6: Button Power Connection

- **Male-to-male jumper** → From 25g to red power rail (any hole)
- **Purpose**: Provides +3.3V to right side of button (connects to 25f internally)

### Step 7: Button Input Wire

- **Male-to-male jumper** → From 24d to 25c
- **Purpose**: Connects input circuit to left side of button (connects to 25e internally)

### Step 8: Pull-down Resistor

- **10kΩ resistor** → From 24d to 26d
- **Purpose**: Pulls input LOW when button not pressed

### Step 9: Pull-down Ground

- **Male-to-male jumper** → From 26a to blue ground rail (any hole)
- **Purpose**: Completes pull-down resistor to ground

### Step 10: Pi LED Control

- **Male-to-female jumper** → From Pi GPIO18 (pin 12) to 20e
- **Purpose**: Pi controls LED on/off

### Step 11: Pi Button Input

- **Male-to-female jumper** → From Pi GPIO2 (pin 3) to 24b
- **Purpose**: Pi reads button press state

## Current Status:

- 24d: Has jumper to 25c AND 10kΩ resistor to 26d ⚠️ **CONFLICT!**

## Issues to Fix:

- 24d cannot have both the jumper AND resistor - need different approach
