import robot
r = robot.rmap()
r.lm('task2')


def vertical_move(rb, direction):
    if direction == 1:
        rb.dn()
    else:
        rb.up()


def get_direction(column):
    if column % 2 == 0:
        return -1
    else:
        return 1


def is_paint_cell(column, row):
    return ((column % 3 == 0 or column % 3 == 2) and row == 1) or \
           (column % 3 == 1 and (row == 0 or row == 2))


def is_cant_vertical_move(rb, direction):
    return (rb.wu() and direction == -1) or (rb.wd() and direction == 1)


def task():
    col = 0
    row = 2
    d = get_direction(col)

    while True:
        if is_paint_cell(col, row):
            r.pt('green')

        if is_cant_vertical_move(r, d):
            if r.wr():
                break
            r.rt()
            col += 1
            d = get_direction(col)
        else:
            vertical_move(r, d)
            row += d

r.start(task)
