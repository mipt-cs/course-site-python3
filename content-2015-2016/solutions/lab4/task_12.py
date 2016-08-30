import robot
r = robot.rmap()
r.lm('task12')
r.sleep = 0.05


def task():
    d = 1
    while True:

        if r.wd() and not r.wu():
            if d == 2:
                d = 1
            elif d == 1:
                d = 4

        if r.wu():
            if r.wl():
                r.pt('red')
                d = 2
            elif r.wr():
                d = 1
                r.pt('red')

        if r.wl() and (not r.wu() and not r.wd()) and d == 1:
            break

        if d == 1:
            r.lt()
        elif d == 2:
            r.dn()
        elif d == 3:
            r.rt()
        elif d == 4:
            r.up()
        else:
            break

r.start(task)
