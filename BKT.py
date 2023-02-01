import os, platform
try:
    import requests
except:
    os.system('git pull')
import requests
import time
os.system('clear')
print('BKT TOOL ON UPDATE WAIT FOR UPDATE');exit()
bit = platform.architecture()[0]
if bit == '64bit':
    print('\033[1;34m\n Congratulations! Your Device Support This Tools\033[1;37m');time.sleep(2)
    from BKT2 import asad
    asad()
elif bit == '32bit':
    print('\n YOUR DEVICE IS NOT SUPPORT THIS COMMAND')
    os.system('exit')
