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

def start(_canvas, _delay, _name):
    global canvas
    canvas = _canvas
    canvas.after(_delay, dump)

    global delay
    delay = _delay

    global name
    name = os.path.splitext(os.path.basename(_name))[0]

def finish():
    canvas.update()
    time.sleep(1)
    canvas.update()