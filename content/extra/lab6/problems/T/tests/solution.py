def move(n, a, b):
    if n > 0:
        c = 6 - a - b
        if c == 2:
            move(n - 1, a, b)
            print(n, a, c)
            move(n - 1, b, a)
            print(n, c, b)
            move(n - 1, a, b)
        else:
            move(n - 1, a, c)
            print(n, a, b)
            move(n - 1, c, b)

move(int(input()), 1, 3)
