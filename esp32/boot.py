# This file is executed on every boot (including wake-boot from deepsleep)
###
# 0. Globals  ##################################
print('*'*20)
print('REV 9'.center(20))
print('*'*20)

try:
    import G
except ImportError as e:
    print('!!! Problem on start')
    raise e

# 1. Connect to WiFi ##########################
#
import network
import time
try:
    import wificfg
except:
    print('Problem on import file wificfg.py')


if wificfg.modeAP:
    #################################################################### Acces point
    ap = network.WLAN(network.AP_IF) # create access-point interface
    ap.config(**wificfg.AP_Settings) # set the ESSID of the access point
    ap.active(True)         # activate the interface
    time.sleep(0.1)
    ################################################################### Access point

    G.MAIN_IF = ap.ifconfig()[0]
    print('Main interface IP address = {}'.format(G.MAIN_IF))
    #print('Hostname: {}'.format(network.hostname()))

if wificfg.modeSTA:
    # ##############################################################################
    wlan = network.WLAN(network.STA_IF)  # create station interface
    wlan.active(True)  # activate the interface
    if not wlan.isconnected():
        print('connecting to {} network...'.format(wificfg.STA_Settings['ssid']))
        wlan.connect(wificfg.STA_Settings['ssid'], wificfg.STA_Settings['key'])
        while not wlan.isconnected():
            time.sleep(1)
            pass
    print('Connected to access point {}'.format(wlan.config('essid')))
    # ##############################################################################

    G.MAIN_IF = wlan.ifconfig()[0]
    print('Main interface IP address = {}'.format(G.MAIN_IF))
    # print('Hostname: {}'.format(network.hostname())) TODO

    # wlan.ifconfig()  # get the interface's IP/netmask/gw/DNS addresses