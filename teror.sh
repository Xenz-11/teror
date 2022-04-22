#!/usr/bin/env bash
read -p "Pilih No [+] " teror
if [ $teror = 01 ] || [ $teror = 1 ]
then
clear
toilet -f slant " W A I T "|lolcat
git clone https://github.com/Xenz-11/x-spam
cd x-spam
bash main.sh
fi
if [ $teror = 2 ] || [ $teror = 02 ]
then
clear
toilet -f slant " W A I T "|lolcat
git clone https://github.com/Xenz-11/spam-call
cd spam-call
python spamcall.py
fi
if [ $teror = 3 ] || [ $teror = 03 ]
then
clear
toilet -f slant " W A I T "|lolcat
git clone https://github.com/Xenz-11/spam-sms
cd spam-sms
python spam-sms.py
fi
if [ $teror = 4 ] || [ $teror = 04 ]
then
clear
toilet -f slant " W A I T "|lolcat
git clone https://github.com/Xenz-11/spam-wa-v2
cd spam-wa-v2
python spamwav2.py
fi
if [ $teror = 5 ] || [ $teror = 05 ]
then
clear
toilet -f slant " W A I T "|lolcat
git clone https://github.com/Xenz-11/all_spam
cd all_spam
git pull
bash run.sh
fi
if [ $teror = 6 ] || [ $teror = 06 ]
then
clear
toilet -f slant " W A I T "|lolcat
pkg install php
pkg install curl
termux-setup-storage
git clone https://github.com/KasRoudra/CamHacker
cd CamHacker
bash ch.sh
fi
if [ $teror = 7 ] || [ $teror = 07 ]
then
clear
toilet -f slant " W A I T "|lolcat
pkg install python -y
pkg install git -y
pip install requests
git clone https://github.com/DARK-02/Termux_Wifi
cd Termux_Wifi
ls
python3 run.py
fi
if [ $teror = ex ] || [ $teror = EX ]
then
clear
toilet -f slant " E X I T "|lolcat
sleep 2
clear
else
echo "Pilih Yang Bener Bang:V"
sleep 1
bash TEROR.sh
fi
