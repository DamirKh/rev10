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

# Switches  # parallax PDB
SW_ON = switch_ladder.Switch_ladder(Pin(22, Pin.IN), inverted=True)
SW_OFF = switch_ladder.Switch_ladder(Pin(19, Pin.IN), inverted=True)

# LEDS/RELAYS
LED1 = DOut(pin_number=23)

#PWM output
# pwm0 = PWM(Pin(23), freq=10, duty=0)         # create PWM object from a pin
#HEATER = HeavyDutyPWM(7, period=1)

# Dallas 18B20 temperature sensor
#DALLAS = dallas.Dallas(4, poll_period=1_000)

print(' IO configuration loaded')
