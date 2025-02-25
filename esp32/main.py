from machine import Pin
from network import WLAN, STA_IF

import utime
import requests
import dht

UBIDOTS_API_KEY = "BBUS-8SJzjhAMrwcF1bWXASsP9o9UuyjY9M"
MACHINE = "esp32-uni436"
UBIDOTS_URL = "http://industrial.api.ubidots.com/api/v1.6/devices/" + MACHINE
SSID = "Wokwi-GUEST"
PASSWORD = ""

LABELS = ["dht", "hcsr"]

DHT = Pin(4, Pin.IN)
HC_SR501 = Pin(15, Pin.IN)
# DHT = Pin(4, Pin.IN)
# HC_SR501 = Pin(5, Pin.IN)

# Set up the WLAN
wlan = WLAN(STA_IF)
wlan.active(True)
wlan.connect(SSID, PASSWORD)

# Get current time in ISO 8601 format
def get_iso_timestamp():
    year, month, day = utime.localtime()[0:3]
    hour, minute, second = utime.localtime()[3:6]
    return "{:04d}-{:02d}-{:02d}T{:02d}:{:02d}:{:02d}Z".format(
        year, month, day, hour, minute, second
    )

def create_payload(data):

    payload = {
        "temp_c": data["dht"]["temp_c"],
        "temp_f": data["dht"]["temp_f"],
        "hum": data["dht"]["hum"],
        "distance": data["hcsr"],
    }

    return payload


def post_to_ubidots(payload):
    try:
        status = 400
        attempts = 0
        backoff = 1
        headers = {"X-Auth-Token": UBIDOTS_API_KEY, "Content-Type": "application/json"}

        while status >= 400 and attempts < 5:
            try:
                req = requests.post(url=UBIDOTS_URL, headers=headers, json=payload)
                status = req.status_code
                print(f"[INFO] Attempt {attempts + 1}: Status {status}")
                
                if status < 400:
                    print("[INFO] Request successful")
                    print(req.json())
                    return True
                    
            except OSError as e:
                print(f"[ERROR] Network error: {e}")
                status = 500
            
            attempts += 1
            sleep_time = backoff * 2 ** attempts
            print(f"[INFO] Retrying in {sleep_time} seconds...")
            utime.sleep(sleep_time)

        print("[ERROR] Failed after 5 attempts")
        return False
        
    except Exception as e:
        print(f"[ERROR] Unexpected error: {e}")
        return False


def rest_api(data):

    try:
        url_dht = "http://localhost:8000/dht"
        url_hcsr = "http://localhost:8000/hcsr"

        dht_data = {
            "temperature": data["temp_c"],
            "humidity": data["hum"],
            "timestamp": get_iso_timestamp(),
        }

        hcsr_data = {
            "motion": data["distance"],
            "timestamp": get_iso_timestamp(),
        }
        
        dht_response = requests.post(url_dht, json=dht_data)
        hcsr_response = requests.post(url_hcsr, json={"motion": hcsr_data})
        
        if dht_response.status_code == 200 and hcsr_response.status_code == 200:
            print("[INFO] Data sent successfully to REST API")
            return True
        else:
            print("[ERROR] Failed to send data to REST API")
            return False
            
    except Exception as e:
        print(f"[ERROR] REST API error: {e}")
        return False


def read_sensor():
    dht_22_data = dht_22()
    hcsr_data = hcsr()

    data = {
        LABELS[0]: dht_22_data,
        LABELS[1]: hcsr_data,
    }

    return data


def dht_11():
    sensor = dht.DHT22(DHT)
    try:
        sensor.measure()
        temp = sensor.temperature()
        hum = sensor.humidity()
        temp_f = temp * (9 / 5) + 32.0

        res = {
            "temp_c": temp,
            "temp_f": temp_f,
            "hum": hum,
        }

        return res
    except OSError as e:
        print("Failed to read sensor.")


def dht_22():
    sensor = dht.DHT22(DHT)
    try:
        sensor.measure()
        temp = sensor.temperature()
        hum = sensor.humidity()
        temp_f = temp * (9 / 5) + 32.0

        res = {
            "temp_c": temp,
            "temp_f": temp_f,
            "hum": hum,
        }

        return res
    except OSError as e:
        print("Failed to read sensor.")


# HCSR501 PIR Motion Sensor
motion = 0

def hcsr():
    motion = HC_SR501.value()

    utime.sleep(0.1)  # Sleep for 100 milliseconds

    return motion


while True:
    data = read_sensor()
    payload = create_payload(data)
    post_to_ubidots(payload)

    print(data)
    utime.sleep(5)
