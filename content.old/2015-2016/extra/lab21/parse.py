#!/usr/bin/python

import pickle

def parse_string(s):

    i = s.index('(')+1
    while True:
        res = []
        while True:
            if s[i] == ',':
                i += 1
            elif s[i] == ')':
                i += 1
                break
            elif s[i] == 'N':
                res.append(None)
                i += 4
            elif s[i] == "'":
                j= i = i + 1
                while True:
                    if s[j] == "'":
                        break
                    if s[j] == "\\":
                        j += 1
                    j += 1
                res.append(s[i:j])
                i = j + 1
            else:
                j = i+1
                while True:
                    if s[j] in [')', ',']:
                        x = s[i:j]
                        if x.count('.') != 0:
                            res.append(float(x))
                        else:
                            res.append(int(x))
                        break
                    j += 1
                i = j

        yield res

        if s[i] == ',':
            i += 2
        elif s[i] == ';':
            break


# CREATE TABLE `page` (
#   `page_id` int(8) unsigned NOT NULL AUTO_INCREMENT,
#   `page_namespace` int(11) NOT NULL DEFAULT '0',
#   `page_title` varbinary(255) NOT NULL DEFAULT '',
#   `page_restrictions` varbinary(255) NOT NULL DEFAULT '',
#   `page_counter` bigint(20) unsigned NOT NULL DEFAULT '0',
#   `page_is_redirect` tinyint(1) unsigned NOT NULL DEFAULT '0',
#   `page_is_new` tinyint(1) unsigned NOT NULL DEFAULT '0',
#   `page_random` double unsigned NOT NULL DEFAULT '0',
#   `page_touched` varbinary(14) NOT NULL DEFAULT '',
#   `page_links_updated` varbinary(14) DEFAULT NULL,
#   `page_latest` int(8) unsigned NOT NULL DEFAULT '0',
#   `page_len` int(8) unsigned NOT NULL DEFAULT '0',
#   `page_no_title_convert` tinyint(1) NOT NULL DEFAULT '0',
#   `page_content_model` varbinary(32) DEFAULT NULL,
#   PRIMARY KEY (`page_id`),
#   UNIQUE KEY `name_title` (`page_namespace`,`page_title`),
#   KEY `page_random` (`page_random`),
#   KEY `page_len` (`page_len`),
#   KEY `page_redirect_namespace_len` (`page_is_redirect`,`page_namespace`,`page_len`)
# ) ENGINE=InnoDB AUTO_INCREMENT=6180386 DEFAULT CHARSET=binary;
# /*!40101 SET character_set_client = @saved_cs_client */;

# CREATE TABLE `pagelinks` (
#   `pl_from` int(8) unsigned NOT NULL DEFAULT '0',
#   `pl_namespace` int(11) NOT NULL DEFAULT '0',
#   `pl_title` varbinary(255) NOT NULL DEFAULT '',
#   `pl_from_namespace` int(11) NOT NULL DEFAULT '0',
#   UNIQUE KEY `pl_from` (`pl_from`,`pl_namespace`,`pl_title`),
#   KEY `pl_namespace` (`pl_namespace`,`pl_title`,`pl_from`),
#   KEY `pl_backlinks_namespace` (`pl_from_namespace`,`pl_namespace`,`pl_title`,`pl_from`)
# ) ENGINE=InnoDB DEFAULT CHARSET=binary;



title_map = {}
ids_map = {}
titles = []
sizes = []
raw_links = {}
redirect = []

def parse():

    with open('page.sql') as f:
        i = 0
        while True:
            s = f.readline()
            i += 1
            print('PAGE:', i)
            if not s:
                break
            if not s.startswith('INSERT'):
                continue
            else:
                for (_id, namespace, title, _, _, is_redirect, _, _, _, _, _, size, _, _) in parse_string(s):
                    if namespace != 0:
                        continue
                    ids_map[_id] = len(titles)
                    title_map[title] = len(titles)
                    redirect.append(is_redirect == 1)
                    titles.append(title)
                    sizes.append(size)

    with open('pagelinks.sql') as f:
        i = 0
        while True:
            s = f.readline()
            i += 1
            print('RAW LINKS:', i)
            if not s:
                break
            if not s.startswith('INSERT'):
                continue
            else:
                for (_from, namespace, title, from_namespace) in parse_string(s):
                    if namespace == 0 and from_namespace == 0 and title in title_map and _from in ids_map:
                        _id = ids_map[_from]
                        if not _id in raw_links:
                            raw_links[_id] = []
                        raw_links[_id].append(title_map[title])

def dump():
    with open('wiki', 'wb') as f:
        pickle.dump(title_map, f)
        pickle.dump(ids_map, f)
        pickle.dump(titles, f)
        pickle.dump(sizes, f)
        pickle.dump(raw_links, f)
        pickle.dump(redirect, f)

def load():
    global title_map
    global ids_map
    global titles
    global sizes
    global raw_links
    global redirect
    
    with open('wiki', 'rb') as f:
        title_map = pickle.load(f)
        ids_map = pickle.load(f)
        titles = pickle.load(f)
        sizes = pickle.load(f)
        raw_links = pickle.load(f)
        redirect = pickle.load(f)

#parse()
load()
print('loaded')
dump()

removed = [False]*len(titles)
cnt = 0

flag = True
while flag:
    flag = False
    for i in range(len(titles)):
        if not removed[i] and redirect[i] and not raw_links.get(i, []):
            removed[i] = True
            flag = True
            cnt += 1

    for (k, v) in raw_links.items():
        if not removed[k]:
            raw_links[k] = [x for x in v if not removed[x]]

print('Removed: %d' % cnt)

n = 0
new_idx = [0]*len(titles)
for i in range(len(titles)):
    new_idx[i] = n
    if not removed[i]:
        n += 1

nlinks = 0
for x in raw_links.values():
    nlinks += len(x)

with open('wiki.txt', 'w') as f:
    f.write('%d %d\n' % (len(titles)-cnt, nlinks))
    for (_id, t) in enumerate(titles):
        if not removed[_id]:
            lnks =  raw_links.get(_id, [])
            f.write(t + '\n')
            f.write('%d %d %s\n' % (sizes[_id], redirect[_id], len(lnks)))
            for l in lnks:
                f.write(str(new_idx[l])+ '\n')
