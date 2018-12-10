#!/usr/bin/env python
# -*- coding: utf-8 -*-

from base import *

def start():
    '''entra no jogo'''
    k_alt_tab()
    time.sleep(1)
    '''/entra no jogo'''

    '''ready'''
    k_space(0)
    time.sleep(1)
    k_space(0)
    '''/ready'''

''' Fase 1'''
def fase1():
    time.sleep(0.8)
    k_w(0.75)
    time.sleep(0.2)
    k_w(0.01)
    time.sleep(0.08)
    k_s(0.002)
    time.sleep(0.06)
    k_w(0.01)
    time.sleep(0.05)
    k_w(0.08)
    time.sleep(0.2)
    k_s(0.15)
    time.sleep(1)
    k_w(.3)
    time.sleep(.25)
    k_s(.25)
    time.sleep(.3)
    k_w(.3)
    time.sleep(1)
    k_space(0)
    print("Fim da função 'fase1'")

def fase2():
    '''compra itens'''
    time.sleep(.5)
    k_space(0)
    time.sleep(.2)
    k_space(0)
    x = 0
    while x < 3:
        time.sleep(.1)
        k_d(0)
        x += 1
    x = 0
    while x < 4:
        time.sleep(.1)
        k_space(0)
        x += 1
    x = 0
    while x < 2:
        time.sleep(.6)
        k_space(0)
        x += 1
    x = 0
    '''/compra itens'''

    '''segunda fase'''
    while x < 40:
        time.sleep(.1)
        k_w(0)
        x += 1
    x = 0
    '''/segunda fase'''

    '''compra itens'''
    while x < 4:
        time.sleep(.2)
        k_space(0)
        x += 1
    x = 0
    time.sleep(.5)
    k_space(0)
    time.sleep(1)
    k_space(0)
    '''/compra itens'''
    print("Fim da função 'fase2'")

def fase3():
    time.sleep(.2)
    y = 0
    while y < 4:
        x = 0
        while x < 4:
            time.sleep(.6)
            k_w(.05)
            x += 1
        y += 1
    x = 0
    y = 0
    time.sleep(1)
    '''compra itens'''
    while x < 2:
        time.sleep(1)
        k_space(0)
        x += 1
    x = 0
    '''/compra itens'''
    print("Fim da função 'fase3'")

def finish():
    k_alt_tab()
    print("Fim da função 'finish'")
