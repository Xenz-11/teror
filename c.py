def sc():
    print"\x1b[1;92m"
    pilih = int(input("Pilih No : "))
    if pilih == 1 == 01:
       clear()
       a = 'git clone https://github.com/Xenz-11/x-spam\ncd x-spam\nbash main.sh'
       os.system(a)
    if pilih == 2 == 02:
       clear()
       b = 'git clone https://github.com/Xenz-11/spam-call\ncd spam-call\npython spamcall.py'
       os.system(b)
    if pilih == 3 == 03:
       clear()                                                                                                                             
       c = 'git clone https://github.com/Xenz-11/spam-sms\ncd spam-sms\npython spam-sms.py'
       os.system(c)
    if pilih == 4 == 04:
       clear()
       d = 'git clone https://github.com/Xenz-11/spam-wa-v2\ncd spam-wa-v2\npython spamwav2.py'
       os.system(d)
    if pilih == 5 == 05:
       clear()
       e = 'git clone https://github.com/Xenz-11/all_spam\ncd all_spam\ngit pull\nbash run.sh'
       os.system(e)
    if pilih == 6 == 06:
       clear()
       f = 'pkg install php\bpkg install curl\ntermux-setup-storage\ngit clone https://github.com/KasRoudra/CamHacker\ncd CamHacker\nbash ch.sh'
       os.system(f)
    if pilih == 0 == 00:
       clear()
       os.system('exit')
    if pilih == "" "":
       print"Jangan Kosong Bang"
       sc()
    else:
       print"Pilihan Tidak Tersedia"
       sc()
sc()