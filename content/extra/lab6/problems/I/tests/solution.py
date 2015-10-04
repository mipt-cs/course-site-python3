n = int(input())

i = 2
while i * i <= n and n % i != 0:
    i += 1
if n % i == 0:
    print(i)
else:
    print(n)
