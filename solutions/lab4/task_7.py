import robot
r = robot.rmap()
r.lm('task7')
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
    d = -1
    while True:
        if r.wl() and r.wu():
            break
        if not r.wu():
            r.up()
        elif d == 1:
            if r.wr():
                d = -1
            else:
                r.rt()
        else:
            if r.wl():
                d = 1
            else:
                r.lt()

    d = 1
    c = 0

    while True:
        if r.wu() and r.wd():
            c += 1
        else:
            c = 0

        if c > 1:
            break

        if not can_move_hor(r, d):
            if r.wd():
                break
            d = change_direction(d)
            r.dn()

        move_hor(r, d)

    if c > 1:
        if d == 1:
            r.lt()
        else:
            r.rt()

        while r.wd() and r.wu():
            r.pt('red')
            move_hor(r, d)


r.start(task)
