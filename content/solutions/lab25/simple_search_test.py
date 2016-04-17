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
        )
    }    
  
if __name__ == '__main__':
    unittest.main()
