#!/bin/env python3

from record import start, finish
import turtle
import math

r = 100
n = 5
a = 2*r*math.sin(math.pi/n)
l = a/(2*(1-math.cos(math.pi/n)))**0.5

start(2*r, 2*r, 0, 0, 50, __file__)

turtle.penup()
turtle.left(90-360/n)
turtle.forward(r)
turtle.left(180-90/n)
turtle.pendown()

for i in range(n):
    turtle.forward(l)
    turtle.left(180-180/n)

finish()