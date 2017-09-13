from matrix import Matrix
from unittest import TestCase, main


class SimpleTests(TestCase):
    def testMatrixConstructWithoutInitialization(self):
        """Создание матрицы без инициализации"""

        # тестирум возможность создания матриц разных размеров
        # для каждой матрицы проверяем, что по-умолчанию она заполнена нулями
        dims = [(2, 2), (3, 4), (4, 3)]

        for (m, n) in dims:
            a = Matrix(m, n)

            self.assertEqual(a.get_m(), m)
            self.assertEqual(a.get_n(), n)
            self.assertEqual(a.get_size(), (m, n))

            for i in range(m):
                for j in range(n):
                    self.assertEqual(a.get(i, j), 0)

    def testMatrixConstructWithInvalidArguments(self):
        """Создание матрицы с неправильными аргументами"""

        # передаём неверные аргументы и проверяем, что генерируется исключение
        with self.assertRaises(ValueError):
            Matrix(0, 1)

        with self.assertRaises(ValueError):
            Matrix(1, 0)

        with self.assertRaises(ValueError):
            Matrix(-1, 1)

        with self.assertRaises(ValueError):
            Matrix(1, -1)

        with self.assertRaises(ValueError):
            Matrix(1.0, 1)

        with self.assertRaises(ValueError):
            Matrix(1, 1.0)

    def testMatrixSet(self):
        """Изменение значений матрицы"""

        # тестируем механизм изменения значений элементов матрицы
        m = Matrix(1, 2)

        m.set(0, 0, 1)
        m.set(0, 1, 2)

        self.assertEqual(m.get(0, 0), 1)
        self.assertEqual(m.get(0, 1), 2)

    def testMatrixCompare(self):
        """Сравнение матриц"""

        # создаём две одинаковые матрицы и сравниваем их между собой
        m1 = Matrix(1, 2)
        m2 = Matrix(1, 2)

        self.assertEqual(m1, m2)

        # меняем значение одного элемента второй матрицы и снова сравниваем
        # матрицы между собой
        m2.set(0, 0, 1)

        self.assertNotEqual(m1, m2)

    def testMatrixAdd(self):
        """Сложение матриц"""

        # складываем две матрицы и проверяем результат
        a = Matrix(3, 2)

        a.set(0, 0, -1)
        a.set(0, 1, -2)
        a.set(1, 0, -3)
        a.set(1, 1, -4)
        a.set(2, 0, -5)
        a.set(2, 1, -6)

        b = Matrix(3, 2)

        b.set(0, 0, 1)
        b.set(0, 1, 2)
        b.set(1, 0, 3)
        b.set(1, 1, 4)
        b.set(2, 0, 5)
        b.set(2, 1, 6)

        _c = Matrix(3, 2)

        c = a + b

        self.assertEqual(c, _c)

    def testMatrixSub(self):
        """Вычитание матриц"""

        # вычитаем две матрицы и проверяем результат
        a = Matrix(3, 2)

        a.set(0, 0, 1)
        a.set(0, 1, 2)
        a.set(1, 0, 3)
        a.set(1, 1, 4)
        a.set(2, 0, 5)
        a.set(2, 1, 6)

        b = Matrix(3, 2)

        b.set(0, 0, 1)
        b.set(0, 1, 2)
        b.set(1, 0, 3)
        b.set(1, 1, 4)
        b.set(2, 0, 5)
        b.set(2, 1, 6)

        _c = Matrix(3, 2)

        c = a - b

        self.assertTrue(c, _c)

    def testMatrixScalarMul(self):
        """Умножение матрицы на число"""

        # умножаем матрицу на число и проверяем результат
        _a = Matrix(3, 2)
        _a.set(0, 0, 1)
        _a.set(0, 1, 2)
        _a.set(1, 0, 3)
        _a.set(1, 1, 4)
        _a.set(2, 0, 5)
        _a.set(2, 1, 6)

        a = _a * 2

        b = a * 2

        self.assertEqual(b, a + a)

        b = a * 1.5

        self.assertEqual(b, _a + _a + _a)

    def testMatrixScalarDiv(self):
        """Деление матрицы на число"""

        # делим матрицу на число и проверяем результат
        a = Matrix(3, 2)
        a.set(0, 0, 1)
        a.set(0, 1, 2)
        a.set(1, 0, 3)
        a.set(1, 1, 4)
        a.set(2, 0, 5)
        a.set(2, 1, 6)

        b = a * 2

        self.assertEqual(b / 2, a)

        b = a * 3

        self.assertEqual(b / 1.5, a + a)

    def testTranspose(self):
        """Траспонирование матрицы"""

        # выполняем транспонирование матрицы и проверяем результат
        a = Matrix(3, 2)
        a.set(0, 0, 1)
        a.set(0, 1, 2)
        a.set(1, 0, 3)
        a.set(1, 1, 4)
        a.set(2, 0, 5)
        a.set(2, 1, 6)

        b = Matrix(2, 3)
        b.set(0, 0, 1)
        b.set(1, 0, 2)
        b.set(0, 1, 3)
        b.set(1, 1, 4)
        b.set(0, 2, 5)
        b.set(1, 2, 6)

        self.assertEqual(a.transpose(), b)

    def testMatrixMul(self):
        """Матричное умножение"""

        # выполняем матричное умножение и проверяем результат
        a = Matrix(2, 3)
        a.set(0, 0, 1)
        a.set(0, 1, 2)
        a.set(0, 2, 3)
        a.set(1, 0, 4)
        a.set(1, 1, 5)
        a.set(1, 2, 6)

        b = Matrix(3, 2)
        b.set(0, 0, 9)
        b.set(0, 1, 8)
        b.set(1, 0, 7)
        b.set(1, 1, 6)
        b.set(2, 0, 5)
        b.set(2, 1, 4)

        c = Matrix(2, 2)
        c.set(0, 0, 38)
        c.set(0, 1, 32)
        c.set(1, 0, 101)
        c.set(1, 1, 86)

        self.assertEqual(a * b, c)

    def testMatrixMulWithWrongSizes(self):
        """Матричное умножение матриц с неправильными размерами"""

        # выполняем некорректное матричное умножением и проверяем,
        # что генерируется исключение

        with self.assertRaises(RuntimeError):
            Matrix(1, 2) * Matrix(1, 2)

        with self.assertRaises(RuntimeError):
            Matrix(2, 2) * Matrix(1, 2)


class NotSoSimpleTests(TestCase):
    def testMatrixConstructionWithInvalidArguments(self):
        """Создание матрицы с неправильными аргументами"""

        # передаём неверные аргументы и проверяем, что генерируется исключение
        with self.assertRaises(ValueError):
            Matrix([], 123)

        with self.assertRaises(ValueError):
            Matrix(123, [])

    def testMatrixConstructionWithInitialization(self):
        """Создание и инициализация матрицы"""

        # создаём матрицу и проверяем, что значения её элементов соответствуют тем,
        # при помощи которых была выполнена инициализация
        m = Matrix([
            [1, 2, 3],
            [4, 5, 6]
        ])

        self.assertEqual(m.get(0, 0), 1)
        self.assertEqual(m.get(0, 1), 2)
        self.assertEqual(m.get(0, 2), 3)
        self.assertEqual(m.get(1, 0), 4)
        self.assertEqual(m.get(1, 1), 5)
        self.assertEqual(m.get(1, 2), 6)

    def testMatrixCompareWithWrongSizes(self):
        """Сравнение матриц разного размера"""

        # пытаемся сравнить матрицы разного размера и проверям,
        # что генерируется исключение
        with self.assertRaises(RuntimeError):
            Matrix(1, 1) == Matrix(2, 2)

    def testDeterminant(self):
        """Вычисление определителя"""

        # проверяем, что попытка вычислить определитель для прямоугольной матрицы
        # приводит к генерации исключения
        with self.assertRaises(RuntimeError):
            Matrix(1, 2).determinant()

        with self.assertRaises(RuntimeError):
            Matrix(2, 1).determinant()

        # вычисляем определитель и проверяем результат
        m = Matrix([
            [1, 0],
            [0, 1]
        ])

        self.assertEqual(m.determinant(), 1)

        m = Matrix([
            [1, 0, 1],
            [1, 0, 1],
            [1, 2, 3]
        ])

        self.assertEqual(m.determinant(), 0)

        m = Matrix([
            [0, 0, 1],
            [1, 2, 3],
            [7, 2, 1]
        ])

        self.assertEqual(m.determinant(), -12)

    def testInvert(self):
        """Обращение матрицы"""

        # обращаем матрицу и проверяем результат
        a = Matrix([
            [1, 1],
            [2, 1]
        ])

        b = Matrix([
            [-1, 1],
            [2, -1]
        ])

        self.assertEqual(a.invert(), b)


if __name__ == "__main__":
    main()
