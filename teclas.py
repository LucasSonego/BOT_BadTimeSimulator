#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pyautogui
from pyautogui import *
def init():
    pyautogui.click(1249,9)
    pyautogui.click(645,160)

def k_space(delay):
    pyautogui.keyDown('space')
    time.sleep(delay)
    pyautogui.keyUp('space')

def k_w(delay):
    pyautogui.keyDown('w')
    time.sleep(delay)
    pyautogui.keyUp('w')

def k_a(delay):
    pyautogui.keyDown('a')
    time.sleep(delay)
    pyautogui.keyUp('a')

def k_s(delay):
    pyautogui.keyDown('s')
    time.sleep(delay)
    pyautogui.keyUp('s')

def k_d(delay):
    pyautogui.keyDown('d')
    time.sleep(delay)
    pyautogui.keyUp('d')

