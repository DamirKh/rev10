import uasyncio as asyncio


async def test_coro(pause = 300):
    while True:
        await asyncio.sleep_ms(pause)
        # print('.')
