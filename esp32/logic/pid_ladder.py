from .pid import PID as simple_pid
SETTINGS_FILE_NAME = 'settings.ini'
from configparser.ConfigParser import ConfigParser


class PID:
    def __init__(self, pid_name):
        try:
            config = ConfigParser(SETTINGS_FILE_NAME)
            config.read()
            Kp: float = config.getfloat(pid_name, 'Kp')
            print('Kp={}'.format(Kp))
        except:
            print('File not found: {}'.format(SETTINGS_FILE_NAME))
            print('Creating new one...')
            config = ConfigParser(SETTINGS_FILE_NAME)
            config.add_section(pid_name)
            config.set(pid_name, 'Kp', 1.0)
            with open(SETTINGS_FILE_NAME, 'w') as f:
                config.write(f)