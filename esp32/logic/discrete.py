from machine import Pin

class DOut:
    """Discrete Output"""

    def __init__(self, pin_number, invert=False,):
        """:param pin_number number of Pin
        :param invert if True pin initiated HIGH"""
        assert type(invert) is type(True), 'What?!'
        self._invert = invert
        self._value = False
        self._pin = Pin(pin_number, Pin.OUT, value=1 if invert else 0, drive=Pin.DRIVE_3)
        print('Discrete Output on pin {} initialized. Inverted={}'.format(pin_number, self._invert))

    def _on(self):
        self._pin.value(not self._invert)

    def _off(self):
        self._pin.value(self._invert)

    @property
    def STATE(self):
        return self._value

    @STATE.setter
    def STATE(self, v):
        self._value = True if v else False
        if self._value:
            self._on()
        else:
            self._off()
