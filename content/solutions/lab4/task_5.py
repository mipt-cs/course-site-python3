import robot
r = robot.rmap()
r.lm('task5')


def can_move_hor(rb, d):
    if d == 1:
        return not rb.wr()
    elif d == -1:
        return not rb.wl()

    return False


def move_hor(rb, d):
        if d == 1:
            rb.rt()
        elif d == -1:
            rb.lt()


def paint_row(rb, period, rem, d):
    col = 0
    while True:
        if col % period == rem:
            rb.pt('red')

        if can_move_hor(rb, d):
            move_hor(rb, d)
        else:
            break

        col += 1


def task():
    row = 0
    while True:
        if row % 3 == 0:
            paint_row(r, 2, 0, 1)
        elif row % 3 == 1:
            paint_row(r, 4, 1, -1)

        if r.wd():
            break
        else:
            r.dn()

        row += 1


r.start(task)
