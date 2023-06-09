# Первый шаг

## Получение исходного кода проекта.
### Вариант 1.
Используй git

    $ git clone https://github.com/DamirKh/rev10.git
    Cloning into 'rev10'...
    remote: Enumerating objects: 659, done.
    remote: Counting objects: 100% (4/4), done.
    remote: Compressing objects: 100% (4/4), done.
    remote: Total 659 (delta 0), reused 1 (delta 0), pack-reused 655
    Receiving objects: 100% (659/659), 91.01 MiB | 2.24 MiB/s, done.
    Resolving deltas: 100% (324/324), done.
    $ cd rev10
    $ git status
    On branch master
    Your branch is up to date with 'origin/master'.
    
    nothing to commit, working tree clean
    $ git checkout zero
    Branch 'zero' set up to track remote branch 'zero' from 'origin'.
    Switched to a new branch 'zero'
    $ git status
    On branch zero
    Your branch is up to date with 'origin/zero'.
    
    nothing to commit, working tree clean
    

### Вариант 2.
Скачай исходный код по следующей ссылке [https://github.com/DamirKh/rev10/archive/refs/heads/zero.zip](URL)
Распакуй, перейди в распакованный каталог.

## Что внутри?

    $ tree -L 1
    .
    ├── doc
    ├── esp32
    ├── exp
    └── mI
    
    4 directories, 0 files
    
Каталог **doc** - внутри располагается документация, которой всегда мало.

Каталог **esp32** - внутри расположен код, который нужно прошивать в ESP32. Он будет исполняться MicroPython-ом.

Каталог **mI** - в этом каталоге проект GODOT, из которого генерируется приложение для управления Твоим устройством.

Каталог **exp** - внутри всякие экспериментальные вещи, забытые автором.

## Подготовка ESP32
### Прошить MicroPython

Проект MicroPython живет [https://micropython.org/](https://micropython.org/).
Выбрать подходящую для Твоего контроллера версию [здесь](https://micropython.org/download/?port=esp32).
Описание процесса прошивки [здесь](https://docs.micropython.org/en/latest/esp32/quickref.html).

После того как получен доступ к REPL, установку MicroPythona-а можно считать завершенной. Установку WebREPL автор не рекомендует.

### Инструмент для работы с Твоим кодом

В качестве первого инструмента можно выбрать [Thonny Python IDE for beginners](https://thonny.org/).

В панели файлов перейди в каталог `esp32`, выбери **все** файлы и **каталоги**, правой кнопкой мыши --> `Upload to /`.
Не забывай загружать измененные файлы в esp32. Лучше всегда держать файлы в каталоге разработке и на устройстве синхронизированными.

### Настройка WiFi подключения
В первую очередь настрой подключение твоего модуля esp32 к своей точке доступа, которая будет использоваться в процессе разработки. (Это нужно чтобы сохранить подключение компьютера, на котором производится разработка, к Интернету). Сделай это в каталоге разработки, затем загрузи изменения в esp32.

Открой файл wificfg.py, внеси необходимые изменения:

    modeAP = True  # set to True for making self access point
    
    AP_Settings = {
        'essid': 'ESP32-AP',
        'max_clients': 4,
        'password': '12344321'
    }
    
    
    modeSTA = True  # set tot True to connect to existing access point
    STA_Settings = {
        'ssid': 'YourAcceessPointName',
        'key': 'StrongPassword'
    }
    

В зависимости от конкретной модели esp32 может быть возможным одновременное подключение к Твоей точке доступа и создание  собственной. Сверяйся с документацией на свой модуль.

После того как конфигурация записана в esp32 нажми CTRL+D, чтобы убедиться что esp32 подключается к нужной точке доступа.

    MPY: soft reboot
    ********************
           REV 10       
    ********************
    Globals loading...
    Connected to access point gft
    Main interface IP address = 192.168.43.144
    Main starting

В зависимости от Твоей точки доступа esp32 может быть доступен по имени (обычно [espressif.local](URL)), но вообще - это отдельная тема для обсуждения.

### Конфигурация перифирии

Модуль esp32 без подключенных перифирийных устройств может, разве что поморгать светодиодом. Это, безусловно, интересно, но быстро надоедает. Чтобы разработать устройство, которое будет выполнять полезные функции к модулю esp32 нужно подключить перифирию для связи с внешним миром. Конфигурация перифирийных устройств хранится в файле **hw.py**. (Сокращение от HardWare, т.е. то, что выполнено жестко, проводами). В Твоем случае он выглядит примерно так:

    """
    this file defines the hardware features of the project. Relays, buttons, LEDs, ADC connected to ESP32
    """
    from machine import Pin, PWM
    from logic import switch_ladder, dallas, HeavyDutyPWM
    #from neopixel import NeoPixel
    
    # Switches
    SW_ON = switch_ladder.Switch_ladder(Pin(5, Pin.IN), inverted=True)
    SW_OFF = switch_ladder.Switch_ladder(Pin(6, Pin.IN), inverted=True)
    
    # LEDS/RELAYS
    LED1 = Pin(17, Pin.OUT)
    
    #PWM output
    # pwm0 = PWM(Pin(23), freq=10, duty=0)         # create PWM object from a pin
    #HEATER = HeavyDutyPWM(7, period=1)
    
    # Onboard NeoPixel LED
    
    # Dallas 18B20 temperature sensor
    #DALLAS = dallas.Dallas(4, poll_period=1_000)
    
    print(' IO configuration loaded')

Верхние 10 строк содержат описание назначения этого файла и необходимые для работы модули. Комментировать неиспользуемые модули нет необходимости (пока в Твоем устройстве достаточно памяти), а добавлять используемые - обязательно. В данном файле ниже комментария `# Switches` описаны две кнопки, подключенные к входам модуля esp32. Одна, как несложно догадаться, является кнопкой ВКЛ, другая - ВЫКЛ.
Далее, ниже комментария `# LEDS/RELAYS` описано куда подключен дискретный выход, который может управлять, например реле, светодиодом, или и тем и другим. При описании своей перифирии давай объектам названия, из которых будет ясно их назначение. (Автор так делает не всегда - можешь переименовать LED1 во что-нибудь по своему вкусу.)
После того, как опишешь перифирию, запиши изменения в модуль esp32 и нажми CTRL+D. 

        MPY: soft reboot
    ********************
           REV 10       
    ********************
    Globals loading...
    Connected to access point gft
    Main interface IP address = 192.168.43.144
    Main starting
     IO configuration loaded
    Start application
    UPSTREAM Dispatcher started
    DOWNSTREAM Dispatcher started
    dispatherDOWN waiting for message...
    

Строка `IO configuration loaded` говорит о том, что файл **hw.py**, по крайней мере - загружен.

### Логика приложения
Настало время описать логику работы устройства и заставить его выполнять задуманную, полезную для Тебя работу. Эта логика описывается в файле `app.py`.  Открой файл и обрати внимание на первые строки:
    
    PERIOD = 10  # ms  # это период с которым основная программа будет "сканироваться", т.е. выполняться
    
    import hw  #здесь импортируются описания перифирии которые Ты выполнил на предыдущем шаге
    from logic import Timer  # это кирпичики из которых будет построена Твоя программа
    from logic import Counter
    from logic import Seq
    from logic import Spark
    from logic import Revert
    from logic import OneShoot
    from logic import tag
    from logic import PID
    
Ниже расположены строки с комментариями, где следует размещать конфигурацию тех самых "кирпичиков" приложений.
Все, что расположено от начала файла до функции старта `onstart` будет выполнено один раз при включении устройства.
Все "кирпичики" должны быть инициализированы до выполнения основного скана программы. (Основным сканом Я буду называть периодически вызываемое выполнении функции `normal`). С точки зрения языка программирования Python эти кирпичики являются объектами. Каждый объект занимает в памяти определенное место для хранения своего состояния. Поэтому объекты не должны создаваться при выполнении основного скана программы. Размер занятой памяти не должен значительно меняться - это является одним из условий стабильности выполнения основного скана, который может работать очень долгое время. Теоритически - вечно.

После того как программа в модуле загружена необходимо привести перифирию в исходное состояние. (Конечно, при разработке схемотехнической части устройства нужно позаботиться о том, чтобы перифирия стартовала в безопасном состоянии). После старта и выполнения всех инициализаций "кирпичиков" программа выполняет код описанный в функции `onstart()`

#### onstart
Во-первых, эта функция (с точки зрения Python - это функция) печатает в REPL `Start application`, чтобы во время отладки убедиться что программа стартовала. Во-вторых, в этой функции следует описать операции по приведению перифирии в исходное состояние и, возможно, ее проверки. На предыдущем шаге в файле hw Ты описал подключенный к модулю светодиод (или реле) и дал ему имя. Автор назвал его `LED1`. С точки зрения логики не имеет значения подключен к модулю светодиод или реле - и в том и в другом случае программа рассматривает его как `Discrete Output - DO`.
При старте программы светодиод должен быть погашен, реле отпущено.

    def onstart():
        print('Start application')
        # Start code below
        hw.LED1.STATE = OFF

Обрати внимание на отступы в начале строки - они важны в Python.

#### normal
Эта функция выполняется постоянно, пока включено устройство с паузой между сканами, указанной в первой строке
файла `app.py`. 

    def normal():
        # Normal executed code below
        if hw.SW_OFF.ON:
            hw.LED1.STATE = OFF
        else:
            hw.LED1.STATE = hw.LED1.STATE or hw.SW_ON.ON
        pass

Приведенная программ имеет две ветви: одна исполняется при нажатой кнопке SW_OFF,
другая - в ином случае. Т.е, по смыслу - при НЕ нажатой.
Если кнопка SW_OFF нажата - светодиод выключается.
Если кнопка SW_OFF НЕ нажата - светодиод сохраняет свое текущее состояние или включается, если кнопка SW_ON нажата. 
Если светодиод включен - его состояние не измениться, пока не будет нажата кнопка SW_OFF.

