#!/bin/env python3

from record import start, finish
import turtle
import math


r = 50
n = 50
m = 3
a = 2*r*math.sin(math.pi/n)
b = 180*(1-2/n)

def circle(sgn):
    for i in range(n):
        turtle.forward(a)
        turtle.left(sgn*(180-b))

turtle.speed('fastest')

start(4*r, 4*r, 0, 0, 50, __file__)


for i in range(m):
    circle(1)
    circle(-1)
    turtle.left(180/m)


finish()