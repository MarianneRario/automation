import random, threading, webbrowser, time
from ppadb.client import Client as AdbClient
from flask import Flask

def connect():
    client = AdbClient(host="127.0.0.1", port=5037) # Default is "127.0.0.1" and 5037
    devices = client.devices()

    if len(devices) == 0:
        print("No devices")
        quit()

    device = devices[0]

    print(f"Connected to {device}")

    return device, client

app = Flask(__name__)

device, client = connect()
device.shell('am start -n com.android.chrome/com.google.android.apps.chrome.Main '
             '-d https://www.facebook.com/manilabulletin/videos/415232433264613')
time.sleep(10)
device.shell(f'input swipe 360 664 360 164 1000')
time.sleep(3)
device.shell(f'input tap 384 1053')
time.sleep(3)
device.shell(f"input swipe 360 664 360 120 1000")
time.sleep(3)
device.shell(f"input tap 147 1115")
time.sleep(3)
device.shell(f"input tap 121 465")
time.sleep(3)
comment = f"Congrats! #PinoyPride"
device.shell(f'input text "{comment}"')
time.sleep(4)
device.shell(f"input tap 653 351")
time.sleep(3)