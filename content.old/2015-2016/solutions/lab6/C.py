f = open('input.txt')

N = int(f.readline())
mind = N
A = list(map(int, f.readline().split()))

f.close()

for i in range(N):
    if A[i] < 0:
        for j in range(i + 1, N):
            if A[i] + A[j] == 0 and j - i < mind:
                mind = j - i

f = open('output.txt', 'w')
if mind == N:
    print(0, file=f)
else:
    print(mind, file=f)

f.close()
