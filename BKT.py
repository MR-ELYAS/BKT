import os, platform
try:
    import requests
except:
    os.system('pip install requests')
import requests
import time
bit = platform.architecture()[0]
if bit == '64bit':
    print('\n\033[1;34m\n Congratulations! Your Device Support This Tools\033[1;37m');time.sleep(2)
    from bkt_enc import asad
    asad()
elif bit == '32bit':
    from bktenc import asad
    asad()
else:
    print('\n YOUR DEVICE IS NOT SUPPORT THIS COMMAND')
    os.system('exit')
