#!/usr/bin/env python
# -*- coding: utf-8 -*-

from funcs import *

#entrar no jogo
alt_tab()
time.sleep(1)

#ready
k_space(0)
time.sleep(1)
k_space(0)

#começa a putaria

# iiiiii
time.sleep(0.8)
k_w(0.75)

# ~~~~
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

# ----====
time.sleep(1)
k_w(.3)
time.sleep(.3)
k_s(.25)
time.sleep(.3)
k_w(.3)
# ---

# compra item
time.sleep(2.5)
k_space(0)
time.sleep(.1)
k_d(0)
time.sleep(.1)
k_d(0)
time.sleep(.1)
k_d(0)
x = 0
while x < 4:
    time.sleep(.1)
    k_space(0)
    x += 1
x = 0
while x < 2:
    time.sleep(1)
    k_space(0)
    x += 1
x = 0
# =====

# Segunda fase
while x < 40:
    time.sleep(.1)
    k_w(0)
    x += 1
x = 0

#compra itens
while x < 4:
    time.sleep(.2)
    k_space(0)
    x += 1
x = 0
time.sleep(.5)
k_space(0)
time.sleep(1)
k_space(0)