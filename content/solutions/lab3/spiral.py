#!/bin/env python3

from record import start, finish
import turtle
import math

r = 5
n = 50

start(2*10*r, 2*10*r, 0, 0, 50, __file__)

turtle.penup()
turtle.forward(r)
turtle.left(90)
turtle.pendown()

for i in range(10):
    x = 5/n
    for j in range(n):
        a = 2*r*math.sin(math.pi/n)
        b = 180*(1-2/n)
        turtle.forward(a)
        turtle.left(180-b)
        r += x

finish()