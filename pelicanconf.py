#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Alexey Ermakov'
SITENAME = 'Курс информатики на Python 3'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Moscow'

DEFAULT_LANG = 'ru'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

MENUITEMS = (('Главная', '/'),)

# Blogroll
# LINKS = (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)

# Social widget
# SOCIAL = (('You can add links in your config file', '#'),
#           ('Another social link', '#'),)

DEFAULT_PAGINATION = False
FILENAME_METADATA = '(?P<slug>.*)'
ARTICLE_URL = 'labs/{slug}.html'
ARTICLE_SAVE_AS = ARTICLE_URL


# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = 'themes/the-theme'

ARTICLE_ORDER_BY = 'date'
DISPLAY_CATEGORIES_ON_MENU = False

PLUGIN_PATHS = ['plugins']
PLUGINS = ['extract_toc', 'code_include']

STATIC_PATHS = [
    'images',
    'code',
    'extra/favicon.png',
    'extra/lab6/lib.m.html',
    'extra/lab6/lib.py',
    'extra/lab6/tests.tgz',
    'extra/checker.py'
]

EXTRA_PATH_METADATA = {
    'extra/favicon.png': {'path': 'favicon.png'},
    'extra/lab6/lib.m.html': {'path': 'extra/lab6/lib.m.html'},
    'extra/lab6/lib.py': {'path': 'extra/lab6/lib.py'},
    'extra/checker.py': {'path': 'extra/checker.py'},
    'extra/lab6/tests.tgz': {'path': 'extra/lab6/tests.tgz'}
}

READERS = {'html': None}
