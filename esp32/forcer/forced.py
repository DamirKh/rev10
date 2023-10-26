import G

class ForcedCommon():
    def __init__(self):
        self._force_value = None
        self._force_enabled = False
        print('Forced object initialised {}'.format(self.name))
        G.FORCER.register(forced_obj=self)
        pass

    @property
    def forced(self):
        return self._force_enabled and self._force_value is not None

    @property
    def force_enabled(self):
        return self._force_enabled

    def enable_force(self):
        raise NotImplemented

    def disable_force(self):
        raise NotImplemented

    def force_value(self, value):
        """Override me"""
        raise NotImplemented
