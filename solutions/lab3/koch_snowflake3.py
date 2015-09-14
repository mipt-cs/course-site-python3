#!/bin/env python3

from record import start, finish
from koch import snowflake
import turtle
import sys

L = 300
H = L/6*3**0.5
N = 3

start(L, 4*H, -L/2, H, 50, __file__)

turtle.speed('fast')
snowflake(L, N)

finish()