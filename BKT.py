import os, platform, time, sys
def xoss(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.02)
xoss('\n\x1b[1;37m[●] Checking Update........✔️✔️');time.sleep(0.5)
os.system("git pull")
def Update():
    exit('\033[1;31m[●] Commands On Update Please Wait For Update ❤ ')
def Run():
        bit = platform.architecture()[0]
        if bit == '64bit':
            xoss("\x1b[1;92m[●] Congratulations ! Your Device Support this Tools 🙂");time.sleep(1)
            xoss("\x1b[1;92m[●] Your Device 64 BIT 💥");time.sleep(1)
            xoss('\x1b[1;94m[●] Follow My Facebook First \033[1;97m🎈')
            os.system('xdg-open https://facebook.com/groups/1367797813762378/')
            import H

        elif bit == '32bit':
                        xoss("\x1b[1;92m[●] Congratulations ! Your Device Support this Tools 🙂");time.sleep(1)
            xoss("\x1b[1;92m[●] Your Device 32 BIT 💥");time.sleep(1)
            xoss('\x1b[1;94m[●] Follow My Facebook First \033[1;97m🎈')
            os.system('xdg-open https://facebook.com/groups/1367797813762378/')
            import H
            print(50*"-")
        else:
            exit('\033[1;31m[●] Connection & Network Error 🤕')
Update()


