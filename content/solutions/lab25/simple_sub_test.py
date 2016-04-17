#!/usr/bin/env python3

from regexp_test import regexp_test, SUB
import simple_sub

import unittest

@regexp_test(simple_sub)
class SimpleSubTest(unittest.TestCase):
    TEST_DATA = {
        'REGEXP_1': (         # название тестируемого регулярного выражения
            SUB,              # тип тестируемого метода — SUB для этого файла
            {                 # словарь с тестовыми данными вида (строка на входе => строка на выходе)
                'bab': 'bzb', 
                'bcb': 'bzb',
                'bxb': 'bzb'
            }
        )
    }    
  
if __name__ == '__main__':
    unittest.main()
