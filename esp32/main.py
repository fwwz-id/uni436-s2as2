from machine import Pin
from network import WLAN, STA_IF
from utime import sleep

import dht

SSID = "Wokwi-GUEST"
PASSWORD = ""

# Set up the WLAN
wlan = WLAN(STA_IF)
wlan.active(True)
wlan.connect(SSID, PASSWORD)

def rest_api():
    return

def read_sensor():
    dht_22_data = dht_22()

    data = {
        "dht": dht_22_data
    }

    return data
    

def dht_11():
    return

def dht_22():
    sensor = dht.DHT22(Pin(4))
    try:
        sensor.measure()
        temp = sensor.temperature()
        hum = sensor.humidity()
        temp_f = temp * (9/5) + 32.0
        
        res = {
            "temp_c": temp,
            "temp_f": temp_f,
            "hum": hum,
        }

        return res
    except OSError as e:
        print('Failed to read sensor.')

def hcsr():
    return

def ldr():
    return

while(True):
    data = read_sensor()
    print(data)
    sleep(5)