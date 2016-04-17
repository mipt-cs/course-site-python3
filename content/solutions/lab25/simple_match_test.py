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
        ),
        'REGEXP_3': (
            MATCH,
            ['sofia.mp3', 'sofia.mp4'],
            ['sofia.mp7', 'sofia.mp34']
        ),
        'REGEXP_4': (
            MATCH,
            ['taverna', 'versus', 'vera', 'zveri'],
            ['zver']
        ),
        'REGEXP_5': (
            MATCH,
            ['aaa', 'bbb'],
            ['a', 'aa', 'aaaa', 'b', 'bb', 'bbbb']
        ),
        'REGEXP_6': (
            MATCH,
            ['OkOkOk', 'ababab'],
            ['Ok', 'OkOk', 'OkOkOkOk', 'ab', 'abab', 'abababab']
        ),
        'REGEXP_7': (
            MATCH,
            ['aaa Aaa aaa', 'aaa aaa Aaa', 'Aaa aaa aaa'],
            ['aaa', 'aaa aaa', 'A', 'aaa A aaa']
        ),
        'REGEXP_8': (
            MATCH,
            ['abc', 'abc03', 'a-b-c-3', 'a.b.c.0'],
            ['Aabc', 'abc1', '#abc']
        )
    }

if __name__ == '__main__':
    unittest.main()
