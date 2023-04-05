# First step

## Get project source code.
### Option 1.
Use git

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
    

### Option 2.
Download the source code from the following link [https://github.com/DamirKh/rev10/archive/refs/heads/zero.zip](URL)
Unpack, go to the unpacked directory.

## What is inside?

     $tree -L 1
     .
     ├── document
     ├── esp32
     ├──exp
     └── mI
    
     4 directories, 0 files
    
Directory **doc** - documentation is located inside, which is always small.

Directory **esp32** - inside is the code that needs to be flashed into the ESP32. It will be executed by MicroPython.

Directory **mI** - in this directory is the GODOT project, from which the application for managing your device is generated.

Catalog **exp** - inside all sorts of experimental things forgotten by the author.

## Prepare ESP32
### Flash MicroPython

The MicroPython project lives on [https://micropython.org/](https://micropython.org/).
Select the appropriate version for your controller [here](https://micropython.org/download/?port=esp32).
Description of the flashing process [here] (https://docs.micropython.org/en/latest/esp32/quickref.html).

Once you have access to the REPL, the installation of MicroPythona is complete. The author does not recommend installing WebREPL.

### A tool to work with your code

You can choose [Thonny Python IDE for beginners](https://thonny.org/) as the first tool.

In the file pane, navigate to the `esp32` directory, select **all** files and **directories**, right click --> `Upload to /`.
Don't forget to upload modified files to esp32. It's best to always keep the files in the development directory and on the device in sync.

### WiFi connection setup
First of all, set up the connection of your esp32 module to your access point, which will be used in the development process. (This is necessary to keep the development computer connected to the Internet). Do this in the development directory, then upload the changes to esp32.

Open the wificfg.py file, make the necessary changes:

     modeAP = True # set to True for making self access point
    
     AP_Settings = {
         'essid': 'ESP32-AP',
         'max_clients': 4,
         'password': '12344321'
     }
    
    
     modeSTA = True # set to True to connect to existing access point
     STA_Settings = {
         'ssid': 'YourAcceessPointName',
         'key': 'StrongPassword'
     }
    

Depending on the specific esp32 model, it may be possible to connect to your hotspot and create your own at the same time. Check the documentation for your module.

Once the configuration is written to the esp32 press CTRL+D to make sure the esp32 connects to the correct access point.

     MPY: soft reboot
     ********************
            REV 10
     ********************
     Global loading...
     Connected to access point gft
     Main interface IP address = 192.168.43.144
     Main starting

Depending on your access point, esp32 may be available by name (usually [espressif.local](URL)), but this is a separate topic for discussion.

### Periphery configuration

The esp32 module without connected peripherals can only blink the LED. It's certainly interesting, but quickly boring. To develop a device that will perform useful functions, you need to connect peripherals to the esp32 module to communicate with the outside world. Peripheral device configuration is stored in the **hw.py** file. (Short for HardWare, that is, what is done hard, with wires). In your case it looks like this:

     """
     this file defines the hardware features of the project. Relays, buttons, LEDs, ADC connected to ESP32
     """
     from machine import Pin, PWM
     from logic import switch_ladder, dallas, HeavyDutyPWM
     #from neopixel import NeoPixel
     # Switches
     SW_ON = switch_ladder.Switch_ladder(Pin(5, Pin.IN), inverted=True)
     SW_OFF = switch_ladder.Switch_ladder(Pin(6, Pin.IN), inverted=True)
     #LEDS/RELAYS
     LED1 = Pin(17, Pin.OUT)
     #PWM output
     # pwm0 = PWM(Pin(23), freq=10, duty=0) # create PWM object from a pin
     #HEATER = HeavyDutyPWM(7, period=1)
     # Onboard NeoPixel LED
     # Dallas 18B20temperature sensor
     #DALLAS = dallas.Dallas(4, poll_period=1_000)
     print('IO configuration loaded')

The top 10 lines contain a description of the purpose of this file and the modules required for operation. There is no need to comment on unused modules (as long as your device has enough memory), but adding used modules is mandatory. In this file, below the `# Switches` comment, two buttons are described that are connected to the inputs of the esp32 module. One, as you might guess, is the ON button, the other is OFF.
Further, below the comment `#LEDS/RELAYS` it is described where the discrete output is connected, which can control, for example, a relay, an LED, or both. When describing your periphery, give the objects names that will make clear their purpose. (The author does not always do this - you can rename LED1 to something you like.)
After you describe the peripherals, write the changes to the esp32 module and press CTRL+D.

         MPY: soft reboot
     ********************
            REV 10
     ********************
     Global loading...
     Connected to access point gft
     Main interface IP address = 192.168.43.144
     Main starting
      IO configuration loaded
     Start application
     UPSTREAM Dispatcher started
     DOWNSTREAM Dispatcher started
     dispatherDOWN waiting for message...
    

The `IO configuration loaded` line tells you that the **hw.py** file is at least loaded.

### Application logic
It's time to describe the logic of the device and make it perform the intended, useful work for you. This logic is described in the `app.py` file. Open the file and pay attention to the first lines:
    
     PERIOD = 10 # ms # is the period with which the main program will be "scanned", i.e. be carried out
    
     import hw #peripheral descriptions are imported here, which you completed in the previous step
     from logic import Timer # these are the building blocks of your program
     from logic import Counter
     from logic import Seq
     from logic import Spark
     from logic import Revert
     from logic import OneShoot
     from logic import tag
     from logic import PID
    
Below are the lines with comments where you should place the configuration of those very "bricks" of applications.
Everything from the beginning of the file to the `onstart` function will be executed once when the device is turned on.
All "bricks" must be initialized before the main scan of the program is executed. (The main scan I will call the periodically called execution of the `normal` function). From the point of view of the Python programming language, these building blocks are objects. Each object occupies a certain place in memory to store its state. Therefore, objects should not be created when performing the main program scan. The size of the occupied memory should not change significantly - this is one of the conditions for the stability of the main scan, which can work for a very long time. Theoretically, forever.

After the program in the module is loaded, it is necessary to bring the periphery to its original state. (Of course, when designing the circuitry of the device, care must be taken that the peripherals start in a safe state). After starting and performing all the initializations of the "bricks", the program executes the code described in the `onstart()` function

#### start
First, this function (in Python's terms, it's a function) prints `Start application` to the REPL to ensure that the program has started during debugging. Secondly, this function should describe operations for bringing the periphery to its original state and, possibly, checking it. In the previous step, in the hw file, you described the LED (or relay) connected to the module and gave it a name. The author named it `LED1`. From the point of view of logic, it does not matter if an LED or a relay is connected to the module - in both cases the program considers it as `Discrete Output - DO`.
When the program starts, the LED must be off, the relay is released.

     def start():
         print('Start application')
         # Start code below
         hw.LED1.STATE = OFF

Pay attention to the indentation at the beginning of the line - they are important in Python.

#### normal
This function runs continuously while the device is on with the pause between scans specified in the first line
`app.py` file.

     def normal():
         # Normal executed code below
         if hw.SW_OFF.ON:
             hw.LED1.STATE = OFF
         else:
             hw.LED1.STATE = hw.LED1.STATE or hw.SW_ON.ON
         pass

The above program has two branches: one is executed when the SW_OFF button is pressed,
the other - otherwise. Ie, according to the meaning - when NOT pressed.
If the SW_OFF button is pressed, the LED turns off.
If the SW_OFF button is NOT pressed - the LED retains its current state or turns on if the SW_ON button is pressed.
If the LED is on, its state will not change until the SW_OFF button is pressed.