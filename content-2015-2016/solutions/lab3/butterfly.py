#!/bin/env python3

from record import start, finish
import turtle
import math


r = 50
n = 50
m = 10


def circle(r, sgn):
    a = 2*r*math.sin(math.pi/n)
    b = 180*(1-2/n)
    for i in range(n):
        turtle.forward(a)
        turtle.left(sgn*(180-b))

start(12*r, 6*r, 0, 0, 50, __file__)

turtle.speed('fastest')

turtle.left(90)

for i in range(m):
    circle(r, 1)
    circle(r, -1)
    r += 10


finish()