import robot
r = robot.rmap()
r.lm('task11')
r.sleep = 0.05


def task():
    while not r.wl():
        r.lt()

    while not r.wu():
        r.up()

    s = 99
    s1 = 0
    s2 = 0
    dv = 1
    dh = 1
    is_first_col = True
    col_min = 0
    row_min = 0

    while True:
        c1 = int(r.gettext())
        if dv == 1:
            r.dn()
        else:
            r.up()
        c2 = int(r.gettext())

        sc = c1 + c2

        if r.wr():
            if r.wd():
                break
            if dv == 1:
                r.dn()
            dh = 0

        if r.wl() and not is_first_col:
            if r.wd():
                break
            if dv == 1:
                r.dn()
            dh = 1

        if dv == 1:
            s1 = sc
            dv = 0
            if s > s1 + s2 and not is_first_col:
                s = s1 + s2
                col_min = r.getCoordC()
                row_min = r.getCoordR()
        else:
            s2 = sc
            dv = 1
            if s > s1 + s2:
                s = s1 + s2
                col_min = r.getCoordC()
                row_min = r.getCoordR()+1

        if dh == 1:
            r.rt()
        else:
            r.lt()

        is_first_col = False

    r.jumpTo((row_min,col_min))
    r.pt('red')
    r.lt()
    r.pt('red')
    r.up()
    r.pt('red')
    r.rt()
    r.pt('red')

r.start(task)
