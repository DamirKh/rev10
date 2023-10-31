from primitives import Switch
from machine import Pin
from forcer.forced import ForcedCommon


class PinInversable():
    def __init__(self, pin, inverted=False):
        assert isinstance(pin, Pin), "pin should be an instance of machine.Pin"
        self._pin = pin
        self._inverted = inverted

    def value(self):
        return not self._pin.value() if self._inverted else self._pin.value()


class Switch_ladder(Switch, ForcedCommon):
    """
    Simple switch input device with debounce = 50ms
    and configurable input invertion
    """
    def __init__(self, pin, inverted=False, name=None):
        if type(pin) is type(1):
            p = Pin(pin, Pin.IN)
        else:
            p = pin
        self._pin_inversable = PinInversable(p, inverted)
        Switch.__init__(self, self._pin_inversable)
        if name is None:
            self.name = 'DI.{}'.format(pin)
        elif ' ' in name:
            raise "Incorrect Name. Should no whitespaces in name"
        else:
            self.name = name
        print('Discrete Input [{}] on pin {} initialized. Inverted={}'.format(self.name, pin, inverted))
        ForcedCommon.__init__(self)

    @property
    def ON(self):
        if not self.force_enabled:
            return self()
        elif self._force_value is None:
            return self()
        else:
            return self._force_value


    def disable_force(self):
        self._force_enabled_internal = False

    def enable_force(self):
        self._force_enabled_internal = True
        self.force_value(self._force_value)

    def force_value(self, value: bool):
        self._force_value = value

    def get_real(self):
        return self()

    def get_logic_value(self):
        return self.ON

    def validate_force_value(self, value):
        if value == True or value==False or value is None:
            return True
        return False