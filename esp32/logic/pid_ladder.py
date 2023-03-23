from .pid import PID as simple_pid

SETTINGS_FILE_NAME = 'settings.ini'
from configparser.ConfigParser import ConfigParser


class PID:
    def __init__(self, pid_name, Kp=1.0, Ki=0.0, Kd=0.0):
        self._pid_name = pid_name
        config = ConfigParser()
        config.read(SETTINGS_FILE_NAME)
        if config.has_section(pid_name):
            _Kp: float = float(config.get(pid_name, 'Kp')) if config.has_option(pid_name, 'Kp') else Kp
            _Ki: float = float(config.get(pid_name, 'Ki')) if config.has_option(pid_name, 'Ki') else Ki
            _Kd: float = float(config.get(pid_name, 'Kd')) if config.has_option(pid_name, 'Kd') else Kd
        else:
            _Kp, _Ki, _Kd = Kp, Ki, Kd
        print('PID controller <{}> initiated'.format(pid_name))
        print('Kp={}  Ki={}  Kd={}'.format(_Kp, _Ki, _Kd))
        self.simple_pid = simple_pid(Kp=_Kp, Ki=_Ki, Kd=_Kd)

    def save_config(self):
        config = ConfigParser()
        config.read(SETTINGS_FILE_NAME)
        if not config.has_section(self._pid_name):
            config.add_section(self._pid_name)

        if config.has_option(self._pid_name, 'Kp'):
            config.remove_option(self._pid_name, 'Kp')
        config.add_option(self._pid_name, 'Kp')
        config.config_dict[self._pid_name]['Kp'] = str(self.simple_pid.Kp)

        if config.has_option(self._pid_name, 'Ki'):
            config.remove_option(self._pid_name, 'Ki')
        config.add_option(self._pid_name, 'Ki')
        config.config_dict[self._pid_name]['Ki'] = str(self.simple_pid.Ki)

        if config.has_option(self._pid_name, 'Kd'):
            config.remove_option(self._pid_name, 'Kd')
        config.add_option(self._pid_name, 'Kd')
        config.config_dict[self._pid_name]['Kd'] = str(self.simple_pid.Kd)

        config.write(SETTINGS_FILE_NAME)
