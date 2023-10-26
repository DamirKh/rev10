import uasyncio as asyncio
from primitives.delay_ms import Delay_ms
import sys
from .forced import ForcedCommon


class Forcer:
    def __init__(self, control_line = None, report_line = None, enable:bool = False):
        self._control = sys.stdin if control_line is None else control_line
        self._report = sys.stdout if report_line is None else report_line
        self._enable = enable
        self.swriter = asyncio.StreamWriter(self._report, {})
        self.sreader = asyncio.StreamReader(self._control)
        self._run = asyncio.create_task(self._run())

        self.objects = {}

        print('Forcer object ready. Forces enabled = {}'.format(self._enable))
        print (self.sreader)
        print(self.swriter)


    async def _run(self):
        print('Forcer object waiting for command...')
        while True:
            res = await self.sreader.readline()
            res = res.decode().strip()
            if len(res) == 0:  # empty line after each command
                continue
            if res.upper()=='?':
                await self.swriter.awrite("#{}:\r\n".format(res))
                for name, obj in self.objects.items():
                    await self.swriter.awrite("- {} forced={}\r\n".format(name, obj.forced))
                await self.swriter.awrite("#Done.\r\n".format(res))
            else:
                await self.swriter.awrite("# Ignore unknown command [{}]\r\n".format(res))


    def register(self, forced_obj):
        assert isinstance(forced_obj, ForcedCommon)
        print('Forcer register object [{}]'.format(forced_obj.name))
        self.objects[forced_obj.name] = forced_obj