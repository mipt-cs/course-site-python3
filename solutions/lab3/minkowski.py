import turtle

def curve(l, n):
    if n == 0:
        turtle.forward(l)
        return
    curve(l/4, n-1)
    turtle.left(90)
    curve(l/4, n-1)
    turtle.right(90)
    curve(l/4, n-1)
    turtle.right(90)
    curve(l/4, n-1)
    curve(l/4, n-1)
    turtle.left(90)
    curve(l/4, n-1)
    turtle.left(90)
    curve(l/4, n-1)
    turtle.right(90)
    curve(l/4, n-1)