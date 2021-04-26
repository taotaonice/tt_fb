
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Xlib import display, X
from PIL import Image
import numpy as np

import cv2
import pymouse, pykeyboard, os, sys
from pymouse import PyMouse
from pykeyboard import PyKeyboard
import pyperclip
import time

m = PyMouse()
k = PyKeyboard()

dsp = display.Display()
root = dsp.screen().root

def cvshow(mat, title=''):
    cv2.imshow(title, mat)
    cv2.waitKey(0)

def screen_shot(x=0, y=0, w=-1, h=-1):
    if w == -1 or h == -1:
        w = root.get_geometry().width
        h = root.get_geometry().height
    raw = root.get_image(x, y, w, h, X.ZPixmap, 0xffffffff)
    image = Image.frombytes("RGB", (w, h), raw.data, "raw", "BGRX")
    image = np.array(image)[:, :, ::-1]
    #  print(root.get_geometry())
    # cv2.imshow('abc', image)
    # cv2.waitKey(0)
    return image

def get_crop_sum(x=0, y=0, w=-1, h=-1):
    return screen_shot(x, y, w, h).sum()

def open_colab_label(toggle=False):
    #k.tap_key(k.function_keys[5])
    if toggle:
        k.press_key(k.control_key)
        k.tap_key(k.tab_key)
        k.release_key(k.control_key)
    time.sleep(0.5)
    #k.tap_key(k.function_keys[5])

    time.sleep(2)
    """
    ready = False
    while not ready:
        cksum = get_crop_sum(18, 37, 18, 13) + get_crop_sum(234, 37, 18, 13)
        print(cksum)
        ready = cksum == 251877
        time.sleep(1)
    print('debug')
    """

    time.sleep(1)
    m.click(441, 398, 1)
    time.sleep(1)
    k.tap_key(k.right_key)
    time.sleep(1)
    k.tap_key(k.right_key)

    k.tap_key(k.enter_key)
    time.sleep(5)
    ready = False
    while not ready:
        cksum = get_crop_sum(529, 168, 80, 30)
        ready = cksum == 1745682
        time.sleep(1)
    print('open colab label ready')

def check_gpu():
    k.tap_key(k.home_key)
    time.sleep(0.5)
    m.click(120, 414, 1)
    time.sleep(1)
    m.press(196, 414, 1)
    time.sleep(1)
    m.release(238, 414, 1)
    k.press_key(k.control_key)
    k.tap_key('c')
    k.release_key(k.control_key)
    time.sleep(1)
    gpu_str = pyperclip.paste()
    if 'V' in gpu_str:
        print('V100')
        return True
    else:
        print('P100')
        return False

def draw_an_instance():
    k.tap_key(k.home_key)
    time.sleep(0.5)
    m.click(82, 243, 1)
    ready = False
    while not ready:
        cksum = get_crop_sum(497, 169, 56, 25)
        ready = cksum == 981471
        time.sleep(1)
    print('drawn an instance')

def reset_instance():
    time.sleep(0.5)
    m.click(261, 153, 1)
    time.sleep(1)
    ready = False
    while not ready:
        cksum = get_crop_sum(255, 395, 141, 24)
        ready = cksum == 2374236
        time.sleep(1)

    m.click(335, 413, 1) # click Factory reset runtime

    ready = False
    while not ready:
        cksum = get_crop_sum(682, 408, 58, 11)
        ready = cksum == 409237
        time.sleep(1)

    m.click(714, 420, 1)
    time.sleep(1)

def close_label():
    time.sleep(0.5)
    k.press_key(k.control_key)
    k.tap_key('w')
    k.release_key(k.control_key)
    time.sleep(2)
    cksum = get_crop_sum(500, 170, 100, 50)
    print(cksum)
    if cksum == 2860611:
        m.click(576, 201, 1)
    time.sleep(1)

def run_all_and_mine():
    time.sleep(0.5)
    k.press_key(k.control_key)
    k.tap_key(k.function_keys[9])
    k.release_key(k.control_key)
    time.sleep(60)

    m.click(26, 558, 1)
    time.sleep(5)
    m.click(647, 379, 1)
    time.sleep(0.5)
    k.type_string('cd ')
    k.tap_key(k.enter_key)
    time.sleep(0.5)
    k.type_string('cd code ')
    k.tap_key(k.enter_key)
    time.sleep(0.5)
    k.type_string('./run.sh ')
    k.tap_key(k.enter_key)


def semi_automatic_machine():
    open_colab_label()
    V100 = False
    while not V100:
        draw_an_instance()
        time.sleep(2)
        V100 = check_gpu()
        if V100:
            break
        else:
            reset_instance()
        time.sleep(300)

    run_all_and_mine()
"""
open_colab_label()
draw_an_instance()
time.sleep(2)
check_gpu()
reset_instance()
close_label()
"""

semi_automatic_machine()

dsp.close()
