class Revert:
    """
    An object inverts its STATE each time its STATE is accessed.
    The object STATE remains initial state (FALSE by default) while the RESET signal is active.
    The initial state can be set when the object is initialized. (Default is FALSE)
    """
    def __init__(self, condition: bool = False):
        """

        :param condition: initial state
        """
        self._condition = condition
        self._reset = False
        self._initial_state = condition

    @property
    def STATE(self):
        if self._reset:
            return self._initial_state
        else:
            w = self._condition
            self._condition = not self._condition
            return w

    @property
    def RESET(self):
        return self._reset

    @RESET.setter
    def RESET(self, bit: bool):
        self._reset = bit
        self._condition = self._initial_state
