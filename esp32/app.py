PERIOD = 10  # ms

import G
from logic import Timer
from logic import Counter
from logic import Seq
from logic import Spark
from logic import Revert
from logic import OneShoot
from logic import tag
from logic import PID
from uasyncio import sleep_ms as PAUSE

# ############################# always accessible devices


# ############################## PIDs
pid_t = PID('pid_t', Kp=1.0, Ki=0.0, Kd=0.0, output_limits=(0, 100), proportional_on_measurement=False, differetial_on_measurement=False)
pid_t.save_config()

# ##############################  timers, counters, sparks

T1 = Timer(8_000)
WorkingTimeCounter = Counter()
OneSecondSpark = Spark(1000)
Q_SPARK = Spark(4000)
ONS = OneShoot()

# ############################# reversibles
R0 = Revert(False)

# ##############################  hardware specific
SW_ON = G.DEVICES['SW_ON']
SW_OFF = G.DEVICES['SW_OFF']
#LED1 = G.DEVICES['LED1']
DALLAS = G.DEVICES['DALLAS']
HEATER = G.DEVICES['HEATER']

# ############################## TAGS
on_command = tag.DiscreteInputTag('SW1')
#led_on = tag.DiscreteOutputTag('LED')
TEMPERATURE = tag.RealOutputTag("TEMPERATURE")
WORK_CNT = tag.IntOutputTag('WORK_CNT')
auto = tag.DiscreteInputTag('AUTO')
auto_up = tag.DiscreteOutputTag('AUTO')
temp_sp = tag.RealInputTag('TEMP_SP')
power = tag.RealOutputTag('POWER')
power_manual = tag.RealInputTag('POWER_MANUAL')
PID_c = tag.RealOutputTag('P'), tag.RealOutputTag('I'), tag.RealOutputTag('D')


def onstart():
    print('Start application')
    # Start code below
    Q_SPARK.EN = OneSecondSpark.EN = True
    TEMPERATURE.VALUE = DALLAS.VALUE
    power_manual.trigger(0.0)
    pid_t.SP = 33.0


def normal():
    OneSecondSpark.EN = True
    s1000 = OneSecondSpark.SPARK
    # application normal execution code below
    T1.EN = (SW_ON.ON or T1.TT) and not SW_OFF.ON
    ONS.EN = on_command.VALUE
    if ONS:
        print('1')

    WorkingTimeCounter.UP = s1000 and pid_t.AUTO
    #print(WorkingTimeCounter.ACC)
    if WorkingTimeCounter.UP:
        WORK_CNT.VALUE = WorkingTimeCounter.ACC

    #LED1(T1.TT or on_command.VALUE)
    #led_on.VALUE = LED1()

    HEATER.EN = auto_up.VALUE = pid_t.AUTO = auto.VALUE

    if Q_SPARK.SPARK:
        TEMPERATURE.VALUE = DALLAS.VALUE
        pid_t.PV = DALLAS.VALUE
        HEATER.VALUE = power.VALUE = pid_t.CV
        # HEATER.duty (int(power.VALUE))
        PID_c[0].VALUE, PID_c[1].VALUE, PID_c[2].VALUE = pid_t.simple_pid.components
    pid_t.CV = power_manual.VALUE


def onstop():
    print("Stop application")
