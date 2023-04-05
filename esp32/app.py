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
T_5sec = Timer(preset=5_000)
Trigger = JK()
ONS = OneShoot()

# ############################# reversibles

# ############################## TAGS
COMMAND = tag.DiscreteInputTag('COMMAND')
REMOTE_CONTROL = tag.DiscreteOutputTag('REMOTE_CONTROL')
LAMP_STATE = tag.DiscreteOutputTag('LAMP')

def onstart():
    print('Start application')
    # Start code below
    T_5sec.EN = OFF
    hw.LED1.STATE = OFF
    REMOTE_CONTROL.VALUE=ON

def normal():
    # Normal executed code below
    ONS.EN = COMMAND.VALUE
    T_5sec.EN = T_5sec.TT or ONS.EN
    if T_5sec.DN:
        COMMAND.trigger('OFF')
    LAMP_STATE.VALUE = hw.LED1.STATE = T_5sec.TT
    pass

def onstop():
    print("Stop application")
    # Start code below