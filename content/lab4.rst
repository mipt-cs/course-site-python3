Практика: "Великий Аниматор"
#######################################

:date: 2017-09-22 09:00
:status: draft

.. default-role:: code
.. contents:: Содержание


Введение
========
На этом занятии мы хотим познакомиться с тем, как используя Python можно рисовать и анимировать персонажей.
Представим, что вы открыли дизайнерскую студию.

У вас есть помощник "Великий Аниматор" (`graphics.py`__) который умеет выполнять команды.

.. __: http://mcsp.wartburg.edu/zelle/python/graphics.py

Однако, этот помощник не отличается ни умом, ни сообразительностью, и у него крайне `скудный словарный запас`__.

.. __: http://mcsp.wartburg.edu/zelle/python/graphics/graphics/index.html

Пример программы для Аниматора:
-------------------------------

.. code-block:: python

	from graphics import *

	win = GraphWin("My Circle", 400, 400)
	c = Circle(Point(50,50), 10)
	c.draw(win)
	c.setFill('yellow')
	c.setOutline('red')
	c.setWidth(2)
	win.getMouse() # Pause to view result
	c.move(10,0)
	win.getMouse() # Pause to view result
	c.undraw()
	point1 = win.getMouse()
	point2 = win.getMouse()
	r = Rectangle(point1, point2)
	r.draw(win)

	
Рисуем логотип согласно ТЗ
==========================

К вам поступил заказ — нарисовать логотип.

