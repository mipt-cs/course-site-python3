from string import punctuation

d = {}
with open('en-ru.txt') as f:
    for line in f:
        key, value = line.strip().split('\t-\t')
        d[key] = value

with open('input.txt') as fi, open('output.txt', 'w') as fo:
    for line in fi:
        data = ''.join((c if c not in punctuation else " " + c + " ") for c in line)

        words = [(d[word] if word in d else word) for word in data.split()]
        for word in data.split():
            if word in d:
                with open('test.txt', 'a') as f:
                    print(word + '\t-\t' + d[word], file=f)

        for i in range(len(words)-1):
            print(words[i], file=fo, sep='', end='')
            if words[i+1][0] not in punctuation:
                print(' ', file=fo, sep='', end='')
        if len(words):
            print(words[-1], file=fo)
