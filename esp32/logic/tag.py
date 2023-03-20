import G


class BaseInputTag:
    """This tag will be updated by HMI"""

    def __init__(self, name: str):
        self._name = name
        self._value = None
        G.INPUT_TAG[name] = self

    def trigger(self, val: str):
        """Override me"""
        raise NotImplementedError

    @property
    def VALUE(self):
        return self._value


class DiscreteInputTag(BaseInputTag):
    def trigger(self, val):
        if val.upper() in ('ON', 'TRUE', '1'):
            self._value = True
        else:
            self._value = False


class BaseOutputTag:
    """This tag updated by ESP32 and will send to HMI"""

    def __init__(self, name: str):
        self._name = name
        self._value = None
        G.OUTPUT_TAG[name] = self

    def trigger(self):
        """Override me"""
        raise NotImplementedError


class DiscreteOutputTag(BaseOutputTag):

    def trigger(self):
        G.OUT_QUEUE.put_nowait(self._name + ' ' + ('ON' if self._value else 'OFF'))

    @property
    def VALUE(self):
        return self._value

    @VALUE.setter
    def VALUE(self, val: bool):
        if not val == self._value:
            self._value = True if val else False
            self.trigger()


class RealOutputTag(BaseOutputTag):
    def __init__(self, name: str, fmt: str = ' {:-.3f}'):
        BaseOutputTag.__init__(self, name)
        self._fmt = fmt

    def trigger(self):
        G.OUT_QUEUE.put_nowait(self._name + self._fmt.format(self._value))

    @property
    def VALUE(self):
        return self._value

    @VALUE.setter
    def VALUE(self, val: float):
        self._value = float(val)
        self.trigger()


class RealInputTag(BaseInputTag):
    def __init__(self, name: str, low: float = -float('inf'), high: float = float('inf')):
        self._low = low
        self._high = high
        BaseInputTag.__init__(self, name)

    def trigger(self, val: str):
        try:
            v = float(val)
        except ValueError:
            # here should be an error message to hmi
            return
        v = max(self._low, v)
        v = min(self._high, v)
        self._value = v

        self._value = float(val)


class IntOutputTag(BaseOutputTag):
    def __init__(self, name: str, fmt: str = ' {:-d}'):
        BaseOutputTag.__init__(self, name)
        self._fmt = fmt

    def trigger(self):
        G.OUT_QUEUE.put_nowait(self._name + self._fmt.format(self._value))

    @property
    def VALUE(self):
        return self._value

    @VALUE.setter
    def VALUE(self, val: int):
        val_int = int(val)
        if val_int == self._value:  # nothing to do. Not even trigger
            return
        self._value = val_int
        self.trigger()


class IntInputTag(BaseInputTag):
    def __init__(self, name: str):
        BaseInputTag.__init__(self, name)

    def trigger(self, val: str):
        try:
            v = int(val)
        except ValueError:
            # here should be an error message to hmi
            return
        self._value = v
