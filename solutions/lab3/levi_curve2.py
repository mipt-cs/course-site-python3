#!/bin/env python3

from record import start, finish
from levi import curve
import turtle

L = 400
N = 2

start(2*L, 3*L/2, -L/2, -L/3, 50, __file__)

turtle.speed('fast')
curve(L, N)

finish()