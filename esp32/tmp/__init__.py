
def test_timer(preset=10_000):
    from time import sleep
    from logic.helpers import cls
    from logic.timer import Timer
    t=Timer(preset)
    cls()
    print(t)
    print("""
    Now starting timer...""")
    sleep(1)
    for x in range(30):
        cls()
        t.EN = 5 < x < 20
        print(t)
        sleep(1)
