PERIOD = 20  # ms

import G
from logic import Timer
from logic import Counter
from logic import Seq
from logic import Spark
from logic import Revert
from logic import OneShoot
from logic import tag
from logic import  PID
from uasyncio import sleep_ms as PAUSE

# ############################# always accessible devices


# ############################## PIDs
pid_t = PID('pid_t')
pid_t.save_config()

# ##############################  timers, counters, sparks

T1 = Timer(8_000)
WorkingTimeCounter = Counter()
OneSecondSpark = Spark(1000)
ONS = OneShoot()

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
WORK_CNT = tag.IntOutputTag('WORK_CNT')


def onstart():
    print('Start application')
    # Start code below
    OneSecondSpark.EN = True
    await PAUSE(500)


def normal():
    OneSecondSpark.EN = True
    # application normal execution code below
    T1.EN = (SW_ON.ON or T1.TT) and not SW_OFF.ON
    ONS.EN = on_command.VALUE
    if ONS:
        print('1')

    WorkingTimeCounter.UP = OneSecondSpark.SPARK and LED1.value()
    #print(WorkingTimeCounter.ACC)
    if WorkingTimeCounter.UP:
        WORK_CNT.VALUE = WorkingTimeCounter.ACC
        TEMPERATURE.VALUE = DALLAS.VALUE

    LED1(T1.TT or on_command.VALUE)
    led_on.VALUE = LED1()


def onstop():
    print("Stop application")
