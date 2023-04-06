class OneShoot:
    def __init__(self):
        self._read = False
        self._val = False

    @property
    def EN(self):
        if self._read or not self._val:
            return False
        self._read = True
        return self._val

    @EN.setter
    def EN(self, bit):
        if bit and not self._val:  # rising front
            self._val = True
            self._read = False
        if not bit:
            self._val = False

    def __bool__(self):
        return self.EN


class JK:
    def __init__(self, state=False):
        self._state = state
        self._j = False
        self._k = False

    @property
    def STATE(self):
        return self._state

    @property
    def JUMP(self):
        return self._j

    @JUMP.setter
    def JUMP(self, bit):
        if self._j == bit:  # nothing to do
            return
        elif bit:  # rising front
            self._state = True
        self._j = bit

    @property
    def KILL(self):
        return self._k

    @KILL.setter
    def KILL(self, bit):
        if self._k == bit:  # nothing to do
            return
        elif bit:  # rising front
            self._state = False
        self._k = bit

