import time

from ppadb.client import Client as AdbClient

def connect():
    client = AdbClient(host="127.0.0.1", port=5037) # Default is "127.0.0.1" and 5037

    devices = client.devices()

    if len(devices) == 0:
        print('No devices')
        quit()

    device = devices[0]

    print(f'Connected to {device}')

    return device, client

if __name__ == '__main__':
    device, client = connect()
    #
    #
    # device.shell('input keyevent 26')
    # time.sleep(1)
    # device.shell('input  swipe 200 500 200 0')
    # time.sleep(2)
    device.shell('am start -n com.android.chrome/com.google.android.apps.chrome.Main')
    time.sleep(2)
    # device.shell(f'input tap 660 201')
    # time.sleep(2)
    # device.shell(f'input tap 314 306')
    # time.sleep(2)
    # device.shell('input  swipe 550 1000 550 0')
    # device.shell('input  swipe 550 850 550 0')
    # time.sleep(2)
    # device.shell(f'input tap 360 860')
    # time.sleep(6)
    # device.shell('input  swipe 550 1000 550 0')
    # device.shell('input  swipe 550 1000 550 0')
    # time.sleep(2)