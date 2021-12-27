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
#     device.shell(f'input swipe 132 852 100 852 1000')
#     device.shell(f'input tap 89 739')
#     time.sleep(2)
#     device.shell(f'input swipe 132 949 100 949 1000')
#     device.shell(f'input tap 190 822')
#     time.sleep(3)
#     device.shell(f'input swipe 132 949 100 949 1000')
#     device.shell(f'input tap 256 829')
#     time.sleep(3)
#     device.shell(f'input swipe 132 949 100 949 1000')
#     device.shell(f'input tap 391 837')
#     time.sleep(3)
#     device.shell(f'input swipe 132 949 100 949 1000')
#     device.shell(f'input tap 444 842')
#     time.sleep(3)
#     device.shell(f'input swipe 132 949 100 949 1000')
#     device.shell(f'input tap 524 842')
#     time.sleep(3)
#     device.shell(f'input swipe 132 949 100 949 1000')
#     device.shell(f'input tap 610 855')
#     time.sleep(3)
#
