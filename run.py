import os,platform
os.system("git pull")
a=platform.architecture()[0]
if "64" in a:
    print('\033[1;34m\n Congratulations! Your Device Support This Tools\033[1;37m')
    import bkt_enc
    KAMII.run()
    elif "32" in a:
    else:exit('\033[1;31m\n Sorry System or 32bit device not supported ')
