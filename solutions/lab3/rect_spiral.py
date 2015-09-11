#!/bin/env python3

from record import start, finish
import turtle

start(200, 200, 0, 0, 50, __file__)

a = 10
for i in range(40):
    turtle.forward(a)
    turtle.left(90)
    a += 5

finish()