class Seq():
    """Sequencer """
    def __init__(self, seq, ring=True):
        """
        Object return a member of sequence by internally incrementing index.
        :param seq: any sequence.
        :param ring: sequence will be rounded
        """
        self._seq = seq
        self._index = 0
        self._ring = ring
        self._step = False
        self._done = False

    @property
    def VALUE(self):
        return self._seq[self._index]

    @property
    def STEP(self):
        return self._step

    @STEP.setter
    def STEP(self, step):
        if not step:
            self._step = False
        else:
            if self._step:  # This is not rising front
                return
            else:           # Rising front
                self._step = True
                i = self._index + 1
                if i == len(self._seq):  # End of sequence
                    self._done = True
                    if self._ring:   # round robin
                        self._index = 0
                else:
                    if self._ring:  #
                        self._done = False
                    self._index = i

    @property
    def DN(self):
        return self._done

    @property
    def RESET(self):
        return self._done

    @RESET.setter
    def RESET(self, bit):
        if not bit:
            self._done = False
            self._index = 0
