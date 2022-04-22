import requests,bs4,json,os,sys,random,datetime,time,re

from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col


x = '\33[m' # DEFAULT
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
def clear():
    os.system("clear")

def banner():
    clear()
    ganz = '# WELCOME TO TEROR'
    xenz = mark(ganz, style='cyan')
    sol().print(xenz)
    au='\x1b[1;92m[•]\x1b[1;93m Author   : Xenz\n\x1b[1;92m[•]\x1b[1;93m Github   : github.com/Xenz-11\n\x1b[1;92m[•]\x1b[1;93m Facebook : Xenz Why'
    pengembang1=nel(au,style="cyan")
    cetak(nel(pengembang1, title='[ INFORMASI PENGEMBANG ]'))




def loginn():
    login1 = '# LOGIN'
    login=mark(login1, style="yellow")
    sol().print(login)
    asu = 'Xenz'
    tai = 'Ganz'
    print('[\x1b[1;91m!\x1b[00m] ASAL AJA KALO GA TAU')
    us = input('\x1b[1;96mUsername : ')
    if us == asu:
       pas = input('Password : ')
       if pas == tai:
          print('\n\x1b[1;92mBerhasil Login\x1b[00m')
          time.sleep(2)
          clear()
          banner()
       else:
          print('\x1b[1;91mPassword Salah\x1b[00m')
          time.sleep(3)
          banner()
          loginn()
    else:
       print('\x1b[1;91mUsername Salah\x1b[00m')
       os.system('xdg-open https://wa.me/6283138613993?text=Bang+Xenz+Minta+Username+Sama+Password+TEROR')
       time.sleep(3)
       banner()
       loginn()
       
banner()
loginn()