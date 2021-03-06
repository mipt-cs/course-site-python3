Практика: физическое моделирование
##################################

:date: 2017-09-29 09:00
:lecture_link: https://youtu.be/3I6OjxoeSS8

.. default-role:: code
.. contents:: Содержание


Введение
========

В прошлый раз мы с вами научились отрисовывать объекты на экран и освоили такой важный инструмент, как функции.

На этом занятии ваше погружение в gamedev продолжится и вы узнаете, как правильно описать физику и логику программным языком и как связать все эти компоненты воедино.

Не забудьте, что для работы с графикой у вас есть вспомогательная библиотека (`graphics.py`),
с помощью которой вы будете отображать объекты на экране.
Нужно `скачать её`__ и положить в ту (именно в ту) директорию, где вы собираетесь далее писать свои программы.

.. __: {filename}/extra/lab4/graphics.py


Моделирование движения материальной точки
-----------------------------------------

Равномерное движение
++++++++++++++++++++

Подключим библиотеку для работы с графикой.

.. code-block:: python

    import graphics as gr

    SIZE_X = 400
    SIZE_Y = 400

    window = gr.GraphWin("Model", SIZE_X, SIZE_Y)  

Начнём мы с такой простенькой задачки. Нужно смоделировать равномерное движение шарика на плоскости. Как же мы это будем делать?

Начнём с описания физической модели. Для моделирования такого процесса, нам достаточно знать 2 физические характеристики шарика: это его положение в пространстве и направление скорости.

.. code-block:: python

    #  Начальное положение шарика
    coords = gr.Point(200, 200)
    #  Скорость
    velocity = gr.Point(1, -2)

Вероятно, вас смущает, что скорость мы описываем с помощью понятия "точка". На самом деле, это абсолютно оправдано, поскольку скорость есть вектор из плоскости. 
Это гораздо лучше, чем отдельно хранить скорость по x и скорость по y, поскольку подход позволит нам тянуть за собой не две переменные, а всего лишь одну (просто вектор из R^2). 
Соответственно, нам придётся меньше держать в голове.

Симуляция материальной точки представляет собой непрерывный процесс пересчёта координат по заданным нами законам. 
Поскольку сейчас мы моделируем обычное равномерное движение, законы пересчёта будут очень просты.

X :sub:`k+1` = X :sub:`k` + V*t

Давайте будем считать, что t равно 1. Тогда все моменты времени отличаются ровно на 1. 
В таком случае, чтобы получить значения координат в следующий момент времени, нужно к текущим координатам прибавить скорость.
Напишем сразу функцию, которая будет возвращать сумму двух векторов.

.. code-block:: python

    def add(point_1, point_2):
        new_point = Point(point_1.x + point_2.x,
                          point_1.y + point_2.y)

        return new_point

Эта функция поможет нам не заморачиваться каждый раз по поводу оперции сложения двух векторов и позволит сфокусироваться на более высокоуровневых вещах.

Процесс отрисовки шарика также лучше вынести на отдельный уровень абстракции и оформить в функцию.

.. code-block:: python

    def draw_circle(coords):
        circle = gr.Circle(coords, 10)
        circle.setFill('red')

        circle.draw(window)

Теперь мы вплотную подошли к процессу моделирования и визуализации. 
Сначала мы рассчитываем координаты шарика, а после отрисовываем его в полученных координатах. И так по кругу, пока мы не захотим прервать этот процесс закрытием окна.

.. code-block:: python

    while True:
        draw_circle(coords)
        coords = add(coords, velocity)

.. image:: {filename}/images/lab5/1.png
   :align: center
   :width: 500px

Как видим, мы столкнулись с двумя проблемами. Первое - вся сцена рисуется мгновенно, никаких промежуточных результатов мы не видим, было бы неплохо добавить задержку между кадрами, 
чтобы мы могли наблюдать эволюцию системы. Второе - мы видим, что на экране остаются изображения шариков в предыдущие моменты времени, от этого артефакта мы бы тоже хотели избавиться.

Давайте напишем функцию, которая очищает экран.

.. code-block:: python

    def clear_window():
        rectangle = gr.Rectangle(gr.Point(0, 0), gr.Point(SIZE_X, SIZE_Y))
        rectangle.setFill('green')
        rectangle.draw(window)

А в основном цикле пропишем команду, которая усыпляет выполнение скрипта на какое то небольшое время

Весь написанный нами пример можно посмотреть `здесь`__.

.. __: {filename}/code/lab5/1.py

Отражение от стенок
+++++++++++++++++++

Давайте усовершенствуем нашу модель. В течение двух секунд шарик покидает область экрана, и мы теряем возможность за ним наблюдать. 
Для решения этой проблемы добавим упругое отражение шарика от стенок экрана. Это делается очень простым образом. 
В теле основного цикла добавим функцию, которая будет проверять столкновение, и, в случае такого события, инвертировать скорость шарика по нужной оси.

.. code-block:: python
    def check_coords(coords, velocity):
        if coords.x < 0 or coords.x > SIZE_X:
            velocity.x = -velocity.x

        if coords.y < 0 or coords.y > SIZE_Y:
            velocity.y = -velocity.y

.. code-block:: python
    while True:
        clear_window()
        draw_ball(coords)
        coords = add(coords, velocity)

        check_coords(coords, velocity)

        gr.time.sleep(0.02)

Весь код `здесь`__. 

.. __: {filename}/code/lab5/2.py

Равномерная сила тяжести (Равноускоренное движение)
+++++++++++++++++++++++++++++++++++++++++++++++++++

Давайте ещё немного разнообразим модель, добавив в наш 2D мирок силу гравитации. Для этого достаточно написать всего лишь ещё одно физическое правило. Только на этот раз мы будем пересчитывать скорость, а не координаты.

.. code-block:: python
    #   Это переделанная функция пересчёта координат
    def update_coord s(coords, velocity):
        return add(coords, velocity)


    def update_velocity(velocity, acceleration):
        return add(velocity, acceleration)


    while True:
        clear_window()
        draw_ball(coords)

        coords = update_coords(coords, velocity)
        velocity = update_velocity(velocity, acceleration)
        check_coords(coords, velocity)

        gr.time.sleep(0.02)

Весь код `здесь`__.

.. __: {filename}/code/lab5/3.py

Центральная сила тяжести (спутник возле солнца)
+++++++++++++++++++++++++++++++++++++++++++++++

Давайте теперь рассмотрим другую модель: движение материальной точки в поле центральных сил. Несмотря на то, что на первый взгляд задача кажется сложной, нам нужно лишь слегка модифицировать код, чтобы мы могли наблюдать данную модель.
Отличие данной задачи от предыдущей заключается в том, что в прошлой задаче ускорение было постоянным, а теперь ускорение будет меняться в каждый момент времени в соответствии с законом гравитационного притяжения.

Добавим следующую функцию:

.. code-block:: python
    def update_acceleration(ball_coords, center_coords):
        diff = sub(ball_coords, center_coords)
        distance_2 = (diff.x ** 2 + diff.y ** 2) ** (3/2)

        #Данная константа установлена методом научного подгона
        G = 2000

        return gr.Point(-diff.x*G/distance_2, -diff.y*G/distance_2)

Весь код `здесь`__.

.. __: {filename}/code/lab5/4.py

Как мы можем заметить, наш модульный подход позволил нам внести в наш код минимальные изменения, чтобы решить абсолютно другую задачу.
Однако, у приведенного решения есть два узких места. Первое - вы можете заметить, что орбита не подчиняется в полной мере законам Кеплера. Это связано с погрешностью машинных вычислений.
Для того, чтобы минимизировать данный недостаток, нужно считать более умным способом, но это относится к области вычислительной математики. Второе - со временем у нас сильно проседает производительность. 
Это связано с тем, что в цикле while мы постоянно создаем новые графические обьекты в функциях draw_ball() и clear_window() а старые никуда не деваются. Со временем таких обьектов становится много и резко падает производительность.

Для того, чтобы избавиться от этой проблемы, можно объявить обьект только один раз, а потом вызывать один из методов библиотеки graphics.py

.. code-block:: python
    import graphics as gr

    SIZE_X = 800
    SIZE_Y = 800

    window = gr.GraphWin("Model", SIZE_X, SIZE_Y)

    #Обьект Circle создается здесь лишь ОДИН раз
    circle = gr.Circle(gr.Point(400, 400), 10)
    circle.draw(window)

    while True:
        #Метод move передвигает обьект circle на (1, 1) относительно его текущего положения
        circle.move(1, 1)

        gr.time.sleep(0.02)

Самостоятельное задание 1:
--------------------------

Перепишите код солнечной системы, используя метод move, так, чтобы обьекты не создавались каждый раз в цикле.

Теперь, вы решили действительно полноценную задачу. Надеемся, данная задача доставила вам удовольствие.


Самостоятельное задание 2:
--------------------------

Опираясь на примеры и используя новые инструменты, реализуйте модель математического маятника.
