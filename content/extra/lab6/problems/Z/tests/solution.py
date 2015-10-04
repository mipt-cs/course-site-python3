def f(n):
    if n <= 1:
        return 0
    m = n
    for i in range(1, n):
        m = min(m, 1 + max(i-1, f(n - i)))
    return m

n = int(input())
print(f(n))

