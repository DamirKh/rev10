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
