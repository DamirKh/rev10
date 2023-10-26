from machine import Pin
from forcer.forced import ForcedCommon

class DOut(ForcedCommon):
    """Discrete Output"""

    def __init__(self, pin_number, invert=False, name=None):
        """:param pin_number number of Pin
        :param invert if True pin initiated HIGH"""
        assert type(invert) is type(True), 'What?!'
        self._invert = invert
        self._value = False
        self._pin = Pin(pin_number, Pin.OUT, value=1 if invert else 0, drive=Pin.DRIVE_3)
        if name is None:
            self.name = 'DO.{}'.format(pin_number)
        elif ' ' in name:
            raise "Incorrect Name. Should no whitespaces in name"
        else:
            self.name = name
        print('Discrete Output [{}] on pin {} initialized. Inverted={}'.format(self.name, pin_number, self._invert))
        super().__init__()

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
        if self.force_enabled:
            return
        if self._value:
            self._on()
        else:
            self._off()

    def force_value(self, value: bool):
        self._force_value = value
        if self.force_enabled:
            if value: self._on()
            else: self._off()

    def enable_force(self):
        self._force_enabled = True
        self.force_value(self._force_value)

    def disable_force(self):
        self._force_enabled = False
        self.STATE = self.STATE
