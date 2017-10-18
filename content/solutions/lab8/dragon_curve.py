from record import start, finish
import turtle

def curve(l, n, direction=45):
   if n == 0:
       turtle.forward(l)
       return
   turtle.right(direction)
   curve(l/2, n-1, 45)
   turtle.left(direction * 2)
   curve(l / 2, n - 1, -45)
   turtle.right(direction)


L = 800
N = 5

#turtle.speed('fastest')

start(L/2, L/2, -L/6, 0, 50, __file__)
#turtle.penup()
#turtle.goto(-L/2, -L/3)
#turtle.pendown()

curve(L, N)
finish()