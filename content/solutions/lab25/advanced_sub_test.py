#!/usr/bin/env python3

from regexp_test import regexp_test, SUB
import advanced_sub

import unittest

@regexp_test(advanced_sub)
class AdvancedSubTest(unittest.TestCase):
    TEST_DATA = {
        'REGEXP_1': (         # название тестируемого регулярного выражения
            SUB,              # тип тестируемого метода — SUB для этого файла
            {                 # словарь с тестовыми данными вида (строка на входе => строка на выходе)
                'this is text':  'this is text',
                'this is is text':  'this !is! text',
                'this is is is text': 'this !is! text'

            }
        )
    }    
  
if __name__ == '__main__':
    unittest.main()
