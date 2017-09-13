#!/usr/bin/env python3

import sys
import os

if len(sys.argv) == 1:
    print('Укажите хотя бы один файл')
    sys.exit(-1)

for fname in sys.argv[1:]:
    if not os.path.isfile(fname):
        print('%s не является файлом, пропускаю' % fname, file=sys.stderr)
        continue

    with open(fname) as f:
        print(f.read())