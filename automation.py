# import time
#
# from ppadb.client import Client as AdbClient
#
# def connect():
#     client = AdbClient(host="127.0.0.1", port=5037) # Default is "127.0.0.1" and 5037
#
#     devices = client.devices()
#
#     if len(devices) == 0:
#         print('No devices')
#         quit()
#
#     device = devices[0]
#
#     print(f'Connected to {device}')
#
#     return device, client
#
# if __name__ == '__main__':
#     device, client = connect()
#
#     device.shell('am start -n com.facebook.katana/com.facebook.katana.LoginActivity')
#
#     time.sleep(3)
#
#     post = f'Automated post from Python device shell'
#
#     post_points = '140, 315'
#
#     device.shell(f'input tap 180 309')
#
#     time.sleep(3)
#
#     device.shell(f'input tap 91 428')
#
#     time.sleep(3)
#
#     device.shell(f'input tap 160 594')
#
#     time.sleep(3)
#
#     device.shell(f'input text "{post}"')
#
#     device.shell('input keyevent 66')
#
#     time.sleep(3)
#
#     device.shell(f'input tap 632 109')
#
#     time.sleep(3)
#
#
#
