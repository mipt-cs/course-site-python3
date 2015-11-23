import numpy as np


class Matrix:
    """Класс матрицы"""

    def __init__(self, m, n=None):
        """Создаёт матрицу

        Параметры:

        **m**, **n** — размеры матрицы

        или

        **m** — список списков со значениями элементом матрицы
        """

        if isinstance(m, int) and isinstance(n, int):
            if m < 1 or n < 1:
                raise ValueError("m and n are expected to be positive numbers")
            self.m = m
            self.n = n
            self.npm = np.matrix([[0] * n for i in range(m)])
        elif isinstance(m, list) and n is None:
            self.npm = np.matrix(m)
        else:
            raise ValueError("Invalid input types: %s and %s" % (type(m), type(n)))

    def get_size(self):
        """Возвращает размер матрицы в виде кортежа"""

        return self.npm.shape

    def get_m(self):
        """Возвращает размер матрицы **M**xN"""

        return self.get_size()[0]

    def get_n(self):
        """Возвращает размер матрицы Mx**N**"""

        return self.get_size()[1]

    def get(self, i, j):
        """Возвращает значение элемента матрицы

        Параметры:

        **i** и **j** — индексы элемента
        """

        return self.npm.item(i, j)

    def set(self, i, j, value):
        """Изменяет значение элемента матрицы

        Параметры:

        **i** и **j** — индексы элемента

        **value** — новое значение
        """

        self.npm.itemset(i, j, value)

    def __eq__(self, other):
        """Выполняет сравнение двух матриц.

        Параметры:

        **other** — матрица для сравнения

        Возвращает True или False в зависимости от равенства матриц
        """

        if self.get_size() != other.get_size():
            raise RuntimeError("Matrixes must have equal sizes")

        return (self.npm == other.npm).all()

    def __add__(self, other):
        """Выполняет сложение двух матриц

        Параметры:

        **other** — матрица для сложения

        Возвращает новую матрицу, равную сумме исходных
        """

        return Matrix((self.npm + other.npm).tolist())

    def __sub__(self, other):
        """Выполняет вычитание двух матриц

        Параметры:

        **other** — матрица для вычитания

        Возвращает новую матрицу, равную разности исходных
        """

        return Matrix((self.npm - other.npm).tolist())

    def __mul__(self, other):
        """Выполняет умножение матрицы на другую матрицу или скаляр

        Параметры:

        **other** — другая матрица или скаляр для умножения

        """

        if isinstance(other, Matrix):
            if self.get_n() != other.get_m():
                raise RuntimeError("Can't multiply matrix with size [%d, %d] by matrix with size [%d, %d]" % (
                    *self.get_size(), *other.get_size()))

            return Matrix((self.npm * other.npm).tolist())
        else:
            return Matrix((self.npm * other).tolist())

    def __truediv__(self, other):
        """Выполняет деление матрицы на число

        Параметры:

        **other** — число, на которое требуется разделить матрицу
        """

        return self * (1 / other)

    def transpose(self):
        """Выполнеят транспонирование матрицы"""

        return Matrix(self.npm.transpose().tolist())

    def determinant(self):
        """Вычисляет определитель матрицы"""

        if self.get_m() != self.get_n():
            raise RuntimeError("Can't compute determinant for matrix with size [%d, %d]" % self.get_size())

        return np.linalg.det(self.npm)

    def invert(self):
        """Возвращает обратную матрицу"""

        if self.get_m() != self.get_n():
            raise RuntimeError("Can't invert matrix with size [%d, %d]" % self.get_size())

        if self.determinant() == 0:
            raise RuntimeError("Can't invert matrix with zero determinant")

        return Matrix(np.linalg.inv(self.npm).tolist())
