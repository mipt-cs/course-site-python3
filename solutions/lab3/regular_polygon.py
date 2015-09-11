#!/bin/env python3

from record import start, finish
import turtle
import math

r = 30
n = 3
a = 2*r*math.sin(math.pi/n)
b = 180*(1-2/n)

start(460, 460, 0, 0, 50, __file__)

turtle.penup()
turtle.forward(r)
turtle.pendown()

for i in range(10):
    a = 2*r*math.sin(math.pi/n)
    b = 180*(1-2/n)
    turtle.left(180-b/2)

    for j in range(n):
        turtle.forward(a)
        turtle.left(180-b)

    turtle.right(180-b/2)
    turtle.penup()
    turtle.forward(20)
    turtle.down()

    n += 1
    r += 20

finish()