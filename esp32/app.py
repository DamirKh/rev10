PERIOD = 10  # ms

import hw
from logic import ON, OFF
from logic import Timer
from logic import Counter
from logic import Seq
from logic import Spark
from logic import Revert
from logic import OneShoot
from logic import tag
from logic import PID


# ############################# always accessible devices


# ############################## PIDs

# ##############################  timers, counters, sparks

# ############################# reversibles

# ############################## TAGS

def onstart():
    print('Start application')
    # Start code below
    hw.LED1

def normal():
    # Normal executed code below
    pass

def onstop():
    print("Stop application")
    # Start code below