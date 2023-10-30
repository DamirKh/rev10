import G

class ForcedCommon:
    def __init__(self):
        self._force_value = None
        self._force_enabled_internal = False
        print('Forced object initialised {}'.format(self.name))
        G.FORCER.register(forced_obj=self)
        pass

    @property
    def forced(self):
        return self._force_enabled_internal and self._force_value is not None

    @property
    def force_enabled(self):
        return self._force_enabled_internal

    def enable_force(self):
        raise NotImplemented

    def disable_force(self):
        raise NotImplemented

    def force_value(self, value):
        """Override me"""
        raise NotImplemented

    def get_real(self):
        """Override me"""
        raise NotImplemented

    def get_force_value(self):
        return self._force_value

    def get_logic_value(self):
        """Override me"""
        raise NotImplemented

    def validate_force_value(self, value):
        """Override me"""
        return True