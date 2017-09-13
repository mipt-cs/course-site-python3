from random import randrange
from random import choice

nk = list(map(int, input().split()))
N, K = nk[0], nk[1]
keys = []
neighs = []
key_store = [None] * N

for i in range(N):
    # Зададим ключ для квартиры
    keys.append(randrange(N//4+1))

    # Зададим количество соседей у которых есть ключ
    n_neigh = randrange(1, K+1)

    # Сгенерим номера соседей
    neighs.append([])
    for j in range(n_neigh):
        neighs[i].append(randrange(N))

    # Дадим соседям ключи
    for j in range(n_neigh):
        if not key_store[neighs[i][j]]:
            key_store[neighs[i][j]] = []
        key_store[neighs[i][j]].append([i, keys[i]])

# Выберем квартиру Фёдора
N0 = randrange(N)
# Найдем всех соседей от которых можно придти в квартиру Фёдора
old = set()
new = {N0}
while len(new):
    i = new.pop()
    old.add(i)
    for j in range(len(neighs[i])):
        if neighs[i][j] not in old:
            new.add(neighs[i][j])
# Выберем одного
M0 = choice(list(old))

print('#########')
print('Ответ:', keys[N0])
print('#########')

f = open('input.txt', 'w')
print("N =", N0, "M =", M0, "K =", keys[M0])
print(N0, M0, keys[M0], file = f)
for i in range(N):
    if not key_store[i]:
        key_store[i] = []

    print(str(i) + ' : ', end = '')

    for j in range(len(key_store[i])):
        # "Запрем" дверь
        key_store[i][j][0] += keys[i]

        end = ','
        if j == len(key_store[i]) - 1:
            end = ''
        print(key_store[i][j][0], key_store[i][j][1], end = end)
        print(key_store[i][j][0], key_store[i][j][1], end = end, file = f)
    print()
    print(file = f)
