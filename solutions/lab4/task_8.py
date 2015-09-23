import robot
r = robot.rmap()
r.lm('task8')
r.sleep = 0.05

def move_hor(rb, d):
        if d == 1:
            rb.rt()
        elif d == -1:
            rb.lt()


def change_direction(d):
    if d == 1:
        return -1
    else:
        return 1


def can_move_hor(rb, d):
    if d == 1:
        return not rb.wr()
    elif d == -1:
        return not rb.wl()

    return False


def task():
    while not r.wu():
        r.up()

    while not r.wl():
        r.lt()

    d = 1
    w = 0
    col = 0

    while True:
        if not can_move_hor(r, d):
            if r.wd() or (w > 0 and col < w):
                break
            d = change_direction(d)
            r.dn()
            if w == 0:
                w = col + 1
            col = 0

        col += 1
        move_hor(r, d)

    if d == -1:
        r.up()
        r.lt()
        r.dn()

    c = 0
    h = 0
    while True:
        if r.wr():
            r.pt('red')
        else:
            c += 1
            if c > 1:
                break
        r.dn()
        h += 1

    r.up()

    while True:
        r.pt('red')
        if r.wl():
            break
        r.lt()

    y = 0
    while True:
        r.pt('red')
        if y >= h-1:
            break
        r.up()
        y += 1

    while True:
        r.pt('red')
        if r.wr():
            break
        r.rt()


r.start(task)
