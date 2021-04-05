#!/usr/bin/env bash

sudo apt install xserver-xorg-core tigervnc-* ubuntu-gnome-desktop 

mkdir ~/.vnc/

echo '[ -x /etc/vnc/xstartup ] && exec /etc/vnc/xstartup' >> ~/.vnc/xstartup
echo '[ -r $HOME/.Xresources ] && xrdb $HOME/.Xresources' >> ~/.vnc/xstartup
echo 'vncconfig -iconic &' >> ~/.vnc/xstartup
echo 'dbus-launch --exit-with-session gnome-session &' >> ~/.vnc/xstartup

echo 'vncserver -localhost no -geometry 800x600 -depth 24 :1' > ~/vnc.sh
echo 'vncserver -kill :1' > ~/kill.sh
chmod +x ~/*.sh

wget "https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb"
sudo dpkg -i google*.deb
