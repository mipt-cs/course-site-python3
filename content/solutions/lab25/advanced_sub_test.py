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
                'aAc': 'a!A!c',
                'aZc': 'a!Z!c',
                'aZZc': 'a!Z!!Z!c',
                'aBaCa': 'a!B!a!C!a'
            }
        ),
        'REGEXP_2': (
            SUB,
            {
                'abc': 'abc',
                'abbc': 'abc',
                'azzzc': 'azc',
                'arrrrc': 'arc',
                'xxxxxx': 'x'
            }
        ),
        'REGEXP_3': (
            SUB,
            {
                'this is text': 'this is text',
                'this is is text': 'this *is* text',
                'this is is is text': 'this *is* text',
                'this is text text': 'this is *text*',
                'this is is text text': 'this *is* *text*'
            }
        ),
        'REGEXP_4': (
            SUB,
            {
                'one two three': 'two one three',
                'dog cat wolf': 'cat dog wolf',
                'goose car rat': 'goose rat car'
            }
        ),
        'REGEXP_5': (
            SUB,
            {
                'cat dog': 'cat dog',
                'cat dog cat': 'cat dog cat',
                'dog cat dog cat cat': 'dog dog',
                'dog wolf dog rat rat wolf wolf': 'dog dog rat rat'
            }
        )
    }    
  
if __name__ == '__main__':
    unittest.main()
