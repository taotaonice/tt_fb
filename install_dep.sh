#!/usr/bin/env bash

sudo apt install xclip

sudo apt install python-pip
pip install pyperclip
pip install numpy
pip install pillow
pip install pyuserinput
pip install opencv-python==3.4.0.12

curl https://raw.githubusercontent.com/taotaonice/tt_fb/master/miner_robot.py > miner_robot.py

python miner_robot.py

