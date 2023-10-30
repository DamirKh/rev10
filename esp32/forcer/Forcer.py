import uasyncio as asyncio
from primitives.delay_ms import Delay_ms
import sys
from .forced import ForcedCommon

NO_SUCH_OBJECT_STR="# No such object! [{}]\r\n"
FORCE_VALUE_STR = "# Force value = [{}]\r\n"
FORCES_STR = "# Forces {}\r\n"
OBJECT_STR = "# Object [{}]:\r\n"
REAL_VALUE_STR = "# Real value = [{}]\r\n"
LOGIC_VALUE_STR = "# Logic value = [{}]\r\n"
INCORRECT_VALUE_STR = "# Incorrect value [{}]\r\n"

class Forcer:
    def __init__(self, control_line=None, report_line=None, enable: bool = False):
        self._control = sys.stdin if control_line is None else control_line
        self._report = sys.stdout if report_line is None else report_line
        self._enable = enable
        self.swriter = asyncio.StreamWriter(self._report, {})
        self.sreader = asyncio.StreamReader(self._control)
        self._run = asyncio.create_task(self._run())

        self.objects = {}

        print('Forcer object ready. Forces enabled = {}'.format(self._enable))
        print(self.sreader)
        print(self.swriter)

    async def _run(self):
        print('Forcer object waiting for command...')
        while True:
            await self.swriter.awrite(">")
            forcer_command = await self.sreader.readline()
            # assert type(forcer_command) is type('')
            forcer_command = forcer_command.decode().strip()
            if len(forcer_command) == 0:  # empty line after each command
                continue
            EnDis_str = 'Enabled' if self._enable else 'Disabled'
            if forcer_command.upper() == '!':                                              # List of all forced ojects #
                # await self.swriter.awrite("#{}:\r\n".format(forcer_command))
                await self.swriter.awrite("# Forces {}:\r\n".format(EnDis_str))
                counter = 0
                for name, obj in self.objects.items():
                    if obj.get_force_value() is not None:
                        await self.swriter.awrite("- [{}] force value={}\r\n".format(name, obj.get_force_value()))
                        counter+=1
                await self.swriter.awrite("# Done. {} forces total\r\n".format(counter))
                continue
            if forcer_command.upper() == '?':                                          # List of all registered ojects #
                # await self.swriter.awrite("#{}:\r\n".format(forcer_command))
                await self.swriter.awrite("# Forces {}:\r\n".format(EnDis_str))
                counter = 0
                for name, obj in self.objects.items():
                    await self.swriter.awrite("- [{}] force value={}\r\n".format(name, obj.get_force_value()))
                    counter+=1
                await self.swriter.awrite("# Done. {} objects registered\r\n".format(counter))
                continue
            if forcer_command.upper()[0] == '?':                                                         # object info #
                try:
                    obj_name = forcer_command.split()[1]
                except IndexError:
                    await self.swriter.awrite("# Incorrect command format [{}]\r\n".format(forcer_command))
                    continue
                obj = self.objects.get(obj_name)
                if obj is None:
                    await self.swriter.awrite("# No such object {}:\r\n".format(obj_name))
                    continue
                # await self.swriter.awrite("#{}:\r\n".format(forcer_command))
                await self.swriter.awrite(FORCES_STR.format(EnDis_str))
                await self.swriter.awrite(OBJECT_STR.format(obj_name))
                await self.swriter.awrite(FORCE_VALUE_STR.format(obj.get_force_value()))
                await self.swriter.awrite(REAL_VALUE_STR.format(obj.get_real()))
                await self.swriter.awrite(LOGIC_VALUE_STR.format(obj.get_logic_value()))
                continue
            if forcer_command.upper() == '!E':                                                         # enable forces #
                self._enable = True
                for name, obj in self.objects.items():
                    obj.enable_force()
                await self.swriter.awrite("# All Forces enabled.\r\n")
                continue
            if forcer_command.upper() == '!D':                                                        # disable forces #
                self._enable = False
                for name, obj in self.objects.items():
                    obj.disable_force()
                await self.swriter.awrite("# All Forces disabled.\r\n")
                continue
            if forcer_command.upper()[0] == '!':                                              # set/remove force value #
                try:
                    command, obj_name, value = forcer_command.split()
                except ValueError or IndexError:
                    await self.swriter.awrite("# Incorrect command format [{}]\r\n".format(forcer_command))
                    continue
                obj = self.objects.get(obj_name)
                if obj is None:
                    await self.swriter.awrite(NO_SUCH_OBJECT_STR.format(obj_name))
                    continue
                try:
                    valeval = eval(value)
                except:
                    await self.swriter.awrite(INCORRECT_VALUE_STR.format(value))
                    continue
                try:
                    assert obj.validate_force_value(valeval)
                except AssertionError:
                    await self.swriter.awrite(INCORRECT_VALUE_STR.format(valeval))
                    continue
                obj.force_value(valeval)
                await self.swriter.awrite(FORCES_STR.format(EnDis_str))
                await self.swriter.awrite(OBJECT_STR.format(obj_name))
                await self.swriter.awrite(FORCE_VALUE_STR.format(obj.get_force_value()))
                await self.swriter.awrite(REAL_VALUE_STR.format(obj.get_real()))
                continue

            else:
                await self.swriter.awrite("# Ignore unknown command [{}]\r\n".format(forcer_command))

    def register(self, forced_obj):
        assert isinstance(forced_obj, ForcedCommon)
        print('Forcer register object [{}]'.format(forced_obj.name))
        self.objects[forced_obj.name] = forced_obj
