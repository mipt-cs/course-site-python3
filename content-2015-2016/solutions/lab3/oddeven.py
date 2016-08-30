n = int(input())

for i in range(1, n):
    if i % 2 == 0:
        s = 'even'
    else:
        s = 'odd'
    print(i, s, sep=' ')