


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
import sys

m = PyMouse()
k = PyKeyboard()

dsp = display.Display()
root = dsp.screen().root

last_end_time = time.time()
cur_end_time = time.time() - 24*60*60 - 600

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
    time.sleep(5)
    k.tap_key(k.home_key)
    time.sleep(0.5)
    m.click(120, 414, 1)
    time.sleep(1)
    """
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
    """
    cksum = get_crop_sum(204, 406, 30, 20)
    if cksum == 417021:
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
    time.sleep(1)

def watch_dog():
    now = time.time()
    while True:
        if time.time() - now >= 60*60*24:
            break
        cksum = get_crop_sum(15, 108, 40, 40)
        if cksum != 985667:
            m.click(330, 534, 1)
            k.tap_key(k.function_keys[5])
        time.sleep(300)

def close_and_swap():
    time.sleep(2)
    k.press_key(k.control_key)
    k.tap_key('w')
    k.release_key(k.control_key)
    time.sleep(3)
    m.click(767, 133, 1)
    ready = False
    while not ready:
        cksum = get_crop_sum(457, 185, 54, 44)
        print(cksum)
        ready = cksum == 1817640
        time.sleep(1)
    m.click(550, 422, 1)
    time.sleep(2)
    k.press_key(k.control_key)
    time.sleep(0.5)
    k.tap_key(k.tab_key)
    time.sleep(3)
    k.tap_key('w')
    time.sleep(1)
    k.release_key(k.control_key)

    ready = False
    while not ready:
        cksum = get_crop_sum(20, 38, 16, 11)
        ready = cksum == 87681
        time.sleep(1)
    m.press(223, 593, 1)
    time.sleep(1)
    m.move(647, 593)
    time.sleep(1)
    m.release(647, 593, 1)
    time.sleep(1)

    m.click(206, 553, 1, 2)


def semi_automatic_machine():
    time.sleep(2)
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


while True:
    if time.time() - cur_end_time >= 24*60*60 + 600:
        semi_automatic_machine()
        down = False
        while not down:
            time.sleep(300)
            cksum = get_crop_sum(538, 171, 73, 19)
            down = cksum == 941148
        cur_end_time = time.time()
        close_and_swap()
        last_end_time, cur_end_time = cur_end_time, last_end_time

        wait_time = cur_end_time + 24*60*60 + 600 - time.time()
        if wait_time > 0:
            time.sleep(wait_time)
    else:
        time.sleep(60)

dsp.close()
