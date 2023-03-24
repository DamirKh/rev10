#
print("Main starting")

import uasyncio as asyncio
from ws_server import add_client, dispatcherDOWN, dispatcherUP
from websockets import server
import G
from logic import test
import io
import app

app.onstart()

test_task = asyncio.create_task(test.test_coro())
DispUP_task = asyncio.create_task(dispatcherUP())
DispDown_task = asyncio.create_task(dispatcherDOWN())
ws_server_task = server.serve(add_client, G.MAIN_IF, 7777)

loop = asyncio.get_event_loop()
loop.run_until_complete(ws_server_task)


async def main():
    await asyncio.sleep(0)
    try:
        while True:
            app.normal()  # periodically executed application code
            await asyncio.sleep_ms(app.PERIOD)
    except Exception as e:  # this will not work as expected.
        app.onstop()
        raise e


asyncio.run(main())
