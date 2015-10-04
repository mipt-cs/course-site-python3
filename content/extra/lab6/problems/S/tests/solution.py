def move(n, a, b):
    if n > 0:
        move(n - 1, a, 6 - a - b)
        print(n, a, b)
        move(n - 1, 6 - a - b, b)

move(int(input()), 1, 3)
