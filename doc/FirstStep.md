# Первый шаг

## Получение исходного кода проекта.
### Вариант 1.
Используй git

    damir@damir-VirtualBox:~/rollout$ git clone https://github.com/DamirKh/rev10.git
    Cloning into 'rev10'...
    remote: Enumerating objects: 659, done.
    remote: Counting objects: 100% (4/4), done.
    remote: Compressing objects: 100% (4/4), done.
    remote: Total 659 (delta 0), reused 1 (delta 0), pack-reused 655
    Receiving objects: 100% (659/659), 91.01 MiB | 2.24 MiB/s, done.
    Resolving deltas: 100% (324/324), done.
    damir@damir-VirtualBox:~/rollout$ cd rev10
    damir@damir-VirtualBox:~/rollout/rev10$ git status
    On branch master
    Your branch is up to date with 'origin/master'.
    
    nothing to commit, working tree clean
    damir@damir-VirtualBox:~/rollout/rev10$ git checkout zero
    Branch 'zero' set up to track remote branch 'zero' from 'origin'.
    Switched to a new branch 'zero'
    damir@damir-VirtualBox:~/rollout/rev10$ git status
    On branch zero
    Your branch is up to date with 'origin/zero'.
    
    nothing to commit, working tree clean
    

### Вариант 2.
Скачай исходный код по следующей ссылке [https://github.com/DamirKh/rev10/archive/refs/heads/zero.zip](URL)
Распакуй, перейди в распакованный каталог.

## Что внутри?

    damir@damir-VirtualBox:~/rollout/rev10$ tree -L 1
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

### Инструмент для работы с Вашим кодом.

В качестве первого инструмента можно выбрать [Thonny Python IDE for beginners](https://thonny.org/).

В панели файлов перейди в каталог `esp32`, выбери **все** файлы и **каталоги**, правой кнопкой мыши --> `Upload to /`
В первую очередь 