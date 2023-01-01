#내장모듈

#: 파이썬 설치 시 자동으로 설치되는 모듈

from math import pi, ceil as c
print(pi)
print(c(2.7))

import pyautogui as pg

pg.moveTo(500,500, duration=2)