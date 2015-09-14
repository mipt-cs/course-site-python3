import turtle
import math

def draw(r, n):
    a = 2*r*math.sin(math.pi/n)
    l = a/(2*(1-math.cos(math.pi/n)))**0.5

    turtle.penup()
    turtle.left(90-360/n)
    turtle.forward(r)
    turtle.left(180-90/n)
    turtle.pendown()

    for i in range(n):
        turtle.forward(l)
        turtle.left(180-180/n)