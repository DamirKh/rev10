"""
this file defines the hardware features of the project. Relays, buttons, LEDs, ADC connected to ESP32
"""
import G
from machine import Pin
from logic import switch_ladder, dallas
#from neopixel import NeoPixel

# Switches
G.DEVICES['SW_ON'] = switch_ladder.Switch_ladder(Pin(22, Pin.IN), inverted=True)
G.DEVICES['SW_OFF'] = switch_ladder.Switch_ladder(Pin(19, Pin.IN), inverted=True)

# LEDS/RELAYS
G.DEVICES['LED1'] = Pin(23, Pin.OUT)

# Onboard NeoPixel LED


# Dallas 18B20 temperature sensor
G.DEVICES['DALLAS'] = dallas.Dallas(4, poll_period=10_000)


print(G.DEVICES)
print(' IO configuration loaded')
