#!/usr/bin/env python3

import sys
import os


def tree(path, level=0):
    name = os.path.basename(path) if level > 0 else os.path.realpath(path)
    print('   '*level, name, sep='')
    for c in sorted(os.listdir(path)):
        full_path = os.path.join(path, c)
        if os.path.isfile(full_path):
            print('   '*(level+1), c, sep='')
        else:
            tree(full_path, level+1)


def pretty_tree(path, indices=[]):

    def print_prefix(indices):
        for x in indices:
            print('│   ' if x != -1 else '    ', end='')

    level = len(indices)
    name = os.path.basename(path) if level > 0 else os.path.realpath(path)
    print_prefix(indices[:-1])
    if level > 0:
        print('├── ' if indices[-1] != -1 else '└── ', end='')
    print(name, sep='')
    children = sorted(os.listdir(path))
    for i, c in enumerate(children):
        if i == len(children)-1:
            idx = -1
        elif i == 0:
            idx = 1
        else:
            idx = 0

        full_path = os.path.join(path, c)
        if os.path.isfile(full_path):
            print_prefix(indices)
            print('├── ' if idx != -1 else '└── ', c, sep='')
        else:
            pretty_tree(full_path, indices + [idx])


if len(sys.argv) != 2:
    print('Эта программа ожидает ровно один параметр')
    sys.exit(-1)

if not os.path.isdir(sys.argv[1]):
    print("Указанный путь не существует или не является папкой")
    sys.exit(-1)

pretty_tree(sys.argv[1])