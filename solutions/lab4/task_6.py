import robot
r = robot.rmap()
r.lm('task6')
r.sleep = 0.01


def task():
    w = int(input("Enter letter width: "))
    h = int(input("Enter letter height: "))
    x = 0
    y = 0

    while x < w:
        r.pt('red')
        x += 1
        if r.wr():
            break
        elif x < w:
            r.rt()

    rem = x % 2
    mid = x // 2

    while x > mid + rem:
        r.lt()
        x -= 1

    while y < h:
        r.pt('red')
        y += 1
        if r.wd():
            break
        elif y < h:
            r.dn()

    if rem == 0:
        r.rt()
        while y > 1:
            r.pt('red')
            r.up()
            y -= 1

r.start(task)
