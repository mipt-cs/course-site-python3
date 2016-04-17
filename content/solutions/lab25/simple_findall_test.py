#!/usr/bin/env python3

from regexp_test import regexp_test, FINDALL
import simple_findall

import unittest

@regexp_test(simple_findall)
class SimpleFindallTest(unittest.TestCase):
    TEST_DATA = {
        'REGEXP_1': (       # название тестируемого регулярного выражения
            FINDALL,        # тип тестируемого метода — FINDALL для этого файла
            {               # словарь с тестовыми данными вида (строка на входе => найденные подстроки)
                '1 a 1 2 b': ['a', 'b'],
                'z 2 y': ['z', 'y']
            }
        )
    }    
  
if __name__ == '__main__':
    unittest.main()
