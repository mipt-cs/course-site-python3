def move(n, a, b):
    if n == 1:
        print(1, a, b)
    elif n > 1:
        c = 6 - a - b
        move(n - 1, a, b)
        move(n - 2, b, c)
        print(0, a, b)
        move(n - 2, c, a)
        move(n - 1, a, b)

move(int(input()), 1, 3)
