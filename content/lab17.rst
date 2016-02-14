Разработка игры "Pacman"
########################

:date: 2016-01-21

.. default-role:: code
.. contents:: Содержание

Введение
========

Целью текущего и следующего занятий будет знакомство с библиотекой pygame и разработка игры Pacman 

Игровой процесс
---------------

Пакман – игровое существо, похожее на колобка, способное перемещаться по лабиринту, разрушать некоторые стенки и поедать артифакты.
Цель игры – сьесть все белые точки на уровне и избежать столкновения с привиденями. Помимо точек на уровне могут находится другие сьедобные артифакты, за поедание которых начисляются дополнительные очки.  Некоторые из них могут быть замурованы в стены. 
Стены уровня бывают двух типов – разрушаемые и неразрушаемые. Разрушать стены может только Пакман.
Привидения перемещаются вдоль стен со скоростью близкой к скорости Пакмана, и на перекрестках случайным образом принимают решение куда продолжать движение. Количество привидений зависит от сложности уровня. 

Улучшения игры:

Артефакты могут не только давать большее количество очков по сравнению с точками, но и наделять пакмана волшебными свойствами (это должно визуально отображаться изменением цвета пакмана), например такими:

1. Ускорение. В  течение некоторого времени Пакман двигается быстрее.
2. Возможность проламывать неразрушаемые стены. При этом стены по периметру лабиринта разрушить нельзя.
3. Выживание в случае со встречей с привидением. (Действие свойства нужно ограничивать или по времени, или до первой встречи)
4. Режим невидимки. Если в модели перемещения привидений реализовано движение в сторону Пакмана, то на некоторое время они становятся “слепыми”

Привидения могут быть нескольких типов:

1. Бестолковые – перемещающиеся вдоль стен и случайно поворачивающие на перекрестках
2. Со зрением – если находятся с Пакманом на одной линии то начинают двигаться за ним и при этом “помнят” куда он повернул на перекрестке. Если Пакмана нет в поле зрения, то двигаются как в п.1

Первоначальное расположение пакмана и привидений может быть как задано на карте так и при каждом старте уровня определяться случайным образом.

Карта
-----

Карта представляет собой текстовый файл, в котором каждый символ описывает одну клетку игрового пространства. Например:
X – наразрушаемая стена
O – разрушаемая стена
. – точка которую нужно сьесть Пакману (могут быть не во всех свободных клетках), также могут быть замурованы в разрушаемые стены
1-9 – “волшебные” артефакты. Могут располагаться как на открытых участках лабиринта, так и быть замурованы в стены.

Библиотека PyGame
=================

PyGame (PYGAME_)– библиотека, для написания игр на языке Python. Поддерживается работа с 2D/3D и существует возможность подключать сторонние графические и физические движки.
Программа HelloWorld с использованием PyGame выглядит следующим образом:
import pygame
 
.. _PYGAME: http://www.pygame.org/

.. code-block:: python

	import pygame
	from pygame.locals import *

	pygame.init() # Инициализируем библиотеку
	window = pygame.display.set_mode((640, 480)) # Задаем размеры окошка
	pygame.display.set_caption('Hello world') # Задаем загаловок окошка

В данном примере окошко исчезает сразу после появления. Следующий шаг – добавим цикл, принимающий и обрабатывающий собщения:

.. code-block:: python

	import sys
	import pygame
	from pygame.locals import *
 
	def init_window():
		pygame.init()
    		pygame.display.set_mode((640, 480))
    		pygame.display.set_caption('Hello world 2')
 
	# В функции описывается логика поведения приложения на события, генерируемые пользователем

	def process_events(events):
		for event in events:
			# Если был клик на кнопке закрытия окна или нажата клавиша Eвс завершаем процесс
		        if (event.type == QUIT) or (event.type == KEYDOWN and event.key == K_ESCAPE):
		            sys.exit(0)
 
	def main():
		# Инициализируем окно приложения
		init_window()
    
		# В бесконечном цикле принимаем и обрабатываем сообщения
		while 1:
			process_events(pygame.event.get())
 
	if __name__ == '__main__': main()


После инициализации приложения добавляется бесконечный цикл, принимающий и обрабатывающий сообщения от клавиатуры и мыши. В данном случае приложение завершает свою работу при нажатии на кнопку закрытия окна или клавишу Esc.

Далее загрузим из файла и выведем на экран фоновое изображение и персонажа. 
Чтобы не было мерцания экрана в процессе перерисовок, обычно применяется метод рисования на скрытые поверхности: при инициализации окна создается два буфера, один из которых отображается в окне, а во второй осуществляется рисование. Как только отрисовка сцены закончена, буфера меняются местами посредством вызова функции flip().
Отрисовку фона зададим функцией:

.. code-block:: python
	
	def draw_background(scr, img=None):
		""" scr - обьект класса Surface для рисования в окне приложения,
		img - фоновая картинка, в случае отсутствия, осуществляется заливка черным фоном.
		"""
		if img:
	        	scr.blit(img, (0, 0)) # Рисуем фоновую картинку 
		else:
        		bg = pygame.Surface(scr.get_size()) # Если картинка не передана, создаем изображение  
        		bg.fill((0, 0, 0))                  # Заполняем изображение черным цветом
        		scr.blit(bg, (0, 0))                # Рисуем изображение
	.....	
	# далее в коде        
	background = pygame.image.load("./resources/background.png") # загружаем изображение 
	screen = pygame.display.get_surface() # получаем обьект Surface для рисования в окне
        draw_background(screen, background)


Класс Surface (SCREEN_) создан для рисования графических примитивов в памяти с возможностью последующего вывода на экран. 

.. _SCREEN: http://www.pygame.org/docs/ref/surface.html

Для манипуляций с изображениями игровых персонажей существует класс pygame.sprite.Sprite (SPRITE_). Создадим базовый класс для персонажей игры:

.. _SPRITE: http://www.pygame.org/docs/ref/sprite.html

.. code-block:: python	

	class GameObject(pygame.sprite.Sprite):
		# img - путь к файлу с изображением персонажа
		# x, y - координаты персонажа на карте
	        # tile_size - размер клетки игрового поля в пикселях (предполагается, что клетки игрового поля квадратные)
		# map_size - размер карты игрового поля в клетка (предполагается, что карта квадратная)
		def __init__(self, img, x, y, tile_size, map_size):
			pygame.sprite.Sprite.__init__(self)
			self.image = pygame.image.load(img) # загружаем изображение персонажа  
			self.screen_rect = None             # переменная хранящая размеры и координаты отрисовки персонажа на экране
			self.x = 0			    # x, y - координаты положения персонажа на карте
			self.y = 0
			self.tick = 0			    # время, прошедшее с момента создания персонажа, в условных единицах (см. ниже)
			self.tile_size = tile_size
			self.map_size = map_size
			self.set_coord(x, y)                # инициализация экранных координат

		def set_coord(self, x, y):
			self.x = x
			self.y = y
			self.screen_rect = Rect(floor(x) * self.tile_size, floor(y) * self.tile_size, self.tile_size, self.tile_size )

		def game_tick(self):                       # функция должна вызываться с каждым тиком игровых часов 
			self.tick += 1

		def draw(self, scr):                       # отображение персонажа на экране
			scr.blit(self.image, (self.screen_rect.x, self.screen_rect.y))

и класс конкретного героя:

.. code-block:: python	

	class Ghost(GameObject):
		def __init__(self, x, y, tile_size, map_size):
			GameObject.__init__(self, x, y, “./resourses/monster.png”, tile_size, map_size)


В данном примере примере координаты игрового обьекта задаются в пикселях относительно левого верхнего угла экрана. Поскольку игровое поле разбито на квадраты одинакового размера (тайлы) то в “игровом мире” удобее использовать тайловую систему координат.
Перевод координат их игровой в экранную осуществляется по формуле:

Х\ :sub:`экр`\ = размер тайла * X\ :sub:`игр`\
Y\ :sub:`экр`\ = размер тайла * Y\ :sub:`игр`\

В играх время течет дискретно, и измеряется в тиках (tick). Если обьект перемещается с некоторой скоростью, то координата будет выражатся по формуле x = x0 + v * n, где n = 0, 1, 2,… Для того чтобы обьект переместился на 1 клетку за 10 тиков, его скорость должна равняться 1/10, а координата будет принимать дробные значения. Номер позиции тайла на игровом поле будет равен floor(x). Иначе говоря, координаты обьекта на игровом поле могут принимать вещественные значения, в которых целая часть определяет столбец/строку в которой должен быть отрисован тайл.
     
Обьеденим вышесказанное воедино, и получим игровой персонаж и элемент стены на фоне.

.. code-block:: python	

	import sys
	import pygame
	from pygame.locals import *
	from math import floor
	import random


	def init_window():
		pygame.init()
		pygame.display.set_mode((512, 512))
		pygame.display.set_caption('Packman')


	def draw_background(scr, img=None):
		if img:
			scr.blit(img, (0, 0))
		else:
			bg = pygame.Surface(scr.get_size())
			bg.fill((0, 0, 0))
			scr.blit(bg, (0, 0))


	class GameObject(pygame.sprite.Sprite):
 		def __init__(self, img, x, y, tile_size, map_size):
			pygame.sprite.Sprite.__init__(self)
			self.image = pygame.image.load(img)
			self.screen_rect = None
			self.x = 0
			self.y = 0
			self.tick = 0
			self.tile_size = tile_size
			self.map_size = map_size
			self.set_coord(x, y)

		def set_coord(self, x, y):
			self.x = x
			self.y = y
			self.screen_rect = Rect(floor(x) * self.tile_size, floor(y) * self.tile_size, self.tile_size, self.tile_size )

		def game_tick(self):
			self.tick += 1

		def draw(self, scr):
			scr.blit(self.image, (self.screen_rect.x, self.screen_rect.y))

		
	class Ghost(GameObject):
		def __init__(self, x, y, tile_size, map_size):
			GameObject.__init__(self, './resources/ghost.png', x, y, tile_size, map_size)


	def process_events(events):
		for event in events:
			if (event.type == QUIT) or (event.type == KEYDOWN and event.key == K_ESCAPE):
				sys.exit(0)


	if __name__ == '__main__':
		init_window()
		tile_size = 32
		map_size = 16
		ghost = Ghost(5, 5, tile_size, map_size)
		background = pygame.image.load("./resources/background.png")
		screen = pygame.display.get_surface()

		while 1:
			process_events(pygame.event.get())
			pygame.time.delay(100)
			ghost.game_tick()
			draw_background(screen, background)
			ghost.draw(screen)
			pygame.display.update()


Для описания игрового поля можно использовать двумерный массив, каждый элемент которого описывает обьект, находящийся в данной клетке. Данный подход хорош ровно до того момента, пока не появится два персонажа, которые могут одновременно находится в одном месте игрового поля. Например – два привидения, движущиеся навстречу друг другу. Поэтому для описания игрового мира проще всего использовать двухмерный массив например списков.

В начальный момент в массиве содержится карта, загруженная из файла. Опишем карту в виде класса Map:

.. code-block:: python	

	class Map:
		def __init__(self, w, h):
			self.map = [ [list()]*x for i in range(y) ]
	
		# Функция возвращает список обьектов в данной точке карты
		def get(self, x, y):
			return self.map[x][y]

		# Функция, перемещающая произвольный обьект в новую точку, будет выглядеть так:
		def moveTo(self, obj, new_x, new_y):
			point = self.map[obj.x][obj.y]
			if obj in point:
				point.remove(obj)
				self.map[new_x][new_y].add(obj)
				obj.set_ccord(x,y)
				return true
			return false

		#Метод, осущеставляющий отрисовку всего игрового поля, реализуется следующим образом:
		def drawAll(self):
			

Привидения двигаются все время сами. Это достигается модификацией класса Ghost:

.. code-block:: python	

	class Ghost(GameObject):
		def __init__(self, x, y, tile_size, map_size):
			GameObject.__init__(self, './resources/ghost.png', x, y, tile_size, map_size)
			self.direction = 0                # 0 - неподвижно, 1 - вправо, 2 = вниз, 3 - влево, 4 - вверх
			self.velocity = 4.0 / 10.0        # Скорость в клетках / игровой тик 

		def game_tick(self):
			super(Ghost, self).game_tick()
			if self.tick % 20 == 0 or self.direction == 0: # Каждые 20 тиков случайно выбираем направление движения. Вариант self.direction == 0 соотвествует моменту первого вызова метода game_tick() у обьекта                                                                           
				self.direction = random.randint(1, 4)

			if self.direction == 1:                        # Для каждого направления движения увеличиваем координату до тех пор пока не достгнем стены. Далее случайно меняем напрвление движения      
				self.x += self.velocity
				if self.x >= self.map_size-1:
					self.x = self.map_size-1
					self.direction = random.randint(1, 4)
			elif self.direction == 2:
				self.y += self.velocity
				if self.y >= self.map_size-1:
					self.y = self.map_size-1
					self.direction = random.randint(1, 4)
			elif self.direction == 3:
				self.x -= self.velocity
				if self.x <= 0:
					self.x = 0
					self.direction = random.randint(1, 4)
			elif self.direction == 4:
				self.y -= self.velocity
				if self.y <= 0:
					self.y = 0
					self.direction = random.randint(1, 4)
			self.set_coord(self.x, self.y)


Пакман перемещается по игровому полю только когда игрок нажимает соответствующую клавишу:

.. code-block:: python	

	class Pacman(GameObject):
		def __init__(self, x, y, tile_size, map_size):
			GameObject.__init__(self, './resources/pacman.png', x, y, tile_size, map_size)
			self.direction = 0                # 0 - неподвижно, 1 - вправо, 2 = вниз, 3 - влево, 4 - вверх
			self.velocity = 4.0 / 10.0        # Скорость в клетках / игровой тик 

		def game_tick(self):                      # Реализация метода аналогична реализации в классе Ghost
                                                          # с небольшой разницей - направление движения меняется извне
			super(Pacman, self).game_tick()
			if self.direction == 1:
				self.x += self.velocity
				if self.x >= self.map_size-1:
					self.x = self.map_size-1
			elif self.direction == 2:
				self.y += self.velocity
				if self.y >= self.map_size-1:
					self.y = self.map_size-1
			elif self.direction == 3:
				self.x -= self.velocity
				if self.x <= 0:
					self.x = 0
			elif self.direction == 4:
				self.y -= self.velocity
				if self.y <= 0:
					self.y = 0

			self.set_coord(self.x, self.y)


	def process_events(events, packman):
		for event in events:
			if (event.type == QUIT) or (event.type == KEYDOWN and event.key == K_ESCAPE):
				sys.exit(0)
			elif event.type == KEYDOWN:               
				if event.key == K_LEFT:            # Выставляем значения поля direction у Packman в зависимости от нажатой клавиши
					packman.direction = 3
				elif event.key == K_RIGHT:
					packman.direction = 1
				elif event.key == K_UP:
					packman.direction = 4
				elif event.key == K_DOWN:
					packman.direction = 2
				elif event.key == K_SPACE:
					packman.direction = 0
	
Задание:

1) Склонируйте в свой репозиторий классы (Pacman_), описанные выше

2) Добавьте неразрушаемые стены на карту, убедитесь что пакман сквозь них не проходит и не разрушает

3) Добавьте привидение, реализуйте случайную модель поведения.

4) Добавьте второе привидение, убедитесь что они корректно могут проходить друг сквозь друга.

5) Реализуйте загрузку карты из файла

6) Добавьте на карту точки, которые пакман должен сьесть, и завершение игры когда точек более не осталось.


.. _Pacman: https://github.com/mipt-cs-on-python3/pacman




