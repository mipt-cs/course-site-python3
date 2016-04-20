Клеточные автоматы
##################

:date: 2016-04-25


.. default-role:: code
.. contents:: Содержание

Описание работы
===============

В этой работе вы будете программировать исполнители на их языке, а также дорабатывать их реализацию.

Исполнитель нормальных алгоритмов Маркова
=========================================

Нормальный алгоритм (или алгорифм) Маркова — один из стандартных способов формального определения понятия алгоритма (другой известный способ — машина Тьюринга). Понятие нормального алгоритма введено А. А. Марковым (младшим) в конце 1940-х годов в работах по неразрешимости некоторых проблем теории ассоциативных вычислений. Традиционное написание и произношение слова «алгорифм» в этом термине также восходит к его автору, многие годы читавшему курс математической логики на механико-математическом факультете МГУ.

Нормальные алгоритмы являются вербальными, то есть предназначенными для применения к словам в различных алфавитах.

Определение всякого нормального алгоритма состоит из двух частей: определения алфавита алгоритма (к словам из символов которого алгорифм будет применяться) и определения его схемы. Схемой нормального алгоритма называется конечный упорядоченный набор так называемых формул подстановки, каждая из которых может быть простой или заключительной. Простыми формулами подстановки называются слова вида L -> D, где L и D — два произвольных слова в алфавите алгоритма (называемые, соответственно, левой и правой частями формулы подстановки). Аналогично, заключительными формулами подстановки называются слова вида L -> D., где L и D — два произвольных слова в алфавите алгоритма. При этом предполагается, что вспомогательные буквы -> и . не принадлежат алфавиту алгоритма (в противном случае на исполняемую ими роль разделителя левой и правой частей следует избрать другие две буквы).

Пример алгорифма Маркова, умножающий два числа в унарной системе счисления:

.. code-block:: text

	# Правила умножения чисел в унарной системе счисления
	# Пример входной строки: 1111*111

	# используем *, чтобы сделать первое унарное число "умножатором"
	1* -> *b
	*  ->

	b1 -> a1b
	ba -> ab

	# эти правила приводят ответ к нужной форме
	@a -> 1@
	@1 -> @
	@b -> @
	@  -> .
	-> @

Реализация исполнителя нормальных алгоритмов Маркова:

.. code-block:: python

	# -. coding: utf8 .-
	__author__ = "Timofey Khirianov"
	
	def read_rules(filename):
	    """example of format of file:
	        A -> B
	        BB -> C. #комментарий к строке
	        C ->
	        # D -> D --- комментированное правило
	        -> A

	        возвращает список кортежей (слово, замена, bool), где
	            bool -- признак терминальности правила
	        """
	    rules = []
	    file = open(filename)
	    for line in file:
	        line = line.strip() # убираем лишние пробелы слева и справа
	        if line.find('#') != -1:
	            line = line[:line.find('#')] # убираем из строки правила комментарий
	        if len(line) == 0: # пустые строки просто пропускаем
	            continue
	        word1, word2 = line.split('->')
	        word1 = word1.strip()
	        word2 = word2.strip()
	        if len(word2) != 0 and word2[-1] == '.':
	            rule = (word1, word2[:-1], True) # терминальное правило
	        else:
	            rule = (word1, word2, False) # не терминальное правило
	        rules.append(rule)
	    return rules


	rules = read_rules('rules1.txt')
	s = input()
	terminate_rule_found = False
	while not terminate_rule_found:
	    for rule in rules:
	        word, substitute, is_terminator = rule
	        if s.find(word) != -1:
	            s = s.replace(word, substitute, 1)
	            print(s) # распечатка промежуточного результата
	            terminate_rule_found = is_terminator
	            break #прерываем движение по приоритетам вниз


Машина Алана Тьюринга
=====================

`Машина Тьюринга`__ — абстрактный исполнитель. Была предложена Аланом Тьюрингом в 1936 году для формализации понятия алгоритма.
Согласно тезису Чёрча — Тьюринга, способна имитировать все исполнители (с помощью задания правил перехода),
каким-либо образом реализующие процесс пошагового вычисления, в котором каждый шаг вычисления достаточно элементарен.

.. __:	https://ru.wikipedia.org/wiki/%D0%9C%D0%B0%D1%88%D0%B8%D0%BD%D0%B0_%D0%A2%D1%8C%D1%8E%D1%80%D0%B8%D0%BD%D0%B3%D0%B0


.. code-block:: python

	# -. coding: utf8 .-
	__author__ = "Timofey Khirianov"

	states = {'change', 'move', 'finished'}
	stop_states = {'finished'}
	alphabet = {'A', 'B', 'C', '_'}
	shifts = {'S':0, '<-':-1, '->':+1}

	rules = {'change' :{'A' :('change', 'B', '->'),
	                    'B' :('change', 'C', '->'),
	                    'C' :('change', 'A', '->'),
	                    '_' :('move',   '_', '<-')},
	         'move' :{'A' :('move', 'A', '<-'),
	                  'B' :('move', 'B', '<-'),
	                  'C' :('move', 'C', '<-'),
	                  '_' :('finished', '_', 'S')}}
	                   
	lenta = list('_AAAABBCCABC__');
	state = 'change'
	position = 3
	print('Начальное состояние каретки:', state, ', позиция', position)
	print(position*' ', 'v', (len(lenta) - position)*' ', state, sep='')
	print(*lenta, sep='')
	while not state in stop_states:
	    alpha = lenta[position]
	    state, alpha, shift = rules[state][alpha]
	    lenta[position] = alpha
	    position += shifts[shift]
	    print(position*' ', 'v', (len(lenta) - position)*' ', state, sep='')
	    print(*lenta, sep='')
	 

Возможные продолжения разработки:

#. Вынести правила поведения и начальное состояние ленты в отдельный файл с начальными данными, чтобы они не были жёстко "зашиты" в программу, а хотя бы подключались как модуль или (в идеале) считывались как файл.
#. Визуализация работы машины Тьюринга


Одномерные клеточные автоматы
=============================

.. code-block:: python

	# -. coding: utf8 .-
	__author__ = "Timofey Khirianov"

	N = 150

	def cell_calculate(left, current, right):
	    return left^right

	def calculate_field(field):
	    """field -- список из N ноликов или единичек"""
	    new_field = [0]*N
	    for i in range(1, N-1):
	        new_field[i] = cell_calculate(field[i-1], field[i], field[i+1])
	    field[:] = new_field

	def generate_field():
	    field = [0]*N
	    x = N//2
	    field[x] = 1
	    return field

	def print_field(field):
	    for cell in field:
	        print('۞' if cell else ' ' , end = '')
	    print()
	    
	def modelling():
	    """ цикл моделирования клеточного автомата """
	    field = generate_field()
	    print_field(field)
	    for t in range(50):
	        calculate_field(field)
	        print_field(field)

	if __name__ == '__main__':
	    modelling()



"Игра Жизнь" Джона Конвея
=========================

.. code-block:: python

	# -. coding: utf8 .-
	__author__ = "Timofey Khirianov"
	from tkinter import *

	frame_sleep_time = 1   # задержка между кадрами в милисекундах

	cell_width = 3
	cell_height = 3
	cells_horizontal_number = 300
	cells_vertical_number = 200
	max_physical_x = cells_horizontal_number
	max_physical_y = cells_vertical_number
	screen_width = cell_width * cells_horizontal_number    # ширина игрового экрана
	screen_height = cell_height * cells_vertical_number    # высота игрового экрана


	def screen_x(_physical_x):
	    return round(_physical_x * cell_width)


	def screen_y(_physical_y):
	    return screen_height - round(_physical_y * cell_height)


	def physical_x(_screen_x):
	    return _screen_x / cell_width


	def physical_y(_screen_y):
	    return (screen_height - _screen_y) / cell_height


	def cell_color(symbol):
	    colors = {0: 'white', 1: 'green', ' ': None}
	    return colors[symbol]


	def cell_outline_color(symbol):
	    colors = {0: 'lightgray', 1: 'lightgray', ' ': None}
	    return colors[symbol]


	class Field:
	    def __init__(self, field_file, canvas):
	        """загружает поле с клетками из файла"""
	        self._canvas = canvas
	        with open(field_file) as file:
	            self.matrix = [None] * cells_vertical_number
	            self.avatars = [None] * cells_vertical_number
	            for yi in range(cells_vertical_number):
	                self.matrix[yi] = [None] * cells_horizontal_number
	                self.avatars[yi] = [None] * cells_horizontal_number
	                line = file.readline().rstrip()
	                line += ' '*(cells_horizontal_number - len(line))
	                for xi in range(cells_horizontal_number):
	                    # любой символ, кроме пробела -- значикт соотв. клетка жива
	                    is_cell_alive = 0 if line[xi] == ' ' else 1
	                    self.matrix[yi][xi] = is_cell_alive
	                    self.avatars[yi][xi] = canvas.create_rectangle(screen_x(xi), screen_y(yi),
	                                                                   screen_x(xi+1), screen_y(yi+1),
	                                                                   fill=cell_color(is_cell_alive),
	                                                                   outline=cell_outline_color(is_cell_alive))

	    def calculate(self):
	        """  """
	        # рассчитываем матрицу состояний клеток на следующем шаге
	        new_matrix = [[0]*cells_horizontal_number for i in range(cells_vertical_number)]
	        for yi in range(1, cells_vertical_number-1):
	            for xi in range(1, cells_horizontal_number-1):
	                # подсчитаем количество живых соседей
	                number_of_neighbours = 0
	                for i in range(-1, 2):
	                    for j in range(-1, 2):
	                        number_of_neighbours += self.matrix[yi+i][xi+j]
	                number_of_neighbours -= self.matrix[yi][xi]
	                cell_is_alive = self.matrix[yi][xi]
	                if (cell_is_alive and number_of_neighbours == 2) or number_of_neighbours == 3:
	                    new_matrix[yi][xi] = 1
	                else:
	                    new_matrix[yi][xi] = 0
	        # копируем рассчитанную матрицу в self.matrix
	        for yi in range(1, cells_vertical_number-1):
	            for xi in range(1, cells_horizontal_number-1):
	                if self.matrix[yi][xi] != new_matrix[yi][xi]:
	                    self.matrix[yi][xi] = new_matrix[yi][xi]
	                    self._canvas.delete(self.avatars[yi][xi])
	                    self.avatars[yi][xi] = self._canvas.create_rectangle(screen_x(xi), screen_y(yi),
	                                                                         screen_x(xi+1), screen_y(yi+1),
	                                                                         fill=cell_color(new_matrix[yi][xi]),
	                                                                         outline=cell_outline_color(new_matrix[yi][xi]))


	def time_event():
	    global scores
	    # перевычислить состояние поля с клетками
	    field.calculate()
	    canvas.after(frame_sleep_time, time_event)


	def mouse_move(event):
	    pass


	def mouse_click(event):
	    pass


	if __name__ == "__main__":
	    root = Tk()
	    canvas = Canvas(root, width=screen_width, height=screen_height)
	    canvas.pack()
	    canvas.bind('<Motion>', mouse_move)

	    field = Field('map1.txt', canvas)

	    time_event()  # начинаю циклически запускать таймер
	    root.mainloop()
