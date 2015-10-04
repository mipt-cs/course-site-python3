n = int(input())

i = 2
while i * i <= n and n % i != 0:
    i += 1
if i * i > n:
    print("YES")
else:
    print("NO")
