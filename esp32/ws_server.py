import G
G.last_client = 0


async def add_client(ws, path):
    print("Connection on {}".format(path))
    print(path)
    client_No = G.last_client
    G.last_client +=1
    G.CLIENTS[client_No] = ws
    print("Client {} connected".format(client_No))

    try:
        async for in_msg in ws:
            print(in_msg)
            #print(in_msg.decode("UTF8"))
            await G.IN_QUEUE.put(in_msg)
            #G.OUT_QUEUE.put_nowait(str(G.IN_QUEUE.qsize()))  # TODO COMMENT ME
            # await ws.send(str(G.IN_QUEUE.qsize()))
    except:
        print("Something wrong")
    finally:
        del(G.CLIENTS[client_No])  # ERROR
        print("Disconnected {}".format(client_No))


async def dispatcherUP():
    print("UPSTREAM Dispatcher started")
    while True:
        out_msg = await G.OUT_QUEUE.get()
        for ws in G.CLIENTS.values():
            print("sending <{}> --> {}".format(out_msg, ws))
            try:
                await ws.send(out_msg)
            except Exception as e:
                print("trouble sending message to client")
                print(e)
                pass


async def dispatcherDOWN():
    print("DOWNSTREAM Dispatcher started")
    while True:
        print("dispatherDOWN waiting for message...")
        in_msg = await G.IN_QUEUE.get()
        print("** DOWN message <{}>".format(in_msg))
        args = in_msg.split(" ", 1)
        device_name = args[0]
        try:
            if len(args) == 1:
                print("** Trigger tag {} with no args".format(device_name))
                G.INPUT_TAG[device_name].trigger()
            else:
                print("** Trigger tag {} with arg <{}>".format(device_name, args[1]))
                G.INPUT_TAG[device_name].trigger(args[1])
        except KeyError:
            print("!! Tag <{}> not registered".format(device_name))
