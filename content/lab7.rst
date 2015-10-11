Пострение графиков
##################

:date: 2015-10-10 21:30

.. default-role:: code
.. contents:: Содержание


Введение
========

matplotlib - набор дополнительных модулей (библиотек) языка Python. Предоставляет средства для построения самых разнообразных 2D графиков и диаграмм данных. Отличается простотой использования - для построения весьма сложных и красочно оформленных диаграмм достаточно нескольких строк кода. При этот качество получаемых изображений более чем достаточно для их публикования. Также позволяет сохранять результаты в различных форматах, например Postscript, и соответственно, вставлять изображения в документы TeX. Предоставляет API для встраивания своих графических объектов в приложения пользователя.

Пример построения графика функции:

.. code-block:: python

  	import numpy as np
	import matplotlib.pyplot as plt
	x=np.arange(-10,10.01,0.01) 
	plt.plot(x,x**2)
	plt.show()

.. image:: {filename}/images/lab7/figure_1.png
   :width: 50%


На одном рисунке можно построить несколько графиков функций:

.. code-block:: python

	import numpy as np
	import matplotlib.pyplot as plt
	x=np.arange(-10,10.01,0.01) 
	plt.plot(x,np.sin(x),x,np.cos(x),x,-x)
	plt.show()

.. image:: {filename}/images/lab7/figure_2.png
   :width: 50%


Также довольно просто на график добавить служебную информацию и отобразить сетку:

.. code-block:: python

	import numpy as np
	import matplotlib.pyplot as plt
	x=np.arange(-10,10.01,0.01) 
	plt.plot(x,np.sin(x),x,np.cos(x),x,-x)
	plt.xlabel(r'$x$') 
	plt.ylabel(r'$f(x)$') 
	plt.title(r'$f_1(x)=\sin(x),\ f_2(x)=\cos(x),\ f_3(x)=-x$')
	plt.grid(True)
	plt.show()

.. image:: {filename}/images/lab7/figure_3.png
   :width: 50%

Работа с matplotlib основана на использовании графических окон и осей (оси позволяют задать некоторую графическую область). Все построения применяются к текущим осям. Это позволяет изображать несколько графиков в одном графическом окне. По умолчанию создается одно графическое окно figure(1) и одна графическая область subplot(111) в этом окне. Команда subplot позволяет разбить графическое окно на несколько областей. Она имеет три параметра: nr; nc; np. Параметры nr и nc определяют количество строк и столбцов на которые разбивается графическая область, параметр np определяет номер текущей области (np принимает значения от 1 до nr*nc). Если nr*nc<10, то передавать параметры nr,nc,np можно без использовния запятой. Например, допустимы формы subplot(2,2,1) и subplot(221).

.. code-block:: python

	import numpy as np
	import matplotlib.pyplot as plt
	x=np.arange(-10,10.01,0.01); t=np.arange(-10,11,1) 

	#subplot 1
	plt.subplot(221)
	plt.plot(x,np.sin(x))
	plt.title(r'$\sin(x)$')
	plt.grid(True)

	#subplot 2
	plt.subplot(222)
	plt.plot(x,np.cos(x),'g')
	plt.axis('equal')
	plt.grid(True)
	plt.title(r'$\cos(x)$')

	#subplot 3
	plt.subplot(223)
	plt.plot(x,x**2,t,t**2,'ro')
	plt.title(r'$x^2$')

	#subplot 4
	plt.subplot(224)
	plt.plot(x,x)
	plt.subplot(224).spines['left'].set_position('center')
	plt.subplot(224).spines['bottom'].set_position('center')
	plt.title(r'$x$')
   
	plt.show()

.. image:: {filename}/images/lab7/figure_4.png
   :width: 75%

График может быть построен в полярной системе координат:

.. code-block:: python

	import numpy as np
	import matplotlib.pyplot as plt
	plt.subplot(111, polar=True)
	phi = np.arange(0,2*np.pi,0.01)
	rho = 2*phi
	plt.plot(phi, rho, lw=2)
	plt.show()

.. image:: {filename}/images/lab7/figure_5.png
   :width: 50%


И быть задан в параметрической форме:

.. code-block:: python

	import numpy as np
	import matplotlib.pyplot as plt
	t = np.arange(0,2*np.pi,0.01)
	r=4
	plt.plot(r*np.sin(t),r*np.cos(t),lw=3)
	plt.axis('equal')
	plt.show()

.. image:: {filename}/images/lab7/figure_6.png
   :width: 50%


График функции двух переменных может быть построен например так:

.. code-block:: python

	from mpl_toolkits.mplot3d import axes3d
	import matplotlib.pyplot as plt
	import numpy as np
	ax = axes3d.Axes3D(plt.figure())
	i = np.arange(-1, 1, 0.01)
	X, Y = np.meshgrid(i, i)
	Z = X**2-Y**2
	ax.plot_wireframe(X, Y, Z, rstride=10, cstride=10)
	plt.show()

.. image:: {filename}/images/lab7/figure_7.png
   :width: 50%


Добавление текста на график:
Команду text() можно использовать для добавления текста в произвольном месте (по умолчанию координаты задаются в координатах активных осей), а команы xlabel(), ylabel() и title() служат соответственно для подписи оси абсцисс, оси ординат и всего графика. Для более полной информации смотрите Text introduction раздел на офсайте.

.. code-block:: python

	import numpy as np
	import matplotlib.pyplot as plt
	mu, sigma = 100, 15
	x = mu + sigma * np.random.randn(10000)
	# the histogram of the data
	n, bins, patches = plt.hist(x, 50, normed=1, facecolor='g', alpha=0.75)

	plt.xlabel('Smarts')
	plt.ylabel('Probability')
	plt.title('Histogram of IQ')
	plt.text(60, .030, r'$\mu=100,\ \sigma=15$')
	plt.text(50, .033, r'$\varphi_{\mu,\sigma^2}(x) = \frac{1}{\sigma\sqrt{2\pi}} \,e^{ -\frac{(x- \mu)^2}{2\sigma^2}} = \frac{1}{\sigma} \varphi\left(\frac{x - \mu}{\sigma}\right),\quad x\in\mathbb{R}$', fontsize=20, color='red')
	plt.axis([40, 160, 0, 0.04])
	plt.grid(True)
	plt.show()

.. image:: {filename}/images/lab7/figure_8.png
   :width: 50%


plot() универсальная команда и в неё можно передавать произвольное количество аргументов. Например, для того чтобы отобразить y в зависимости от x, можно выполнить команду:

.. code-block:: python

	import matplotlib.pyplot as plt
	plt.plot([1,2,3,4], [1,4,9,16])
	plt.show()

.. image:: {filename}/images/lab7/figure_9.png
   :width: 50%


Каждую последовательность можно отобразить своим типом точек:

.. code-block:: python

	import numpy as np
	import matplotlib.pyplot as plt

	# равномерно распределённые значения от 0 до 5, с шагом 0.2
	t = np.arange(0., 5., 0.2)

	# красные чёрточки, синие квадраты и зелёные треугольники
	plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
	plt.show()

.. image:: {filename}/images/lab7/figure_10.png
   :width: 50%


Функция eval()
==============
В Python есть встроенная функция eval(), которая выполняет строку с кодом и возвращает результат выполнения:

.. code-block:: python

	>>> eval("2 + 3 * len('hello')")
	17
	>>>

Это очень мощная, но в то же время и очень опасная инструкция, особенно если строки, которые вы передаёте в eval, получены не из доверенного источника. Если строкой, которую мы решим скормить eval'у, окажется os.system('rm -rf /'), то интерпретатор честно запустит процесс удаления всех данных с компьютера. 

