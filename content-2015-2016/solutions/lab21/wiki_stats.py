#!/usr/bin/python3

import os
import sys
import math

import array

import statistics

from matplotlib import rc
rc('font', family='Droid Sans', weight='normal', size=14)

import matplotlib.pyplot as plt


class WikiGraph:

    def load_from_file(self, filename):
        print('Загружаю граф из файла: ' + filename)

        with open(filename) as f:
            (n, _nlinks) = map(int, f.readline().split())
            self._titles = []

            self._sizes = array.array('L', [0]*n)
            self._links = array.array('L', [0]*_nlinks)
            self._redirect = array.array('B', [0]*n)
            self._offset = array.array('L', [0]*(n+1))
            l = 0

            for i in range(n):
                title = f.readline().strip()
                (sz, rdrct, numlinks) = map(int, f.readline().split())

                self._titles.append(title)
                self._sizes[i] = sz
                self._redirect[i] = rdrct

                self._offset[i] = l
                for j in range(numlinks):
                    self._links[l] = int(f.readline())
                    l += 1

            self._offset[n] = l

        print('Граф загружен')

    def get_number_of_links_from(self, _id):
        return self._offset[_id+1]-self._offset[_id]

    def get_links_from(self, _id):
        return self._links[self._offset[_id]:self._offset[_id+1]]

    def get_id(self, title):
        return self._titles.index(title)

    def get_number_of_pages(self):
        return len(self._titles)

    def is_redirect(self, _id):
        return self._redirect[_id]

    def get_title(self, _id):
        return self._titles[_id]

    def get_page_size(self, _id):
        return self._sizes[_id]


def hist(fname, data, bins, xlabel, ylabel, title, facecolor='green', alpha=0.5, transparent=True, **kwargs):
    plt.clf()
    plt.hist(data, bins, facecolor=facecolor, alpha=alpha, **kwargs)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.grid(True)
    plt.savefig(fname, transparent=transparent)


if __name__ == '__main__':

    if len(sys.argv) != 2:
        print('Использование: wiki_stats.py <файл с графом статей>')
        sys.exit(-1)

    if os.path.isfile(sys.argv[1]):
        wg = WikiGraph()
        wg.load_from_file(sys.argv[1])
    else:
        print('Файл с графом не найден')
        sys.exit(-1)

    redirect_count = sum(wg.is_redirect(idx) for idx in range(wg.get_number_of_pages()))
    print("Количество статей с перенаправлением: %d (%0.2f%%)" % (redirect_count, 100*redirect_count/wg.get_number_of_pages()))
    
    numlinks = [wg.get_number_of_links_from(idx) for idx in range(wg.get_number_of_pages()) if not wg.is_redirect(idx)]
    _min = min(numlinks)
    _max = max(numlinks)
    print("Минимальное количество ссылок из статьи: %d" % _min)
    print("Количество статей с минимальным количеством ссылок: %d" % sum(n == _min for n in numlinks))
    print("Максимальное количество ссылок из статьи: %d" % _max)
    print("Количество статей с максимальным количеством ссылок: %d" % sum(n == _max for n in numlinks))
    for i in range(wg.get_number_of_pages()):
        if wg.get_number_of_links_from(i) == _max:
            print("Статья с наибольшим количеством ссылок: " + wg.get_title(i))
            break
    print("Среднее количество ссылок в статье: %0.2f (ср. откл. %0.2f)" % (statistics.mean(numlinks), statistics.stdev(numlinks)))
    
    hist('links_from.png', numlinks, 100, "Количество статей", "Количество ссылок", "Распределение количества ссылок из статьи", range=(0, 200))
    numlinks = None
    
    links_to = array.array('I', [0]*wg.get_number_of_pages())
    for i in range(wg.get_number_of_pages()):
        if not wg.is_redirect(i):
            for l in wg.get_links_from(i):
                links_to[l] += 1


    _min = min(links_to)
    _max = max(links_to)
    print("Минимальное количество ссылок на статью: %d" % _min)
    print("Количество статей с минимальным количеством внешних ссылок: %d" % sum(n == _min for n in links_to))
    print("Максимальное количество ссылок на статью: %d" % _max)
    print("Количество статей с максимальным количеством внешних ссылок: %d" % sum(n == _max for n in links_to))
    for i in range(len(links_to)):
        if links_to[i] == _max and not wg.is_redirect(i):
            print("Статья с наибольшим количеством внешних ссылок: " + wg.get_title(i))
            break
    print("Среднее количество внешних ссылок на статью: %0.2f (ср. откл. %0.2f)" % (statistics.mean(links_to), statistics.stdev(links_to)))
    
    hist('links_to.png', links_to, 100, "Количество статей", "Количество ссылок", "Распределение количества ссылок на статью", range=(0, 200))
    links_to = None
    finks_to = None
    
    redirects_to = array.array('I', [0]*wg.get_number_of_pages())
    for i in range(wg.get_number_of_pages()):
        if wg.is_redirect(i):
            if wg.get_links_from(i):
                redirects_to[wg.get_links_from(i)[0]] += 1
    
    _min = min(redirects_to)
    _max = max(redirects_to)
    print("Минимальное количество перенаправлений на статью: %d" % _min)
    print("Количество статей с минимальным количеством внешних перенаправлений: %d" % sum(n == _min for n in redirects_to))
    print("Максимальное количество перенаправлений на статью: %d" % _max)
    print("Количество статей с максимальным количеством внешних перенаправлений: %d" % sum(n == _max for n in redirects_to))
    for i in range(len(redirects_to)):
        if redirects_to[i] == _max:
            print("Статья с наибольшим количеством внешних перенаправлений: " + wg.get_title(i))
            break
    print("Среднее количество внешних перенаправлений на статью: %0.2f (ср. откл. %0.2f)" % (statistics.mean(redirects_to), statistics.stdev(redirects_to)))
    
    hist('redirects.png', redirects_to, 20, "Количество статей", "Количество ссылок", "Распределение количества перенаправлений на статью", range=(0, 20))
    redirects_to = None
    
    sizes = [wg.get_page_size(i) for i in range(wg.get_number_of_pages()) if not wg.is_redirect(i)]
    hist('sizes.png', sizes, 100, "Размер статьи", "Количество статей", "Распределение размеров статей", range=(0, 100000))
    hist('sizes_log.png', [math.log(s, 10) for s in sizes], 25, "Размер статьи", "Количество статей", "Распределение размеров статей (в логарифмическом масштабе)", range=(0, 6))
    sizes = None

    queue = array.array('I', [0]*wg.get_number_of_pages())
    prev = array.array('i', [-1]*wg.get_number_of_pages())
    dist = array.array('i', [-1]*wg.get_number_of_pages())

    first = 0
    last = 1

    _from = 'Python'
    _to = 'Боль'

    print('Запускаем поиск в ширину')

    queue[0] = wg.get_id(_from)
    prev[queue[0]] = -1
    dist[queue[0]] = 0

    while first < last:
        for l in wg.get_links_from(queue[first]):
            if dist[l] == -1:
                dist[l] = dist[first] + 1
                prev[l] = queue[first]
                queue[last] = l
                last += 1
        first += 1

    idx = wg.get_id(_to)
    path = []
    while idx != -1:
        path.append(wg.get_title(idx))
        idx = prev[idx]

    print('Поиск закончен. Найден путь:')

    for p in path[::-1]:
        print(p)
