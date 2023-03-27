from .pid import PID as simple_pid
import time

SETTINGS_FILE_NAME = 'settings.ini'
from configparser.ConfigParser import ConfigParser


class PID:
    def __init__(
            self,
            pid_name,
            Kp=1.0,
            Ki=0.0,
            Kd=0.0,
            setpoint=0,
            # sample_time=None,
            output_limits=(0.0, 100.0),
            auto_mode=False,
            proportional_on_measurement=False,
            differetial_on_measurement=False,
    ):
        self._pid_name = pid_name
        self._set_point = setpoint
        self._pv = setpoint
        self._cv = 0.
        self._auto = auto_mode

        # ############################################################################  configuration loader
        if True:
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
            self.simple_pid = simple_pid(
                Kp=_Kp, Ki=_Ki, Kd=_Kd,
                sample_time=None,
                output_limits=output_limits,
                auto_mode=auto_mode,
                proportional_on_measurement=proportional_on_measurement,
                differetial_on_measurement=differetial_on_measurement,
            )
            # self.simple_pid.time_fn = time.ticks_us

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

    @property
    def SP(self):
        """SetPoint of PID-controller"""
        return self.simple_pid.setpoint

    @SP.setter
    def SP(self, value):
        """Set new value to SetPoint"""
        self.simple_pid.setpoint = float(value) if value is not None else 0.0

    @property
    def PV(self):
        """ProcessVariable"""
        return self._pv

    @PV.setter
    def PV(self, value):
        """ Set current value for ProcessVariable """
        self._pv = float(value)

    @property
    def CV(self):
        """Control Variable"""
        if self._auto:
            self._cv = self.simple_pid(self._pv)
            #print('Mode AUTO. CV = {}'.format(self._cv))
            return self._cv
        else:
            #print('Mode MANUAL. CV = {}'.format(self._cv))
            return self._cv


    @CV.setter
    def CV(self, value):
        if self._auto:
            return
        else:
            self._cv = value
            #print('!! mode MANUAL  set CV={}'.format(self._cv))


    @property
    def AUTO(self):
        return self._auto

    @AUTO.setter
    def AUTO(self, a):
        if a and self._auto:  # no change
            return
        if a and not self._auto:  # switch to auto mode
            self._auto = True
            self.simple_pid.set_auto_mode(True, last_output=self._cv)
        if not a and not self._auto:  # no change
            return
        if not a and self._auto: # switch to manual mode
            self._auto = False
            self.simple_pid.auto_mode = False

