#!/bin/env python3

from record import start, finish
import turtle
import math


R = 50
r = 10
N = 20
n = 10
m = 5


def arc(r, n):
    a = 2*r*math.sin(math.pi/n/2)

    turtle.right(90/n)
    for i in range(n):
        turtle.forward(a)
        turtle.right(180/n)

    turtle.left(90/n)

l = m*2*R+(m-1)*2*r

start(l, R+r, -l/2, -(R+r)/2, 50, __file__)

turtle.left(90)

for i in range(m-1):
    arc(R, N)
    arc(r, n)

arc(R, N)

finish()