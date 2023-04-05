### About the project
The proposed software package is designed to create small automation devices.

##### Main ideas:

1. using a separate device (for example, a telephone) as a human-machine interface
2. Ability to directly connect HMI - esp32 without external dependencies. (I don’t want to lose the opportunity to turn on the light somewhere due to a non-working mqtt broker)
3. Hardware - ESP32
4. The software part of the controller - a set of libraries and an engine in micropython
5. HMI software part - libraries and engine on GODOT.
It turned out pretty cool in my opinion. Thanks to GODOT, building interfaces is not complicated, visual. Deploy is simple on all kinds of platforms.


##### Remarks
1. An indirect connection between the HMI and the esp32 is possible, but is not the main interest of the author.
2. it is possible to combine several esp32 devices into a single network.


### О проекте
Предлагаемый программный комплект предназначен для создания небольших устройств автоматизации. 

##### Основные идеи:

1. использование отдельного устройства (например, телефона) в качестве человеко-машинного интерфеса
2. Возможность прямого соединения ЧМИ - esp32 без внешних зависимостей. (Не хочется потерять возможность включить где-либо свет из-за неработающего mqtt брокера)
3. Аппаратная часть -  ESP32
4. Программная часть контроллера - набор библиотек и движок на micropython
5. Программная часть ЧМИ - библиотеки и движок на GODOT.
На мой взгляд получилось прикольно. Благодаря GODOT построение интерфейсов не сложное, визуальное. Деплой простой на всевозможные платформы.


##### Ремарки
1. Непрямое соединение между ЧМИ и esp32 возможно, но не является основным интересом автора.
2. возможно объединение нескольких устройств esp32 в единую сеть.
