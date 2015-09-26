import robot
r = robot.rmap()
r.lm('task10')
r.sleep = 0.05


def find_dir(rb):
    if not rb.wd():
        return 2
    elif not rb.wr():
        return 1
    elif not rb.wl():
        return 3
    return 0


def paint_cell(rb, d):
    if (d == 1 and (not rb.wu() or not rb.wd()) and not rb.wr()) or \
       (d == 3 and (not rb.wu() or not rb.wd()) and not rb.wl()) or \
       (d == 2 and (not rb.wl() or not rb.wr()) and not rb.wd()):
        rb.pt('red')


def task():
    d = 1
    while True:
        if d == 1:
            r.rt()
            paint_cell(r, d)
            if r.wr():
                d = find_dir(r)
        elif d == 2:
            r.dn()
            paint_cell(r, d)
            if r.wd():
                d = find_dir(r)
        elif d == 3:
            r.lt()
            paint_cell(r, d)
            if r.wl():
                d = find_dir(r)
        else:
            break


r.start(task)
