from string import punctuation

data = []
with open('/usr/share/licenses/python/LICENSE') as f:
    data = f.read()

data = ''.join((c if c not in punctuation else ' ') for c in data)

words = [w.lower() for w in data.split()]

d = {}
for w in words:
    if w in d:
        d[w] += 1
    else:
        d[w] = 1

rd = {v: i for i, v in d.items()}
for i in range(10):
    m = max(rd.keys())
    print(rd[m], m)
    del rd[m]
