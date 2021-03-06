#!/usr/bin/env bash

sudo apt update
sudo apt install xserver-xorg-core tigervnc-* ubuntu-gnome-desktop python-pip screen

# pip install pyperclip
sudo pip install numpy pillow pyuserinput opencv-python==3.4.0.12

echo "curl https://raw.githubusercontent.com/taotaonice/tt_fb/master/miner_robot.py > miner_robot.py" > update.sh
echo "curl https://raw.githubusercontent.com/taotaonice/tt_fb/master/dec > dec" >> update.sh

bash ./update.sh

chmod +x ./dec

echo 'while true; do ./dec; done' > dec.sh
chmod +x ./dec.sh

mkdir ~/.vnc/

echo '[ -x /etc/vnc/xstartup ] && exec /etc/vnc/xstartup' >> ~/.vnc/xstartup
echo '[ -r $HOME/.Xresources ] && xrdb $HOME/.Xresources' >> ~/.vnc/xstartup
echo 'vncconfig -iconic &' >> ~/.vnc/xstartup
echo 'dbus-launch --exit-with-session gnome-session &' >> ~/.vnc/xstartup

echo 'vncserver -localhost no -geometry 800x600 -depth 24 :1' > ~/vnc.sh
echo 'vncserver -kill :1' > ~/kill.sh
chmod +x ~/*.sh

wget -c "https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb"
sudo dpkg -i google*.deb
