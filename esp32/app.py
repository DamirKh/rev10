PERIOD = 10  # ms

import hw
from logic import ON, OFF
from logic import Timer
from logic import Counter
from logic import Seq
from logic import Spark
from logic import Revert
from logic import OneShoot, JK
from logic import tag
from logic import PID


# ############################# always accessible devices

# ############################## PIDs

# ##############################  timers, counters, sparks
T_Light = Timer(preset=5_000)
MyLAMP = JK()


# ############################# reversibles

# ############################## TAGS
BTN_ON = tag.DiscreteInputTag('BTN_ON')
BTN_OFF = tag.DiscreteInputTag('BTN_OFF')
LAMP_STATE = tag.DiscreteOutputTag('LAMP')
COUNTDOWN = tag.IntOutputTag('COUNTDOWN')
LIGHT_TIME = tag.IntInputTag('LIGHT_TIME')

def onstart():
    print('Start application')
    # Start code below
    T_Light.EN = OFF
    hw.LED1.STATE = OFF
    LIGHT_TIME.trigger(T_Light.PRE/1000)
    COUNTDOWN.VALUE = T_Light.PRE/1000

def normal():
    # Normal executed code below
    T_Light.PRE = LIGHT_TIME.VALUE * 1000
    MyLAMP.JUMP = BTN_ON.VALUE or hw.SW_ON.ON
    MyLAMP.KILL = BTN_OFF.VALUE or hw.SW_OFF.ON or T_Light.DN
    T_Light.EN = MyLAMP.STATE
    COUNTDOWN.VALUE = (T_Light.PRE - T_Light.ACC)/1000 + 1
    LAMP_STATE.VALUE = hw.LED1.STATE = T_Light.TT

    # Drop discrete input tags below
    BTN_ON.trigger('OFF')
    BTN_OFF.trigger('OFF')
    pass

def onstop():
    print("Stop application")
    # Stop code below