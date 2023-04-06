## Timer

Объект используется там где нужно отмерять временные отрезки: задержку включения/выключения и т.д.
По составу доступных свойств и методов напоминает инструкцию TON, используемую в LadderLogic.

###  Инициализация
Инициализацию таймера (с точки зрения Python это создание объекта класса Timer) лучше производить до выполнения основного скана программы и до функции `onstart`.

    # ##############################  timers, counters, sparks
    T_Light = Timer(preset=5_000)

`T_Light` - имя объекта, по котору в дальнейшем обращаться к нему.
`preset=5_000` - "уставка" таймера в миллисекундах.

### Управление
Изменить уставку таймера можно следующим способом:

    T_Light.PRE = 10_000

Таймер запускается при подаче на EN значения True. (В проекте также доступны константы ON и OFF)

    T_Light.EN = ON
