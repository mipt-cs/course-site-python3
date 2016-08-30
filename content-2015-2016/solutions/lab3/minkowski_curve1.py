#!/bin/env python3

from record import start, finish
from minkowski import curve
import turtle


L = 800
N = 1

start(L, L, -L/2, 0, 50, __file__)

curve(L, N)

finish()