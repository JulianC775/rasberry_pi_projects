# Power Supply Testing - Single Breadboard (BB1)

## Breadboard Configuration

### **Your Breadboard Layout (Vertical):**

```
Rows 1-65, Columns A-J (with center gap), Power rails on both sides

Left Power Rails    Main Area (A-J)    Right Power Rails
   + (1-65)         A B C D E | F G H I J    + (1-65)
   - (1-65)         A B C D E | F G H I J    - (1-65)

Power Supply Module (PSU):
- Mounted at bottom (Rows 57-65)
- Connected to power rails (not in A-J columns)
- Provides 3.3V and GND to all power rail holes
```

### **Available Space for Circuits:**

- **Rows 1-56**: Free for LED circuits, button, Pi connections
- **Rows 57-65**: PSU mounted (avoid these rows for components)
- **Power rails**: Always available for power/ground connections

## Overview

Let's test your power supply module on just Breadboard 1 to verify everything works. This uses minimal wires and proves your power system is ready. You can build your entire 3-LED cycling project on this single breadboard!

## Safety First ⚠️

- **Always disconnect power** when making wiring changes
- **Double-check polarity** before connecting power
- **Start with one LED** before testing multiple
- **Use proper resistor values** to protect LEDs

---

## Single Breadboard Setup

### **Your Layout:**

- **Breadboard 1**: Power Supply Module (PSM) + All LED circuits + Button
- **Simple and clean** - everything in one place
- **Minimal wiring** - saves your jumper wires

### **Power Flow:**

```
PSM (bottom of BB1) → BB1 Power Rails → LED Circuits
```

## Test Components Needed

- **1x Test LED** (any color - just to verify power)
- **1x 330Ω Resistor**
- **Jumper Wires Needed:**
  - **2x Male-to-male** (any color) for LED test circuit
  - **1x Male-to-female** (black) for Pi ground connection (later)
- **Your power supply module** (already mounted on BB1)

**Total: Only 3 wires needed!**

---

## POWER TEST - Single Breadboard

### Step 1: Configure Power Supply Module (BB1)

- **PSM mounted** at bottom of Breadboard 1 (vertical)
- **Remove both 3.3V jumpers** (uncover both 3.3V outputs)
- **Keep 5V jumpers covered** (safety)
- **Set to 3.3V** and connect power adapter
- **Keep power switch OFF**

### Step 2: PSU is Already Connected!

**Your PSU is already inserted into the breadboard power rails - no additional wiring needed!**

```
PSU Status:
✅ PSU 3.3V → Breadboard power rails (already connected)
✅ PSU GND → Breadboard ground rails (already connected)
✅ Power distribution ready - no wires needed!
```

**Note**: Since your PSU is mounted in the breadboard, it automatically powers all the power rail holes!

### Step 3: Test Basic Power

1. **Turn on PSU** (power switch on your PSU module)
2. **Check power indicators** on PSU - should light up
3. **Measure voltage** (if you have multimeter): ~3.3V between red/blue rails
4. **Success!** BB1 has power from your mounted PSU

---

## LED TEST - Verify Power Works

### Step 4: Create Simple LED Test Circuit

**Power OFF while wiring!**

```
BB1 LED Test Circuit - Use MALE-TO-MALE wires:
1) Left Red Rail → Row 10a (RED male-to-male wire) - Brings 3.3V power to circuit
2) Row 10b → 330Ω resistor → Row 10c - Current limiting protection for LED
3) Row 10d → LED long leg (anode) - Connects to LED positive side
4) Row 10e → LED short leg (cathode) - Connects to LED negative side
5) Row 10f → Left Blue Rail (BLACK male-to-male wire) - Completes circuit to ground
```

### Step 5: Test LED Power

1. **Double-check LED polarity** (long leg = anode = positive)
2. **Turn on PSM**
3. **LED should light up** - bright but not blinding
4. **Success!** Your power system works perfectly

---

## RASPBERRY PI INTEGRATION

### Step 6: Add Pi Ground Connection

**Power OFF while connecting Pi!**

```
Pi Ground Connection - Use MALE-TO-FEMALE wire:
Pi GND (Pin 6) → BB1 Left Blue Rail (BLACK male-to-female wire)
```

### Step 7: Test Pi + Power System

1. **Boot Raspberry Pi** (with its own power adapter)
2. **Turn on PSM**
3. **LED should still work** normally
4. **Pi should boot normally**
5. **Test Pi GPIO** (optional):
   ```bash
   python3 -c "from gpiozero import LED; led=LED(2); led.on(); print('Pi working!')"
   ```

---

## SUCCESS! ✅

### **What You've Proven:**

✅ **PSM works** and provides stable 3.3V power  
✅ **LED circuits work** with proper current limiting  
✅ **Pi integrates safely** with common ground  
✅ **Foundation is solid** for your main project

### **Wire Count Used:**

- **2x Male-to-male** for power (red + black)
- **2x Male-to-male** for LED circuit
- **1x Male-to-female** for Pi ground
- **Total: 5 wires** - very manageable!

## Ready for Main Project! 🚀

Your single-breadboard power system is tested and ready. You can now build your complete 3-LED cycling project on BB1:

### **BB1 Layout for Main Project:**

```
Bottom: [Power Supply Module]
Middle: [Red LED] [Green LED] [Blue LED] [Button Circuit]
Top: [Pi GPIO connections]
```

### **Advantages of Single Breadboard:**

✅ **Simple wiring** - everything in one place  
✅ **Easy troubleshooting** - all circuits visible  
✅ **Saves jumper wires** - no inter-board connections  
✅ **Faster to build** - less complexity  
✅ **Still professional** - clean, organized layout

## Next Steps

1. **Keep your test LED** as a power indicator
2. **Follow main project wiring** in `steps.md` (adapted for single board)
3. **Add remaining LEDs and button** to BB1
4. **Upload Python code** for LED cycling

Your power foundation is rock solid - time to build the full project on this single breadboard! 🔴🟢🔵

---

**Pro Tip**: This single-breadboard approach is actually more beginner-friendly and uses way fewer wires. You can always expand to multiple boards later if you want!
