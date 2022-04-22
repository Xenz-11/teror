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
5
def menu():
    pilih = '# MENU'
    mana = mark(pilih, style='yellow')
    sol().print(mana)
    menunya='[01] X-Spam\n[02] Spam Call\n[03] Spam Sms\n[04] Spam Whatsapp\n[05] Spam SWC\n[06] Hack Kamera\n[07] Down Wifi\n[EX]\x1b[1;91m EXIT\x1b[1;93m'
    cetak(menunya)
banner()
menu()