def convert(fi, fo):
    d = {}
    with open(fi) as f:
        for line in f:
            words = line.strip().split('\t-\t')
            if words[0] not in d:
                d[words[0]]=set()
            d[words[0]].add(words[1])
    with open(fo, 'w') as f:
        for k in d:
            print(k,','.join(d[k]), sep='\t-\t', file=f)

convert('input.txt', 'en-ru.txt')
convert('output.txt', 'ru-en.txt')
