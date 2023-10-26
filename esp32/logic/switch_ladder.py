from primitives import Switch
from machine import Pin


class PinInversable():
    def __init__(self, pin, inverted=False):
        assert isinstance(pin, Pin), "pin should be an instance of machine.Pin"
        self._pin = pin
        self._inverted = inverted

    def value(self):
        return not self._pin.value() if self._inverted else self._pin.value()


class Switch_ladder(Switch):
    """
    Simple switch input device with debounce = 50ms
    and configurable input invertion
    """
    def __init__(self, pin, inverted=False):
        self._pin_inversable = PinInversable(pin, inverted)
        Switch.__init__(self, self._pin_inversable)

    @property
    def ON(self):
        return self()
