import G

class ForcedCommon():
    def __init__(self):
        self.__force_value = None
        print('Forced object initialised {}'.format(self.name))
        G.FORCER.register(forced_obj=self)
        pass

    @property
    def forced(self):
        if self.__force_value is None:
            return False
        return True

    @forced.setter
    def forced(self, enable=False):
        self.__force_value = None if not enable else