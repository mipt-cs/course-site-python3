import turtle
import time
import os

canvas = None
delay = None
index = 0

def dump():
    global index
    canvas.postscript(file='%s.%05d.ps' % (name, index))
    index += 1
    canvas.after(delay, dump)

def start(width, height, x, y, _delay, _name):
    turtle.setup(width+45, height+45)
    turtle.screensize(width+15, height+15)
    turtle.up()
    turtle.goto(x, y)
    turtle.pendown()

    turtle.shape('turtle')
    global canvas
    canvas = turtle.getscreen().getcanvas()
    canvas.after(_delay, dump)

    global delay
    delay = _delay

    global name
    name = os.path.splitext(os.path.basename(_name))[0]

def finish():
    canvas.update()
    time.sleep(1)
    canvas.update()