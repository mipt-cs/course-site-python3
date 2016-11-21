Рекурсия: фракталы и обход в глубину
####################################

:date: 2016-11-24 13:40
:status: draft

.. default-role:: code
.. contents:: Содержание

Рекурсия
========

Как мы видели раньше функции могут вызывать другие функции — это вполне обыденная ситуация. При этом функция может
вызывать саму себя. Такой тип вызова называется **рекурсивным**. Самый простой пример рекурсивного вызова функции —
вычисление факториала числа:

.. code-block:: pycon

   >>> def fac(n):
   ...        if n == 0:
   ...            return 1
   ...        else:
   ...            return n*fac(n-1)
   ...
   >>> fac(5)
   120

Конечно, эту программу можно переписать и без рекурсивных вызовов:

.. code-block:: pycon

   >>> def fac(n):
   ...     f = 1
   ...     x = 2
   ...     while x <= n:
   ...         f *= x
   ...         x += 1
   ...
   ...     return f
   ...
   >>> fac(5)
   120

Отличие этих двух программ кроется в подходе к их построению. Первая написана в **декларативном** стиле, то есть для
вычисления факториала используются его *свойства*, а именно `n! = n*(n-1)!` и `0!=1`. Второй же подход использует
**императивный** стиль: мы *явно описываем*, что *представляет из себя* факториал: `n! = 1*2*…*n`. В большинстве случаев
один и тот же алгорит может быть легко записан, как в рекурсивной форме, так и в нерекурсивной, но существует ряд задач,
для которых построение нерекурсивного алгоритма представляется весьма трудозатратным.

Количество вложенных рекурсивных вызовов называется **глубиной** рекурсии. В силу ограниченности вычислительных ресурсов
рекурсия в компьютерных программах не бывает бесконечной — программист должен явно следить за тем, чтоб глубина
рекурсивных вызовов не превышала заранее известного числа. Если программист об этом не позаботился (или же сделал это
некорректно), операционная система (или интерпретатор) аварийно завершит программу по исчерпанию доступых ресурсов.
Чтобы убедиться в этом, попробуйте вычислить `(-5)!` при помощи рассмотренного ранее примера рекурсивного алгоритма
вычисления факториала.

Упражнение №12: числа Фибоначчи
-------------------------------

Напишите программу, вычисляющую n-ное число Фибоначчи. Используйте рекурсивные вызовы функций. Пример

+------+-------+
| Ввод | Вывод |
+======+=======+
| 7    | 13    |
+------+-------+

.. code-block:: python

   def fib(n):
       if n < 2:
           return n
       else:
           return fib(n-2)+fib(n-1)

   print(fib(7))



Фракталы
========

Хорошим примером для иллюстрации рекурсивных алгоритмов являются задачи рисования фракталов_. Фрактальные кривые,
обладающие бесконечным самоподобием, не являются спрямляемыми_: хоть их и можно изобразить на плоскости конечной
площади, эти кривые имют бесконечную длину. Соответственно, программно их невозможно нарисовать полностью: всегда будет
возможность нарисовать кривую детальнее. Поэтому, фрактальные кривые рисуют в некотором приближении, заранее фиксируя
максимально допустимую глубину рекурсии.

.. _фракталов: https://wikipedia.org/ru/%D0%A4%D1%80%D0%B0%D0%BA%D1%82%D0%B0%D0%BB
.. _спрямляемыми: https://wikipedia.org/ru/%D0%94%D0%BB%D0%B8%D0%BD%D0%B0_%D0%BA%D1%80%D0%B8%D0%B2%D0%BE%D0%B9


Пример программы, использующей рекурсивные вызовы функции, чтобы нарисовать ветку:

.. code-block:: python

   def draw(l, n):
       if n == 0:
           turtle.left(180)
           return

       x = l/(n+1)
       for i in range(n):
           turtle.forward(x)
           turtle.left(45)
           draw(0.5*x*(n-i-1), n-i-1)
           turtle.left(90)
           draw(0.5*x*(n-i-1), n-i-1)
           turtle.right(135)

       turtle.forward(x)
       turtle.left(180)
       turtle.forward(l)

   draw(400, 5)

Результат выполнения программы при разной глубине рекурсии:

.. image:: {filename}/images/lab13/leaf2.gif
   :width: 250 px
.. image:: {filename}/images/lab13/leaf3.gif
   :width: 250 px
.. image:: {filename}/images/lab13/leaf5.gif
   :width: 250 px

Упражнение №13: кривая Коха
---------------------------

Нарисуйте `кривую Коха`_. Пример работы алгоритма при разной глубине рекурсии:

.. _`кривую Коха`: https://wikipedia.org/ru/%D0%9A%D1%80%D0%B8%D0%B2%D0%B0%D1%8F_%D0%9A%D0%BE%D1%85%D0%B0

.. image:: {filename}/images/lab13/koch_curve1.gif
   :width: 350 px
.. image:: {filename}/images/lab13/koch_curve2.gif
   :width: 350 px
.. image:: {filename}/images/lab13/koch_curve3.gif
   :width: 350 px
.. image:: {filename}/images/lab13/koch_curve4.gif
   :width: 350 px

.. code-block:: python

   import turtle

   def curve(l, n):
       if n == 0:
           turtle.forward(l)
       else:
           curve(l/3, n-1)
           turtle.left(60)
           curve(l/3, n-1)
           turtle.right(120)
           curve(l/3, n-1)
           turtle.left(60)
           curve(l/3, n-1)

   L = 800
   H = L/6*3**0.5
   N = 4

   turtle.penup()
   turtle.goto(-L/2, -H/2)
   turtle.pendown()

   curve(L, N)

Упражнение №14: снежинка Коха
-----------------------------

Нарисуйте `снежинку Коха`_. Пример работы алгоритма при разной глубине рекурсии:

.. _`снежинку Коха`: https://wikipedia.org/ru/%D0%9A%D1%80%D0%B8%D0%B2%D0%B0%D1%8F_%D0%9A%D0%BE%D1%85%D0%B0

.. image:: {filename}/images/lab13/koch_snowflake1.gif
   :width: 350 px
.. image:: {filename}/images/lab13/koch_snowflake2.gif
   :width: 350 px
.. image:: {filename}/images/lab13/koch_snowflake3.gif
   :width: 350 px
.. image:: {filename}/images/lab13/koch_snowflake4.gif
   :width: 350 px

.. code-block:: python

   import turtle

   def curve(l, n):
       if n == 0:
           turtle.forward(l)
       else:
           curve(l/3, n-1)
           turtle.left(60)
           curve(l/3, n-1)
           turtle.right(120)
           curve(l/3, n-1)
           turtle.left(60)
           curve(l/3, n-1)

   def snowflake(L, N):
       for i in range(3):
           curve(L, N)
           turtle.right(120)

   L = 300
   H = L/6*3**0.5
   N = 4

   turtle.penup()
   turtle.goto(-L/2, H)
   turtle.pendown()

   turtle.speed('fastest')
   snowflake(L, N)

Упражнение №15 кривая Минковского
---------------------------------

Нарисуйте `кривую Минковского`_. Пример работы алгоритма при разной глубине рекурсии:

.. _`кривую Минковского`: http://wikipedia.org/ru/%D0%9A%D1%80%D0%B8%D0%B2%D0%B0%D1%8F_%D0%9C%D0%B8%D0%BD%D0%BA%D0%BE%D0%B2%D1%81%D0%BA%D0%BE%D0%B3%D0%BE

.. image:: {filename}/images/lab13/minkowski_curve1.gif
   :width: 250 px
.. image:: {filename}/images/lab13/minkowski_curve2.gif
   :width: 250 px
.. image:: {filename}/images/lab13/minkowski_curve3.gif
   :width: 250 px

.. code-block:: python

   import turtle

   def curve(l, n):
       if n == 0:
           turtle.forward(l)
           return
       curve(l/4, n-1)
       turtle.left(90)
       curve(l/4, n-1)
       turtle.right(90)
       curve(l/4, n-1)
       turtle.right(90)
       curve(l/4, n-1)
       curve(l/4, n-1)
       turtle.left(90)
       curve(l/4, n-1)
       turtle.left(90)
       curve(l/4, n-1)
       turtle.right(90)
       curve(l/4, n-1)

   L = 800
   N = 3

   turtle.speed('fastest')

   turtle.penup()
   turtle.goto(-L/2, 0)
   turtle.pendown()

   curve(L, N)


Упражнение №16: кривая Леви
---------------------------

Нарисуйте `кривую Леви`_. Пример работы алгоритма при разной глубине рекурсии:

.. _`кривую Леви`: https://wikipedia.org/ru/%D0%9A%D1%80%D0%B8%D0%B2%D0%B0%D1%8F_%D0%9B%D0%B5%D0%B2%D0%B8

.. image:: {filename}/images/lab13/levi_curve1.gif
   :width: 350 px
.. image:: {filename}/images/lab13/levi_curve2.gif
   :width: 350 px
.. image:: {filename}/images/lab13/levi_curve3.gif
   :width: 350 px
.. image:: {filename}/images/lab13/levi_curve9.gif
   :width: 350 px

.. code-block:: python

   import turtle

   def curve(l, n):
       if n == 0:
           turtle.forward(l)
           return
       turtle.left(45)
       curve(l/2**0.5, n-1)
       turtle.right(90)
       curve(l/2**0.5, n-1)
       turtle.left(45)

   L = 400
   N = 9

   turtle.speed('fastest')

   turtle.penup()
   turtle.goto(-L/2, -L/3)
   turtle.pendown()

   curve(L, N)
