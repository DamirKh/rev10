from machine import Pin
from forcer.forced import ForcedCommon

class DOut(ForcedCommon):
    """Discrete Output"""

    def __init__(self, pin_number, invert=False, name=None):
        """
        :param pin_number number of Pin
        :param invert if True pin initiated HIGH
        Forces are only affected to hardware output, not current value!"""
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
        ForcedCommon.__init__(self)

    def _on(self):
        self._pin.value(not self._invert)
        # print("Pin [{}] = {}".format(self._pin, self._pin.value()))

    def _off(self):
        self._pin.value(self._invert)
        # print("Pin [{}] = {}".format(self._pin, self._pin.value()))


    @property
    def STATE(self):
        """Get current output value
        Forces are not affected to current value
        """
        return self._value

    @STATE.setter
    def STATE(self, v):
        self._value = True if v else False      # set internal current value
        if self._force_value is not None and self.force_enabled:
            return # Discrete Out forced! No real change needed.
        if self._value:                     # real hardware output
            self._on()
        else:
            self._off()


    def force_value(self, value: bool):
        self._force_value = value
        if value is None:   # means drop forcing
            self.STATE = self.STATE  # restore programming state
        elif self.force_enabled:
            if value: self._on()
            else: self._off()

    def enable_force(self):
        self._force_enabled_internal = True
        self.force_value(self._force_value)

    def disable_force(self):
        self._force_enabled_internal = False
        self.STATE = self.STATE     # restore programming state

    def get_real(self):
        return self._pin.value()

    def get_logic_value(self):
        return self.STATE

    def validate_force_value(self, value):
        if value == True or value==False or value is None:
            return True
        return False