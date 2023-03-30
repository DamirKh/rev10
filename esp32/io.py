"""
this file defines the hardware features of the project. Relays, buttons, LEDs, ADC connected to ESP32
"""
import G
from machine import Pin, PWM
from logic import switch_ladder, dallas, HeavyDutyPWM
#from neopixel import NeoPixel

# Switches
G.DEVICES['SW_ON'] = switch_ladder.Switch_ladder(Pin(5, Pin.IN), inverted=True)
G.DEVICES['SW_OFF'] = switch_ladder.Switch_ladder(Pin(6, Pin.IN), inverted=True)

# LEDS/RELAYS
#G.DEVICES['LED1'] = Pin(23, Pin.OUT)

#PWM output
# pwm0 = PWM(Pin(23), freq=10, duty=0)         # create PWM object from a pin
# G.DEVICES['PWM0'] = pwm0

big_heater = HeavyDutyPWM(7, period=1)
G.DEVICES['HEATER'] = big_heater


# Onboard NeoPixel LED


# Dallas 18B20 temperature sensor
G.DEVICES['DALLAS'] = dallas.Dallas(4, poll_period=1_000)


print(G.DEVICES)
print(' IO configuration loaded')
