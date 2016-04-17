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
        ),
        'REGEXP_2': (
            SUB,
            {
                'abcXYZabc': 'abcabc',
                'XaYbZcWaM': 'abca',
                'abc XYZabc':'abc abc'
            }
        ),
        'REGEXP_3': (
            SUB,
            {
                'abcABCabc': 'abcABCabc',
                'DaEbFcAaB': 'abcAaB',
                'abcXYZabc': 'abcXYZabc',
                'XaYbZcZaY': 'XaYbZcZaY',
                'DXEYFZabc': 'XYZabc',
                'ADBECFXYZ': 'ABCXYZ'
            }
        ),
        'REGEXP_4': (
            SUB,
            {
                'abc0abc': 'abcabc',
                '1a2b3c4': 'abc',
                'a123!@#bc': 'abc'
            }
        ),
        'REGEXP_5': (
            SUB,
            {
                'a,b,c d,e,f': 'a_b_c_d_e_f',
                'abc!@#a': 'abc___a',
                'abc!@#,./abc abc':  'abc______abc_abc'
            }
        ),
        'REGEXP_6': (
            SUB,
            {
                'a abc aa bb': 'a aa bb',
                'a def dd fd': 'a dd fd',
                'x xy xyz yz': 'x xy yz',
                'x xyz xyz yz': 'x yz',
            }
        ),
        'REGEXP_7': (
            SUB,
            {
                'AabcdZ': 'abcd',
                'BabcdC': 'BabcdC',
                'aAbZcd': 'aAbZcd',
                'AabcdY': 'abcdY',
                'BabcdZ': 'Babcd'
            }            
        ),
        'REGEXP_8': (
            SUB,
            {
                'a b c': 'a b c',
                'a  b c': 'a b c',
                'd    f': 'd f'
            }
        ),
        'REGEXP_9': (
            SUB,
            {
                'a ab abc abcd ab': 'a ab ab',
                'a xyz xyz a': 'a a',
                'd xy xyza a': 'd xy a',
                'a xyzzy b': 'a xyzzy b'
            }
        )
    }    
  
if __name__ == '__main__':
    unittest.main()
