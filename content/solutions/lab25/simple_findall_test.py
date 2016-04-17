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
        ),
        'REGEXP_2': (
            FINDALL,
            {
                'aaa bbb ccc': ['aaa', 'bbb', 'ccc'],
                'ddd eee fgh': ['ddd', 'eee', 'fgh'],
                'a1b c2d e3f': ['a1b', 'c2d', 'e3f']
            }
        ),
        'REGEXP_3': (
            FINDALL,
            {
                'a aa aaa':  ['aa', 'aaa'],
                'b bb bbb':  ['bb', 'bbb'],
                'a bb aaa':  ['bb', 'aaa']
            }
        ),
        'REGEXP_4': (
            FINDALL,
            {
                '1.1.1.1 aaaa bbbbb': ['1.1.1.1'],
                'a.a.a.a bbbb 2.2.2.2': ['2.2.2.2'],
                '3.3.3.3 cccc 4.4.4.4': ['3.3.3.3', '4.4.4.4'],
                '255.23.0.1 cccc 4.4.4.4': ['255.23.0.1', '4.4.4.4'],
                '255.0.23.1 cccc 4.4.4.4': ['255.0.23.1', '4.4.4.4']
            }
        ),
        'REGEXP_5': (
            FINDALL,
            {
                'aaa Abbb ccc': ['Abbb'],
                'Aaa Abbb ccc': ['Aaa', 'Abbb'],
                'Caa Cbb Accc': ['Accc']
            }
        ),
        'REGEXP_6': (
            FINDALL,
            {
                'a b c d e f': ['a', 'b', 'e', 'f'],
                'abcdef': ['a', 'b', 'e', 'f'],
                'adf': ['a', 'f'],
                'acf': ['a', 'f']
            }
        ),
        'REGEXP_7': (
            FINDALL,
            {
                'aaa +1.0 bb': ['+1.0'],
                'aaa -1.0 bb': ['-1.0'],
                'aaa -123.234 bb +111.999': ['-123.234', '+111.999']
            }
        ),
        'REGEXP_8': (
            FINDALL,
            {
                'aaa 18-04-2016 bbb': ['18-04-2016'],
                'aaa 18.04.2016 bbb': ['18.04.2016'],
                'aaa 18-04-ABCD bbb 18.04.2016': ['18.04.2016'],
                'aaa 18/04/ABCD bbb 18/04/2016': ['18/04/2016'],
                'aaa 18/04/ABCD bbb 18/4/2016 ': ['18/4/2016']
            }
        )
    }    
  
if __name__ == '__main__':
    unittest.main()
