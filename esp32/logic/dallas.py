from machine import Pin
import ds18x20, onewire
import uasyncio as asyncio


class Dallas:

    def __init__(self, pin_number, poll_period=10_000, convert_time=800):
        self._poll_period = poll_period
        self._convert_time = convert_time
        self._ds = ds18x20.DS18X20(onewire.OneWire(Pin(pin_number)))
        self._chips = self._ds.scan()
        self._values = []
        print('DALLAS: Found {} chips on pin {}'.format(len(self._chips), pin_number))
        for i in range(len(self._chips)):
            self._values.append(float('inf'))
        # print(self._values)
        self._run = asyncio.create_task(self.measure())

    async def measure(self):
        while True:
            self._ds.convert_temp()
            # print('.')
            await asyncio.sleep_ms(self._convert_time)
            for c in range(len(self._chips)):
                self._values[c] = self._ds.read_temp(self._chips[c])
                # print(self._values)
                await asyncio.sleep(0)
            await asyncio.sleep_ms(self._poll_period - self._convert_time)

    def __len__(self):
        return len(self._values)

    def __getitem__(self, key):
        return self._values[key]

    @property
    def VALUE(self):
        s = sum(self._values)
        a = s / len(self._values)
        return a

    def deinit(self):
        self._run.cancel()
