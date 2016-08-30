import turtle

def curve(l, n):
    if n == 0:
        turtle.forward(l)
    else:
        curve(l/3, n-1)
        turtle.left(60)
        curve(l/3, n-1)
        turtle.right(120)
        curve(l/3, n-1)
        turtle.left(60)
        curve(l/3, n-1)

def snowflake(L, N):
    for i in range(3):
        curve(L, N)
        turtle.right(120)