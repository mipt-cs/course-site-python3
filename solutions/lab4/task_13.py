import robot
r = robot.rmap()
r.lm('task13')
r.sleep = 0.05


def task():
    d = 1
    s = 0
    l = 0

    while not r.wu():
        r.up()

    while True:
        if r.wd():
            d = 2
            if not r.wl():
                r.lt()
            else:
                break

        if r.wu():
            d = 1
            if not r.wl():
                r.lt()
            else:
                break

        if r.wl():
            s += 1
        elif s > 0:
            break

        if d == 1:
            r.dn()
        elif d == 2:
            r.up()
        else:
            break

    if s > 0:
        l = 1
        while not r.wr():
            l += 1
            r.rt()

    print( "Wall size = " + str(s))
    print( "Wall distance = " + str(l))

r.start(task)
