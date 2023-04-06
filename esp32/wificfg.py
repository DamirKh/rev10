modeAP = True  # set to True for making self access point

AP_Settings = {
    'essid': 'ESP32-AP',
    'max_clients': 4,
    'password': '12344321'
}


modeSTA = False  # set tot True to connect to existing access point
STA_Settings = {
    'ssid': 'YourAccessPointName',
    'key': 'StrongPassword'
}
