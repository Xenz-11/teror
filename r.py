
from time import sleep
import requests,random,json,time,sys,os,re
def xenz(text):
        for x in text + '\n':
                sys.stdout.write(x)
                sys.stdout.flush()
                sleep(random.random() * 0.2)
os.system("clear")
xenz("\x1b[1;93mfollow fb gw dulu bang\x1b[1;92m>_<\x1b[00")
time.sleep(1)
os.system("xdg-open https://www.facebook.com/inu.pembangkang.7")
time.sleep(3)
os.system("cd module\npython xenzganteng.py")