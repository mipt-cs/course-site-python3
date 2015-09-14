#!/bin/env python3

from record import start, finish
from koch import curve
import turtle


L = 800
H = L/6*3**0.5
N = 2

start(L, H, -L/2, -H/2, 50, __file__)

curve(L, N)

finish()