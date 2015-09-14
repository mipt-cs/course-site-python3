import turtle

def curve(l, n):
    if n == 0:
        turtle.forward(l)
        return
    turtle.left(45)
    curve(l/2**0.5, n-1)
    turtle.right(90)
    curve(l/2**0.5, n-1)
    turtle.left(45)