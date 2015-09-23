import robot
r = robot.rmap()
r.lm('task9')
r.sleep = 0.03


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

    while True:
        if r.label() == 'green':
            break

        if not can_move_hor(r, d):
            if r.wd():
                break
            d = change_direction(d)
            r.dn()
            if r.label() == 'green':
                break

        move_hor(r, d)

    w = 0
    h = 0

    while True:
        if r.label() != 'green':
            if d == 1:
                r.lt()
            else:
                r.rt()
            break
        w += 1

        if can_move_hor(r, d):
            move_hor(r, d)
        else:
            break

    while True:
        if r.label() != 'green':
            break

        h += 1

        if r.wd():
            break
        else:
            r.dn()

    r.res.config(text='S = ' + str(w*h))

r.start(task)
