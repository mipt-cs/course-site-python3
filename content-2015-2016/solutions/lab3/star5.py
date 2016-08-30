#!/bin/env python3

from record import start, finish
from star import draw

r = 100
n = 5

start(2*r, 2*r, 0, 0, 50, __file__)

draw(r, n)

finish()