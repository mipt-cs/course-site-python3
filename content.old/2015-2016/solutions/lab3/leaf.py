import turtle

def draw(l, n):
    if n == 0:
        turtle.left(180)
        return

    x = l/(n+1)
    for i in range(n):
        turtle.forward(x)
        turtle.left(45)
        draw(0.5*x*(n-i-1), n-i-1)
        turtle.left(90)
        draw(0.5*x*(n-i-1), n-i-1)
        turtle.right(135)

    turtle.forward(x)
    turtle.left(180)
    turtle.forward(l)