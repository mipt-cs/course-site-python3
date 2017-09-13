f = open('input.txt')

f.readline()
A = list(map(int, f.readline().split()))
f.close()

A.sort()
i = 1
while A[i] != A[i - 1]:
    i += 1


f = open('output.txt', 'w')
print(A[i], file=f)
f.close()
