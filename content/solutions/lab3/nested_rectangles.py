#!/bin/env python3

from record import start, finish
import turtle

start(200, 200, 0, 0, 50, __file__)

l = 20
for i in range(10):
    turtle.penup()
    turtle.goto(-l/2, -l/2)
    turtle.pendown()
    for k in range(4):
        turtle.forward(l)
        turtle.left(90)
    l += 20

finish()