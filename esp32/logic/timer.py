from time import ticks_ms, ticks_diff, ticks_add


class Timer:
    def __init__(self, preset: int = 0):
        self.preset = preset
        self._enabled = False
        self._start = None
        self._done = False
        self._last_tick = None

    def _tick(self):
        if self._done or not self._enabled:
            return
        else:
            self._done = self.ACC > self.preset
            self._last_tick = ticks_ms()

    @property
    def EN(self):
        """Does timer counting?"""
        return self._enabled

    @EN.setter
    def EN(self, bit: bool):
        """Enable counting if TRUE
        If FALSE - stop counter, reset ACC, reset DN"""
        if not bit:
            self._enabled = False
            self._done = False
        elif bit and self._enabled:
            self._tick()
        elif bit and not self._enabled:
            # start timer. Rising front of EN
            self._start = ticks_ms()
            self._enabled = True
            self._tick()

    @property
    def TT(self):
        """TRUE while timer counting:
        EN but not DN"""
        return self._enabled and not self._done

    @property
    def DN(self):
        """Done counting bit
        TRUE if the timer has reached the preset """
        self._tick()
        return self._enabled and self._done

    @property
    def ACC(self):
        """Accumulator
        Time in milliseconds since the timer was enabled, e.g. EN=TRUE"""
        if not self._enabled:
            return 0
        else:
            return ticks_diff(self._last_tick, self._start)

    def __str__(self):
        s = """
    |   EN = {}
    |   DN = {}
    |   Preset = {}
    |   ACC = {}
    |   Start = {}  Tick = {}
    *   ACC type = {}
""".format(self.EN,
           self.DN,
           self.preset,
           self.ACC,
           self._start, self._last_tick,
           type(ticks_ms()))
        return s
