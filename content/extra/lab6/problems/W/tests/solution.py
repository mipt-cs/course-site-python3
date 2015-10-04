def move(n, a, b):
    if n > 0:
        move(n - 1, a, 6 - a - b)
        print(n, a, b)
        move(n - 1, 6 - a - b, b)

def solve(n, a):
    if n > 0:
        if n % 2 == 0:
            b = 3
        else:
            b = 2
        if a == b:
            solve(n - 1, a)
        else:
            c = 6 - a - b
            move(n - 1, a, c)
            print(n, a, b)
            solve(n - 1, c)

solve(int(input()), 1)
