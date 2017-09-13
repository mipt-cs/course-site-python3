#!/usr/bin/env python3

from regexp_test import regexp_test, SEARCH
import simple_search

import unittest

@regexp_test(simple_search)
class SimpleSearchTest(unittest.TestCase):
    TEST_DATA = {
        'REGEXP_1': (       # название тестируемого регулярного выражения
            SEARCH,         # тип тестируемого метода — SEARCH для этого файла
            {               # словарь с тестовыми данными вида (строка на входе => найденная подстрока)
                'bab': 'a', 
                'bcb': 'c',
                'bxb': 'x'
            }
        ),
        'REGEXP_2': (
            SEARCH,
            {
                'ooooAAAooooo': 'AAA',
                'asdfasdAAAAfasdf': 'AAAA',
                'AAAAAAfasdf': 'AAAAAA',
                'iiiiiA': 'A'
            }
        ),
        'REGEXP_3': (
            SEARCH,
            {
                'There is <html> tag': '<html>',
                "color can be used as <font color='red'>": "<font color='red'>",
                "There is x <> 10 and something was wrong with < or > brace.": '< or >'
            }
        ),
        'REGEXP_4': (
            SEARCH,
            {
                'C@n Y0u f1nd CaPoAira?': 'CaPoAira',
                's0 Wh@t i5 CamelStyle?': 'CamelStyle',
                'Any simple word should match.': 'Any',
                'I like regular expressions': 'like'
            }
        ),
        'REGEXP_5': (
            SEARCH,
            {
                'all those that were numbered of the camps throughout their hosts were 603550.': '603550',
                'What is the meaning of life, the universe and everything? *42* Douglas Adams': '42',
                'Clive Staples Lewis was born in Belfast, Ireland, on 29 November 1898.': '29'
                }
            ),
        'REGEXP_6': (
            SEARCH,
            {
                'New York: W. H. Freeman, pp. 347-353, 1991.': 'Freeman',
                'set out to travel much faster than light': 'travel',
                'Arise ye, and depart; for this is not your rest...': 'depart',
            }
        ),
        'REGEXP_7': (
            SEARCH,
            {
                'I know that cat can catch a mouse!': 'cat can catch a mouse',
                'But this mouse is faster than the cat.': 'mouse is faster than the cat',
                'Mouse Mickey is not a simple mouse. Tom is a dummy cat.': 'mouse. Tom is a dummy cat'
            }
        ),
        'REGEXP_8': (
            SEARCH,
            {
                'his phone number was 89251366482.': '89251366482',
                'I called +7 999 648-99-86 ans it was right.': '+7 999 648-99-86',
                'Some 52221 numbers should not hide phone numbers such as 8 915 747-68-99': '8 915 747-68-99',
            }
        )
    }    
  
if __name__ == '__main__':
    unittest.main()
