class Counter:
    """Counter
    count UP when rise front on UP input
    count DOWN when rise front on DOWN input"""

    def __init__(self, accum=0):
        self._up = False
        self._down = False
        self._acc = accum

    @property
    def UP(self):
        return self._up

    @UP.setter
    def UP(self, bit):
        if bit == self._up:  # NO changes. nothing to do
            return
        if bit:  # rising up. count it
            self._acc += 1
            #print(self._acc)
        self._up = bit

    @property
    def DOWN(self):
        return self._down

    @DOWN.setter
    def DOWN(self, bit):
        if bit == self._down:  # NO changes. nothing to do
            return
        if bit:  # rising up. count it
            self._acc -= 1
        self._down = bit

    @property
    def ACC(self):
        return self._acc

    @ACC.setter
    def ACC(self, value):
        # assert type(value)  == type(1)
        self._acc = int(value)

    @property
    def ZERO(self):
        return self._acc == 0
