#!/bin/env python3

from record import start, finish
from leaf import draw
import turtle

L = 400
N = 2
LL = L/N*(N+1)

start(LL, LL, 0, -LL/2, 50, __file__)

turtle.left(90)
draw(L, N)

finish()