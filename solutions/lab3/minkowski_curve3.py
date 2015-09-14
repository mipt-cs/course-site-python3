#!/bin/env python3

from record import start, finish
from minkowski import curve
import turtle


L = 800
N = 3

start(L, L, -L/2, 0, 50, __file__)

turtle.speed('fastest')
curve(L, N)

finish()