"""
this file defines the hardware features of the project. Relays, buttons, LEDs, ADC connected to ESP32
"""
from machine import Pin
from machine import PWM
from logic import switch_ladder
from logic import DOut
from logic import dallas
from logic import HeavyDutyPWM
from neopixel import NeoPixel
from machine import TouchPad

# Switches
SW_ON = switch_ladder.Switch_ladder(Pin(5, Pin.IN), inverted=True)
SW_OFF = switch_ladder.Switch_ladder(Pin(6, Pin.IN), inverted=True)

# Touches
#T_BLACK = TouchPad(Pin(12))

# LEDS/RELAYS
LED1 = DOut(pin_number=42)
LED2 = DOut(pin_number=41)

#PWM output
# pwm0 = PWM(Pin(23), freq=10, duty=0)         # create PWM object from a pin
#HEATER = HeavyDutyPWM(7, period=1)

# Dallas 18B20 temperature sensor
#DALLAS = dallas.Dallas(4, poll_period=1_000)

print(' IO configuration loaded')
