def move(n, a, b):
    if n == 1:
        print(n, a, b)
    else:
        move(n - 1, a, b)
        print(n, a, 2)
        move(n - 1, b, a)
        print(n, 2, b)
        move(n - 1, a, b)

move(int(input()), 1, 3)
