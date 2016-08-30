# Подключаем библиотеку для тестирования
import unittest

# Класс, описывающий набор тестов
class ExampleTest(unittest.TestCase):

    # Тестирующая функция
    def test_that_passes(self):
        # Набор проверок
        self.assertEqual(True, True)     # Требуем, чтобы оба аргумента были равны
        self.assertNotEqual(True, False) # Требуем, чтобы аргументы были различны
        self.assertGreater(2, 1)         # Требуем, чтобы первый аргумент был больше второго
        self.assertLess(1, 2)            # Требуем, чтобы первый аргумент был больше второго

    # Ещё одна тестирующая функция
    def test_that_failes(self):
        # Здесь будет ошибка, потому что требование равенства аргументов не выполнено!
        self.assertEqual(1, 2)

# Запускаем тесты на исполнение
unittest.main(verbosity=2)
