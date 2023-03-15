from time import ticks_ms, ticks_diff, ticks_add


class Spark:
    """Flash periodical"""

    def __init__(self, period: int):
        self.period = period
        self._enabled = False
        self._dn_time = ticks_add(ticks_ms(), self.period)

    def _update(self):
        self._dn_time=ticks_add(ticks_ms(), self.period)

    @property
    def SPARK(self):
        if not self._enabled:
            return False
        if ticks_diff(ticks_ms(), self._dn_time) > 0:
            self._dn_time = ticks_add(self._dn_time, self.period)
            return True
        else:
            return False

    @property
    def EN(self):
        return self._enabled

    @EN.setter
    def EN(self, bit):
        if bit and not self._enabled:  # rising front
              self._enabled = True
              self._dn_time = ticks_add(ticks_ms(), self.period)
        if not bit:
            self._enabled = False
