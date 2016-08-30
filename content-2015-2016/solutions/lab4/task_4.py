import robot
r = robot.rmap()
r.lm('task4')


def change_direction(d):
    if d == 1:
        return -1
    else:
        return 1


def task():
    while not r.wl():
        r.lt()

    while not r.wu():
        r.up()

    d = 1
    while True:
        if r.label() == 'red':
            r.pt('red')

        if d == 1:
            if r.wr():
                if r.wd():
                    break
                d = change_direction(d)
                r.dn()
            else:
                r.rt()
        else:
            if r.wl():
                if r.wd():
                    break
                d = change_direction(d)
                r.dn()
            else:
                r.lt()

r.start(task)
