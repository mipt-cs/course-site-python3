#!/usr/bin/env python3

from regexp_test import regexp_test, MATCH
import simple_match

import unittest

@regexp_test(simple_match)
class SimpleMatchTest(unittest.TestCase):
    TEST_DATA = {
        'REGEXP_1': (    # название тестируемого регулярного выражения
            MATCH,       # тип тестируемого метода — MATCH для этого файла
            ['a', 'ab'], # список строк, соответствующих шаблону
            ['b', 'ba']  # список строк, не соответствующих шаблону
        ),
        'REGEXP_2': (
            MATCH,
            ['aab', 'abb', 'acb'],
            ['ab', 'aabc']
        )
    }    
  
if __name__ == '__main__':
    unittest.main()
