#!/bin/env python3

import array
import pickle
import os
import sys
import wiki_stats

wg = wiki_stats.WikiGraph()
wg.load_from_file(sys.argv[1])

_id = wg.get_id('Python')

if os.path.isfile('links_to'):
    with open('links_to', 'rb') as f:
        links_to = pickle.load(f)
else:
    links_to = [[] for i in range(wg.get_number_of_pages())]
    for i in range(wg.get_number_of_pages()):
        for l in wg.get_links_from(i):
            links_to[l].append(i)
    with open('links_to', 'wb') as f:
        pickle.dump(links_to, f)

N = 1000
vertices = set()
vertices.add(_id)

queue = list()

queue.append(_id)

while N > 0:
    _id = queue.pop()

    edges =  list(wg.get_links_from(_id)) + links_to[_id]

    for vert in edges:
        if not vert in vertices:
            vertices.add(vert)
            queue.insert(0, vert)
            N -= 1

edges = { v:[] for v in vertices }

for v in vertices:
    for _id in wg.get_links_from(v):
        if _id in vertices:
            edges[v].append(_id)

vertices = [v for v in vertices if not wg.is_redirect(v) or edges.get(v, [])]

for (k, v) in edges.items():
    edges[k] = [x for x in v if x in vertices]

indexes = { idx:_id for (idx, _id) in enumerate(vertices) }
indexes_rev = { v:k for (k,v) in indexes.items() }

with open('wiki_small.txt', 'w') as f:
    f.write('%d %d\n' % (len(vertices), sum(map(len, edges.values()))))
    for i in range(len(vertices)):
        _id = indexes[i]
        f.write(wg.get_title(_id) + '\n')
        f.write('%d %d %d\n' % (wg.get_page_size(_id), wg.is_redirect(_id), len(edges[_id])))
        for v in edges[_id]:
            f.write('%d\n' % indexes_rev[v])
