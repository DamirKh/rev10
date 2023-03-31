from machine import Pin
import uasyncio as asyncio
from helpers import clamp

class HeavyDutyPWM:
    """Software PWM"""

    def __init__(self, pin_number, period=10, invert=False, limits=(0, 100)):
        """:param period (seconds)
        :param invert if True pin initiated HIGH"""
        assert type(invert) is type(True), 'What?!'
        assert limits == (0, 100), 'Not implemented custom range!'
        self.limits = limits
        self._invert = invert
        self._period = period
        self._value = 0.
        self._enabled = False
        self._freq = 1.0 / float(period)
        self._pin = Pin(pin_number, Pin.OUT, value=1 if invert else 0, drive=Pin.DRIVE_3)
        print('Heavy Duty PWM on pin {} initialized. Period={}, Inverted={}'.format(pin_number, self._period,
                                                                                    self._invert))
        self._run = asyncio.create_task(self.flash())

    def on(self):
        self._pin.value(not self._invert)

    def off(self):
        self._pin.value(self._invert)

    async def flash(self):
        while True:
            if not self._enabled:
                self.off()
                await asyncio.sleep(self._period / 10.0)
            else:
                self.on()
                await asyncio.sleep(self._value * (self._period / 100))
                self.off()
                await asyncio.sleep((100 - self._value) * (self._period / 100))

    @property
    def VALUE(self):
        return self._value

    @VALUE.setter
    def VALUE(self, v):
        self._value = float(clamp(v, self.limits))

    @property
    def EN(self):
        return self._enabled

    @EN.setter
    def EN(self, bit):
        if not bit:
            self.off()
        self._enabled = bit

    def deinit(self):
        self.off()
        self._run.cancel()
