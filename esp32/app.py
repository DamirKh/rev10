PERIOD = 20  # ms

import G
from logic.timer import Timer
from logic.Seq import Seq
from logic.Spark import Spark
from logic.revert import Revert
from logic import tag
from uasyncio import sleep_ms as PAUSE

# ############################# always accessible devices


###############################  timers

T1 = Timer(8_000)
S3000 = Spark(3000)

# ############################# reversibles
R0 = Revert(False)

# ##############################  hardware specific
SW_ON = G.DEVICES['SW_ON']
SW_OFF = G.DEVICES['SW_OFF']
LED1 = G.DEVICES['LED1']
DALLAS = G.DEVICES['DALLAS']

# ############################## TAGS
on_command = tag.DiscreteInputTag('SW1')
led_on = tag.DiscreteOutputTag('LED')
TEMPERATURE = tag.RealOutputTag("TEMPERATURE")
TEMPERATURE.VALUE = DALLAS.VALUE


def onstart():
    print('Start application')
    S3000.EN = True
    # place start code here
    #
    #
    await PAUSE(1_000)


def normal():
    # print("application normal executed")
    # print("ON" if SW1() else "OFF")
    T1.EN = (SW_ON.ON or T1.TT) and not SW_OFF.ON

    if S3000.SPARK:
        TEMPERATURE.VALUE = DALLAS.VALUE
        TEMPERATURE.trigger()

    LED1(T1.TT or on_command.VALUE)
    led_on.VALUE = LED1()


def onstop():
    print("Stop application")
