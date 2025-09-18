🌟 Pattern: Breathing Effect
🔌 All LEDs turned off - GPIO cleaned up
Traceback (most recent call last):
  File "/home/jman/repos/rasberry_pi_projects/led_cycle.py", line 346, in <module>
    main()
  File "/home/jman/repos/rasberry_pi_projects/led_cycle.py", line 335, in main
    run_light_show()
  File "/home/jman/repos/rasberry_pi_projects/led_cycle.py", line 258, in run_light_show
    pattern()
  File "/home/jman/repos/rasberry_pi_projects/led_cycle.py", line 116, in pattern_breathing
    pwm_leds = [PWMLED(LED1_PIN), PWMLED(LED2_PIN), PWMLED(LED3_PIN)]
                ^^^^^^^^^^^^^^^^
  File "/usr/lib/python3/dist-packages/gpiozero/devices.py", line 108, in __call__
    self = super().__call__(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3/dist-packages/gpiozero/output_devices.py", line 392, in __init__
    super().__init__(pin, active_high=active_high, initial_value=None,
  File "/usr/lib/python3/dist-packages/gpiozero/output_devices.py", line 74, in __init__
    super().__init__(pin, pin_factory=pin_factory)
  File "/usr/lib/python3/dist-packages/gpiozero/mixins.py", line 75, in __init__
    super().__init__(*args, **kwargs)
  File "/usr/lib/python3/dist-packages/gpiozero/devices.py", line 552, in __init__
    self.pin_factory.reserve_pins(self, pin)
  File "/usr/lib/python3/dist-packages/gpiozero/pins/__init__.py", line 88, in reserve_pins
    raise GPIOPinInUse(
gpiozero.exc.GPIOPinInUse: pin GPIO4 is already in use by <gpiozero.LED object on pin GPIO4, active_high=True, is_active=False>
