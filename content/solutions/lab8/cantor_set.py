from record import start, finish
import turtle

def cantor_set(x, y, l, n):
    if n == 0:
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()

        turtle.forward(l)
        return

    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

    turtle.forward(l)

    cantor_set(x, y-30, l/3, n-1)
    cantor_set(x + l*2/3, y-30, l/3, n-1)

L = 600
N = 2
X = -L/2
Y = 15 * N

start(L, 2 * Y, X, Y, 50, __file__)

turtle.penup()
turtle.goto(X, Y)
turtle.pendown()

cantor_set(X, Y, L, N)
finish()
