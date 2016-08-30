#!/bin/env python3

import unittest
import lib
import math

class TestLib(unittest.TestCase):

    def test_sin(self):
        self.assertEqual(lib.sin(0.0), 0.0)
        self.assertAlmostEqual(lib.sin(math.pi), 0.0)
        self.assertAlmostEqual(lib.sin(-math.pi), 0.0)
        self.assertAlmostEqual(lib.sin(math.pi/2), 1.0)
        self.assertAlmostEqual(lib.sin(-math.pi/2), -1.0)

    def test_sin_error_1(self):
        self.assertAlmostEqual(lib.sin(5*math.pi/2), 1.0, msg='Функция работает некорректно для чисел не из диапазона[-2π,2π]')

    def test_factorial(self):
        self.assertEqual(lib.factorial(0), 1)
        self.assertEqual(lib.factorial(1), 1)
        self.assertEqual(lib.factorial(2), 2)
        self.assertEqual(lib.factorial(3), 6)
        self.assertEqual(lib.factorial(4), 24)
        self.assertEqual(lib.factorial(5), 120)

    def test_factorial_error_1(self):
        self.assertEqual(lib.factorial(-1), 1, 'Неверно вычисляет факториал отрицательного числа')

    def test_factorial_error_2(self):
        self.assertEqual(type(lib.factorial(5)), int, 'Функция возвращает не int')

    def test_even(self):
        self.assertEqual(lib.even(1), False)
        self.assertEqual(lib.even(2), True)

    def test_even_error_1(self):
        self.assertEqual(lib.even(0), True, 'Функция неверно работает для 0')

    def test_even_error_2(self):
        self.assertEqual(lib.even(-2), True, 'Функция неверно работает для отрицательных чисел')

    def test_palindrome(self):
        self.assertEqual(lib.palindrome('abc'), False)
        self.assertEqual(lib.palindrome('abccba'), True)
        self.assertEqual(lib.palindrome('abdceba'), False)

    def test_palindrome_error_1(self):
        self.assertEqual(lib.palindrome('abcba'), True, 'Функция неверно работает для строк нечётной длины')

    def test_prime(self):
        self.assertEqual(lib.prime(2), True)
        self.assertEqual(lib.prime(3), True)
        self.assertEqual(lib.prime(4), False)
        self.assertEqual(lib.prime(5), True)

    def test_prime_error1(self):
        self.assertEqual(lib.prime(0), False, '0 не является простым числом')

    def test_prime_error2(self):
        self.assertEqual(lib.prime(1), False, '1 не является простым числом')

    def test_prime_error3(self):
        self.assertEqual(lib.prime(-9), False, 'Отрицательное число не является простым')

unittest.main(verbosity=2)