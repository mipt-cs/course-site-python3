#-*- coding: utf-8 -*

"""
Доделать
 выбор скорости
 показать, если ли другие варианты, давать выбирать их
 кнопку пояснение (аудио)
 кнопку подсказка (
"""


"""
Модуль "Робот" для обучения программированию. Версия 2.0
1. знакомство с командами управления и закраски, обход стены
2. процедуры (функции)
3. условие (ветвление)
4. for
5. while дойти до стены, обойти стену, обойти две стены, пройти по закрашенным, по стене, закрасить всё поле
6. while закрасить коридоры
7. переменная, счетчик, текст в ячейках, while до стены и обратно
8. закрасить отмеченные (использование if) (есть одна задача на установку стен)
9. закрасить треугольниками, найти сумму, закрасить четные, пройти спиралью
10. поиск пути, закрасить все. Рекурсия (вводная задача рекурсии 7-0)

Разрешено любое использование при упоминании авторства и сайта progras.ru.
Часть задач была "подсмотрена" в PascalABC

Сайт: progras.ru
skype: boris_vlasenko
email: boris-vlasenko@yandex.ru
phone: +7(905)505-49-49


Пожелания к новой версии:
1. Добавить "пульт прямого управления"
2. Сделать кнопку для перезапуска задачи без закрытия формы
3. Сделать кнопку для прямого перехода в форум

# Далее - Чертежник, черепушка, еще что-нибудь (робот без клеток, например)
# Робота на JS и HTML5
# Робота в Вконтак - обучение программированию.
# Войну Роботов во Вконтакт (обучение программированию)
"""
from tkinter import Tk, Canvas, Label, Button, Frame
from random import randrange as rnd
import  time, os
if __name__ != 'robot':
    print("Этот файл запускать не следует.")
    if not os.path.exists('task.py'):
        f1 = open('task.py','w')
        f1.write("""#-*- coding: utf-8 -*
import robot
r = robot.rmap()
r.lm('task1-1')
def task():
	pass
	#------- пишите код здесь -----
	
	
	
	
	#------- пишите код здесь -----
r.start(task)

#Отступ слева (tab) сохранять!
#r.help() - Список команд и краткие примеры
#r.demo() - показать решение этой задачи (только результат, не текст программы)
#r.demoAll() - показать все задачи (примерно 20 минут)

#r.rt() - вправо
#r.rt(3)- вправо на 3
#r.dn() - вниз
#r.up() - вверх
#r.lt() - влево
#r.pt() - закрасить  Paint

#r.cl() - закрашена ли клетка? Color
#r.fr() - свободно ли справа? freeRight
#r.fl() - свободно ли слева?  freeLeft
#r.fu() - свободно ли сверху? freeUp
#r.fd() - свободно ли снизу?  freeDown

#r.wr() - стена ли справа? freeRight
#r.wl() - стена ли слева?  freeLeft
#r.wu() - стена ли сверху? freeUp
#r.wd() - стена ли снизу?  freeDown


#red - красный
#blue - синий
#yellow - желтый
#green - зеленый
""")
        f1.close()
        if os.path.exists('task.py'): print("Был создан файл task.py - запустите его")
        else: print("""Не удалось создать task.py. Попробуйте создать его самостоятельно с таким содержанием:
#----начало файла task.py------------------------
#-*- coding: utf-8 -*
import robot
r = robot.rmap()
r.lm('task1')
r.help() # Список команд. Уберите, если не нужно
#------- пишите код здесь vvvv -----

#------- пишите код здесь ^^^^ ----- 
r.end()
#----конец файла task.py------------------------
        """)
    else: print("Запустите task.py")
    print("""    

Сайт: progras.ru
skype: boris_vlasenko
email: boris-vlasenko@yandex.ru
phone: +7(905)505-49-49
""")

class rmap():
    _var = [1]
    _nc = 0
    _nr = 0
    _r = 0
    _c = 0
    _size = 0
    _w = 0
    _d = 0
    _NoneUpdate = False
    _Nonelabel = False
    _Nonegettext = False
    _field = []
    _endPoint = (0,0)

    _robot = '' # рисунок Робота (синее кольцо)
    _park = ''

    _canvas = ''
    sleep = 0.5
    _task = ''
    _solve = ''
    _test = ''
    _res = ''
    _bum = 0

    m = []
    m.append('task1')
    m.append('task2')
    m.append('task3')
    m.append('task4')
    m.append('task5')

    m.append('task6')
    m.append('task7')
    m.append('task8')
    m.append('task9')
    m.append('task10')
    m.append('task11')
    m.append('task12')
    m.append('task13')

    class _v: # будет содержать изображение текста и квадратиков закраски и меток. Чтобы можно было "поднимать изображение"
        text = '' 
        label = '' 
        color = ''

    class _Tcell():
        color = ''
        text = ''
        label = '' # color
        wUp = False
        wLeft = False
        v = ''

    def help(self):
        """ Вывести список команд Робота
Примеры использования по команде r.help_full()
"""
        print("""
Пояснение по каждой команде: print команда.__doc__
Например:
print r.color.__doc__

---=: Команды перемещения :=---
r.rt() # Вправо
r.lt() # Влево
r.dn() # Вниз
r.up() # Вверх
r.jumpTo(r,c) # Прыжок в точку. Без особых указаний в задачах не использовать
-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=

---=: Команды изменения среды :=---
r.pt([цвет]) # Закрасить указанным цветом. По умолчанию зеленым
r.sw(направление) # Установить стену с указанной стороны
r.settext(тест) # Вписать в клетку текст
-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=

---=: Команды обратной связи :=---
r.cl() # Каким цветом закрашена клетка? r.color()
r.label() # Какого цвета метка в клетке?
r.gettext() # Какой текст в клетке?

r.getCoords() # Где Робот?
r.getCoordR() # В какой строке Робот?
r.getCoordС() # В каком столбце Робот?

r.fu() # Сверху свободно?
r.fd() # Снизу свободно?
r.fr() # Справа свободно?
r.fl() # Слева свободно?

r.wu() # Сверху стена?
r.wd() # Снизу стена?
r.wr() # Справа стена?
r.wl() # Слева стена?

r.isPark # Робот на парковке?
-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=

---=: Дополнительно :=---
r.sleep = 0.4 # Установить размер задержки после каждого хода. Меньше значение - быстрее Робот.
r._NoneUpdate = False # Отключить прорисовку поля
r._NoneUpdate = True # Включить прорисовку поля
r.demo() # Показать, что нужно сделать в текущей задаче
r.demoAll() # Показать все задачи (с решениями, по очереди)
r.randcolor() # Генерировать случайный цвет
-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=

""")

    def help_full(self):
        """ Примеры. Для получения списка команд r.help()
Примеры использования по команде r.help_full()
Больше информации по каждой команде: print команда.__doc__
Например:
print r.color.__doc__
"""
        print("""
Не реализовано в данной версии. 
Если нужно - пишите на boris-vlasenko@yandex.ru или на сайте progras.ru
""")

    def demo(self):
        """Показать выполнение задачи
Пример использования:
#-------------------
r.demo()
#-------------------

Для уcкорения использовать r.sleep = 0.01
В задании 10-3(4/5) можно отключить обновление экрана
#-------------------
r._NoneUpdate = True
r.demo()
r._NoneUpdate = False
#-------------------
"""
        global r
        r = self
        exec(self._solve)

    def demoAll(self):
        """Показать выполнение всех заданий в автоматическом режиме
Пример использования:

#-------------------
r.demoAll()
#-------------------

Для того, чтобы Робот двигался быстрее, используйте
#-------------------
r.sleep = 0 
r.demoAll()
#-------------------

"""
        global r
        r = self
        for x in r.m:
            r.lm(x)
            print(x)
            r.demo()
            r.pause()
          
    def __init__(self):
        self._w = 4 # толщина стен
        self._d = 4 # на столько меньше клетки закраска (с каждой стороны)
        self.sleep = 0.5 # замедление
        self._font_size = self._size // 2
        self._tk = Tk()
        self._tk.geometry('+0+0')
        x = (self._tk.winfo_screenwidth() - self._tk.winfo_reqwidth()) / 3
        y = (self._tk.winfo_screenheight() - self._tk.winfo_reqheight()) / 4
        self._tk.wm_geometry("+%d+%d" % (x, y))
        self._tk.title('Robot-hobot')
        self._canvas = Canvas(self._tk, width=(self._size*(self._nc+1)), height=(self._size*(self._nr+1)), bg="gray")

        buttons = Frame(self._tk)

        self.task = Label (self._tk, justify = 'left')
        self.res = Label (self._tk, justify = 'left')

        self._but_start = Button(buttons,text = 'start',width=10,height=1)
        self._but_start.bind('<ButtonRelease-1>',self.but1)

        self._but_demo = Button(buttons,text = 'demo',width=10,height=1)
        self._but_demo.bind('<ButtonRelease-1>',self.but_demo)

        self._but_reload = Button(buttons,text = 'reload',width=10,height=1)
        self._but_reload.bind('<ButtonRelease-1>',self.but_reload)

        self._but_load_next = Button(buttons,text = 'load next',width=10,height=1)
        self._but_load_next.bind('<ButtonRelease-1>',self.but_load_next)

        buttons.grid(row=0, column=0, sticky = "w") 
        self._canvas.grid(row=1, column=0, sticky = "e")
        self._but_start.pack(side = "left")
        self._but_demo.pack(side = "left")
        self._but_reload.pack(side = "left")
        self._but_load_next.pack(side = "left")
        self.task.grid(row=3, column=0, sticky = "w")
        self.res.grid(row=4, column=0, sticky = "w")

##        self.loadmap()
    def but_load_next(self,event):
        print ("load next")
        index = self.m.index(self._cur_map)
        if index < len(self.m)-1:
            self.lm(self.m[index+1])
        else:
            self.lm(self.m[0])

    	
    def but_demo(self,event):
        print ("demo")
        self.demo()

    def but1(self,event):
        print ('start')
        #self.lm(self._cur_map)
        self.solve_task()

    def but_reload(self,event):
        print ("reload")
        self.lm(self._cur_map)

            
    def clear (self):
        "Очистка данных (без перерисовки)"
        self._canvas.delete('all')
        self._field = []
        self._park = []
        self._Nonelabel = False
        self._NoneisPark = False
        self._Nonesettext = False
        self._test = ''
        self._res = ''
        self._bum = 0

        for r in range(1,self._nr+2):
            row = []
            for c in range(1,self._nc+2):
                row.append (self._Tcell())
            self._field.append(row)

        for r in range (1,self._nr):
            for c in range(1,self._nc):
                self._field[r][c].text = ''
                self._field[r][c].color = ''
                self._field[r][c].label = ''
                self._field[r][c].wUp = False
                self._field[r][c].wLeft = False
                self._field[r][c].v = self._v()
                
        for c in range (1,self._nc):
            self._field[1][c].wUp = True
            self._field[self._nr][c].wUp = True

        for r in range (1,self._nr):
            self._field[r][1].wLeft = True
            self._field[r][self._nc].wLeft = True

        self._solve = ''
        self._r = 1
        self._c = 1

    def _paintMap(self): 
        "Перерисовка  по имеющимся данным"
        remc = self._c
        remr = self._r
        size = self._size
        sleep = self.sleep
        self.sleep = 0

        self._bg = [self._canvas.create_rectangle(1,1,(size*(self._nc+1)), (size*(self._nr+1)), fill="gray")]
        # создать поле
        
        for r in range (1, self._nr+1):
            self._bg.append(self._canvas.create_line(size,r*size,self._nc*size,r*size))
            if r < self._nr: self._canvas.create_text(size/2,r*size+size/2,text=r)
        for c in range (1, self._nc+1):
            self._bg.append(self._canvas.create_line(c*size,size,c*size,self._nr*size))
            if c < self._nc: self._bg.append(self._canvas.create_text(c*size+size/2,size/2,text=c))
        # клетки и номера столбцов и строк

        for r in range (1,self._nr): 
            for c in range(1,self._nc):
                self._r = r
                self._c = c
                if  self._field[r][c].wUp: # стена сверху
                    self.setWall('up')
                if  self._field[r][c].wLeft: # стена слева
                    self.setWall('left')
                if  self._field[r][c].color != '' : # закраска
                    self.paint(self._field[r][c].color)
                if  self._field[r][c].label != '' : # метка0000
                    d = self._d 
                    x1 = self._size*(c)
                    x2 = self._size*(c+1)
                    y1 = self._size*(r)
                    y2 = self._size*(r+1)
                    self._canvas.delete(self._field[r][c].v.label)
                    self._field[r][c].v.label = self._canvas.create_rectangle(x1+d,y1+d,x2-d,y2-d, width = d-1, outline = self._field[r][c].label)
                    self._canvas.lift(self._robot)
                self.settext(self._field[r][c].text) # текст

        for self._c in range (1,self._nc): 
                if  self._field[self._nr][self._c].wUp: # стена сверху
                    self.setWall('down')

        for self._r in range (1,self._nr): 
                if  self._field[self._r][self._nc].wLeft: # стена слева
                    self.setWall('right')

        r = self._endPoint[0]
        c = self._endPoint[1]
        self._canvas.delete(self._park)
        if r > 0 and c > 0:
            self._park = self._canvas.create_oval (c*size+6,r*size+6, c*size+size-6,r*size+size-6, width = 3, outline = 'yellow')
        # конечная точка
        
        self.jumpTo((remr,remc))
        self._task = '\n'+self._task
        self.task.config(text = self._task)
        self.res.config()
        self._update()
        self.sleep = sleep
        #self.pause()

        
    def _update(self):
        "Обновить canvas"
        if not self._NoneUpdate:
            self._canvas.update()
            time.sleep(self.sleep)
        

    def start(self,fun):
        self.solve_task = fun
        self._tk.mainloop()


##Робот    

    def pause(self,t=1):
        """Приостановка выполнения программы. Пауза в секундах. 
#-------------------
r.pause() # пауза в одну секунду
#-------------------
r.pause(2) # пауза две секунды
#-------------------
"""
        time.sleep(t)
		
    def left(self, a = 1):
        """Шаг влево
#-------------------
r.left()
#-------------------
r.lt()
#-------------------
r.lt(3) 
#-------------------
"""
        if a == 1:
            if self.freeLeft():
                self._c -= 1
                self._canvas.move(self._robot,-self._size*a,0)
                self._update()
            else:
                self._stop()
        else :
            for z in range(0,a):
                self.left()

    def right(self, a = 1):
        """ Шаг вправо        
#-------------------
r.right()
#-------------------
r.rt()
#-------------------
r.rt(5)
#-------------------
"""        
        if a == 1:
            if self.freeRight():
                self._c += 1
                self._canvas.move(self._robot,self._size*a,0)
                self._update()
            else:
                self._stop()
                
        else :
            for z in range(0,a):
                self.right()
        
    def up(self, a = 1):
        """Шаг вверх
#-------------------
r.up()
#-------------------
r.up(3)
#-------------------
"""
        if a == 1:
            if self.freeUp():
                self._r -= 1
                self._canvas.move(self._robot,0,-self._size*a)
                self._update()
            else:
                self._stop()
        else :
            for z in range(0,a):
                self.up()
        
    def down(self, a = 1):
        """ Шаг вниз
#-------------------
r.down()
#-------------------
r.dn()
#-------------------
r.dn(4)
#-------------------
"""
        if a == 1:
            if self.freeDown():
                self._r += 1
                self._canvas.move(self._robot,0,self._size*a)
                self._update()
            else:
                self._stop()
        else :
            for z in range(0,a):
                self.down()
                
    def jumpTo(self,coord=(1,1)):
        """Прыжок в клетку с указанными координами. Через стены.
#-------------------
r.jumpTo((2,3)) # Робот окажется в третьем столбце второй строки
#-------------------
"""

        r = coord[0]
        c = coord[1]
        if ( 0 < r < self._nc) and (0 < c < self._nc):
            self._r = r
            self._c = c
            size = self._size
            self._canvas.coords(self._robot, c*size+4,r*size+4, c*size+size-4,r*size+size-4)
            self._canvas.lift(self._robot)
            self._update()
        else:
            print("Попытка переместиться за пределы поля. Отказано.")

    def paint (self, color = 'green'):
        """ Закрасить текущую клетку выбранным цветом. Если цвет не указан, то зеленым
#-------------------
r.paint() # Закрасит текущую клетку зеленым цветом
#-------------------
r.pt() # Закрасит текущую клетку зеленым цветом
#-------------------
r.pt('red') # Закрасит текущую клетку красным цветом
#-------------------
r.pt(r.randcolor()) # Закрасит текущую клетку случайным цветом
#-------------------
r.pt(r.label()) # Закрасит текущую клетку цветом метки в этой клетке
#-------------------
"""
        d = self._d+1
        self._field[self._r][self._c].color = color

        x1 = self._size*(self._c)
        x2 = self._size*(self._c+1)
        y1 = self._size*(self._r)
        y2 = self._size*(self._r+1)
        self._canvas.delete(self._field[self._r][self._c].v.color)
        self._field[self._r][self._c].v.color = self._canvas.create_rectangle(x1+d,y1+d,x2-d,y2-d, width = 0, fill = color)
        self._canvas.lift(self._field[self._r][self._c].v.text)
        self._canvas.lift(self._robot)
        self._canvas.lift(self._park)
        self._update()

    def setWall (self, target):
        """ Установить стену с указанной стороны
#-------------------
r.sw('up') # Установить стену сверху
#-------------------
r.sw('left') # Установить стену слева 
#-------------------
r.sw('down') # Установить стену снизу
#-------------------
r.sw('right') # Установить стену справа
#-------------------
"""
        size = self._size
        w = self._w
        if target == 'up':
            r = self._r
            c = self._c
            x1 = size*(c)-1
            x2 = size*(c+1)+1
            y1 = size*(r)
            y2 = size*(r+1)
            self._field[r][c].wUp = True
            self._canvas.create_line(x1,y1,x2,y1, width = w)
        elif target == 'left':
            r = self._r
            c = self._c
            x1 = size*(c)
            x2 = size*(c+1)
            y1 = size*(r)-1
            y2 = size*(r+1)+1
            self._field[r][c].wLeft = True
            self._canvas.create_line(x1,y1,x1,y2, width = w)
        elif target == 'down':
            r = self._r+1
            c = self._c
            x1 = size*(c)-1
            x2 = size*(c+1)+1
            y1 = size*(r)
            y2 = size*(r+1)
            self._field[r][c].wDown = True
            self._canvas.create_line(x1,y1,x2,y1, width = w)
        elif target == 'right':
            r = self._r
            c = self._c+1
            x1 = size*(c)
            x2 = size*(c+1)
            y1 = size*(r)-1
            y2 = size*(r+1)+1
            self._field[r][c].wRight = True
            self._canvas.create_line(x1,y1,x1,y2, width = 4)
        self._update()

    def wallUp (self):
        """ Возвращает истину, если сверху есть стена
#-------------------
if r.wallUp(): r.pt() # Закрасить, если сверху стена
#-------------------
if r.wu(): r.pt() # Закрасить, если сверху стена
#-------------------
if r.wu(): 
    r.pt() # Закрасить, если сверху стена
    r.rt() # Перейти вправо
#-------------------
while r.wu(): # Идти вправо, пока сверху есть стена
    r.rt()
"""
        return self._field[self._r][self._c].wUp 

    def wallDown (self):
        """ Возвращает истину, если снизу есть стена
#-------------------
if r.wallDown(): r.pt() # Закрасить, если снизу стена
#-------------------
if r.wd(): r.pt() # Закрасить, если снизу стена
#-------------------
if r.wd(): 
    r.pt() # Закрасить, если снизу стена
    r.rt() # Перейти вправо
#-------------------
while r.wd(): # Идти вправо, пока снизу есть стена
    r.rt()
"""
        return self._field[self._r+1][self._c].wUp 

    def wallLeft (self):
        """ Возвращает истину, если слева есть стена
#-------------------
if r.wallLeft(): r.pt() # Закрасить, если слева стена
#-------------------
if r.wl(): r.pt() # Закрасить, если слева стена
#-------------------
if r.wl(): 
    r.pt() # Закрасить, если слева стена
    r.dn() # Перейти вниз
#-------------------
while r.wl(): # Идти вниз, пока слева есть стена
    r.dn()
"""
        return self._field[self._r][self._c].wLeft

    def wallRight (self):
        """ Возвращает истину, если справа есть стена
#-------------------
if r.wallRight(): r.pt() # Закрасить, если справа стена
#-------------------
if r.wr(): r.pt() # Закрасить, если справа стена
#-------------------
if r.wr(): 
    r.pt() # Закрасить, если справа стена
    r.dn() # Перейти вниз
#-------------------
while r.wr(): # Идти вниз, пока справа есть стена
    r.dn()
"""
        return self._field[self._r][self._c+1].wLeft

    def freeUp (self):
        """ Возвращает истину, если сверху свободно (нет стены)
#-------------------
if r.freeUp(): r.pt() # Закрасить, если сверху свободно
#-------------------
if r.fu(): r.up() # Шагнуть вверх, если сверху свободно
#-------------------
if r.fu(): 
    r.up() # Шагнуть вверх
    r.pt() # Закрасить
    r.dn() # Перейти вниз
#-------------------
while r.fu(): # Идти вверх, пока сверху свободно
    r.up()
"""
        return not self._field[self._r][self._c].wUp 

    def freeDown (self):
        """ Возвращает истину, если снизу свободно (нет стены)
#-------------------
if r.freeDown(): r.pt() # Закрасить, если снизу свободно
#-------------------
if r.fd(): r.dn() # Шагнуть вверх, если снизу свободно
#-------------------
if r.fd(): 
    r.dn() # Шагнуть снизу
    r.pt() # Закрасить
    r.up() # Перейти вверх
#-------------------
while r.fd(): # Идти вниз, пока снизу свободно
    r.dn()
"""
        return not self._field[self._r+1][self._c].wUp 

    def freeLeft (self):
        """ Возвращает истину, если слева свободно (нет стены)
#-------------------
if r.freeLeft(): r.pt() # Закрасить, если слева свободно
#-------------------
if r.fl(): r.lt() # Шагнуть влево, если слева свободно
#-------------------
if r.fl(): 
    r.lt() # Шагнуть влево
    r.pt() # Закрасить
    r.rt() # Перейти вправо
#-------------------
while r.fl(): # Идти влево, пока слева свободно
    r.lt()
"""
        return not self._field[self._r][self._c].wLeft

    def freeRight (self):
        """ Возвращает истину, если снизу свободно (нет стены)
#-------------------
if r.freeDown(): r.pt() # Закрасить, если снизу свободно
#-------------------
if r.fd(): r.dn() # Шагнуть вверх, если снизу свободно
#-------------------
if r.fd(): 
    r.dn() # Шагнуть снизу
    r.pt() # Закрасить
    r.up() # Перейти вверх
#-------------------
while r.fd(): # Идти вниз, пока снизу свободно
    r.dn()
"""
        return not self._field[self._r][self._c+1].wLeft

    def getCoords(self):
        " Возвращает координаты в виде (row,column)"
        return (self._r,self._c)

    def getCoordR(self):
        " Возвращает номер строки, в которой находиться Робот"
        return self._r

    def getCoordC(self):
        " Возвращает номер столбца, в которой находиться Робот"
        return self._c

    def isPark (self):
        " Возвращает истину, если Робот находиться на парковке"
        if self._NoneisPark: self.null()
        else: return self._endPoint == self.getCoords()

    def color (self):
        """ Возвращает цвет, которым закрашена клетка
Можно использовать для проверки, закрашена ли клетка:
#-------------------
# Закрасить, если сверху закрашено
r.up()
if r.color():
    r.dn()
    r.pt()
else:
    r.dn()
#-------------------
if r.color() == 'red': r.rt() # Вправо, если закрашено красным
#-------------------
"""
        return self._field[self._r][self._c].color
    
    def randcolor (self):
        """ Возвращает случайный цвет
#-------------------
r.pt(r.randcolor()) # Закрасить случайным цветом
#-------------------
# Закрасить соседнюю клетку тем же цветом, что и текущая
x = r.color()
r.rt()
r.pt(x)
#-------------------
"""
        cr = rnd(1,255,10)
        cg = rnd(1,255,10)
        cb = rnd(1,255,10)
        color =  "#%02X%02X%02X" %(cr,cg,cb)
        return str(color)


    def label (self):
        """ Возвращает цвет метки текущей клетки
#-------------------
if r.label() == 'red': r.pt('red') # Закрасить клетку красным, если метка красная
#-------------------
"""
        if self._Nonelabel: self.null()
        else: return self._field[self._r][self._c].label
    
    def gettext(self):
        """ Возвращает текст, записанный в ячейке. 
#-------------------
if r.gettext() != '': r.rt() # Перейти вправо, если в ячейке есть какой-нибудь текст
#-------------------
if r.gettext() == '3': r.rt() # Перейти вправо, если в ячейке записано 3
#-------------------
n = r.gettext()
if n: r.rt(n) # Перейти вправо на количество шагов, указанное в клетке
#-------------------
"""
        if self._Nonegettext: self.null()
        else: return self._field[self._r][self._c].text
    
    def settext(self,text):
        """ Записать текст в клетку
#-------------------
r.settext(3)
#-------------------
"""
        self._field[self._r][self._c].text = text
        d = 1
        x1 = self._size*(self._c)
        x2 = self._size*(self._c+1)
        y1 = self._size*(self._r)
        y2 = self._size*(self._r+1)
        self._canvas.delete(self._field[self._r][self._c].v.text)
        self._field[self._r][self._c].v.text =  self._canvas.create_text(self._c*self._size+self._size/2,self._r*self._size+self._size/2,text =
                                 self._field[self._r][self._c].text, font = ('Helvetica', self._font_size,'bold'))
        self._update()

    def _stop (self):
        print ("Bum!")
        self._bum = 1
        self._canvas.delete(self._robot)
        x = self._c
        y = self._r
        
        self._robot = self._canvas.create_oval(
            x*self._size+2*self._d,y*self._size+2*self._d,
            x*self._size+self._size-2*self._d,y*self._size+self._size-2*self._d,
            fill = '#FF0000')

    def null (self, *args):
        print('Эта команда запрещена к использованию в данной задаче. Ищите другой способ')
        return ''


    def loadmap(self,mn=m[0],variant=0):
        """ Загрузить карту (задачу)
#-------------------
r.loadmap('task10-5')
#-------------------
r.lm('task10-5') # Загрузить задачу по названию
#-------------------
r.lm(r.m[5]) # Загрузить задачу по номеру
#-------------------
# Вывести полный список названий и номеров заданий
for x in r.m:
    print r.m.index(x),x
#-------------------
"""
        self._tk.title(mn)
        self._cur_map = mn
        self._NoneUpdate = False
        self._endPoint = (0, 0)
#        self._NoneUpdate = True

        if mn == 'task1':
            self._nc = 7
            self._nr = 5
            self._size = 30

            self.clear()
            self._r = 3
            self._c = 2

            self._solve = ''
            self._endPoint = (3,5)
            self._task = 'Необходимо перевести Робота по лабиринту\n' \
                         ' из начального положения в конечное.\n'

            self._field[2][2].wUp = True
            self._field[2][3].wUp = True
            self._field[2][4].wUp = True
            self._field[2][5].wUp = True

            self._field[4][2].wUp = True
            self._field[4][3].wUp = True
            self._field[4][4].wUp = True
            self._field[4][5].wUp = True

            self._field[2][4].wLeft = True
            self._field[3][3].wLeft = True
            self._field[3][5].wLeft = True

        ##--------------------------------------------------------------------------------------------
        elif mn == 'task2':
            self._nc = 16
            self._nr = 4
            self._size = 30

            self.clear()
            self._r = 3
            self._c = 1

            self._solve = ''
            
            self._task = 'Составьте программу рисования узора.\n'

        ##--------------------------------------------------------------------------------------------
        elif mn == 'task3':
            self._nc = 10
            self._nr = 5
            self._size = 30
            self.clear()
            self._r = 2
            self._c = 1

            self._endPoint = (2,9)
            self._solve = ''
            self._task = 'Необходимо провести Робота вдоль коридора\n' \
                         ' из начального положения в конечное,\n' \
                         ' заглядывая в каждый боковой коридор.'

            for i in range(2, 9):
                self._field[2][i].wUp = True
                if i%2 == 0:
                    self._field[3][i].wUp = True
                else:
                    self._field[4][i].wUp = True

                if i < 8:
                    self._field[3][i+1].wLeft = True

        ##--------------------------------------------------------------------------------------------
        elif mn == 'task4':
            self._nc = 8
            self._nr = 12
            self._size = 30
            self.clear()
            self._r = rnd(1, self._nr)
            self._c = rnd(1, self._nc)

            for i in range(0, 5):
                for j in range(0, 3):
                    self._field[6+2*j-i][2+i].label = 'red'

            self._solve = ''
            self._task = 'Составьте программу закрашивания\n' \
                         ' клеток поля, отмеченных звездочкой.\n'

        ##--------------------------------------------------------------------------------------------
        elif mn == 'task5':
            self._nc = 16
            self._nr = 11
            self._r = 1
            self._c = 1
            self._size = 30

            self.clear()
            self._solve = ''
            self._task = 'Составьте программу рисования узора.'

        ##--------------------------------------------------------------------------------------------
        ##--------------------------------------------------------------------------------------------
        elif mn == 'task6':
            self._nc = 25
            self._nr = 25
            self._r = 1
            self._c = 1
            self._size = 20
            self.clear()
            self._solve = ''
            self._task = 'Составьте программу рисования фигуры в виде буквы "Т".\n' \
                         ' Вертикальные и горизонтальные размеры пользователь вводит\n' \
                         ' с клавиатуры. Ввод данных можно осуществлять любым способом.\n'

        ##-------------------------------------------------------------------------------------------------------
        elif mn == 'task7':
            self._nc = 16
            self._nr = 11
            self._size = 25
                
            self.clear()

            self._r = rnd(1, self._nr)
            self._c = rnd(1, self._nc)

            self._field[3][2].wUp = True
            self._field[2][9].wUp = True
            self._field[3][12].wUp = True
            self._field[6][12].wUp = True
            self._field[7][3].wUp = True
            self._field[7][9].wUp = True
            self._field[8][6].wUp = True
            self._field[9][2].wUp = True
            self._field[9][11].wUp = True

            for i in range(0, 4):
                self._field[4][5+i].wUp = True
                self._field[5][5+i].wUp = True


            self._solve = ''
        
            self._task = 'Где-то в поле Робота находится горизонтальный коридор шириной в одну клетку\n' \
                         ' неизвестной длины. Робот из верхнего левого угла поля должен дойти до\n' \
                         ' коридора и закрасить клетки внутри него, как указано в задании. По полю\n' \
                         ' Робота в произвольном порядке располагаются стены, но расстояние \n' \
                         'между ними больше одной клетки.\n'
        ##--------------------------------------------------------------------------------------------
        elif mn == 'task8':
            self._nc = 16
            self._nr = 11
            self._size = 25

            self.clear()

            self._r = rnd(1, self._nr)
            self._c = rnd(1, self._nc)

            self._field[2][6].wLeft = True
            self._field[3][6].wLeft = True
            self._field[5][6].wLeft = True
            self._field[6][6].wLeft = True
            self._field[7][6].wLeft = True
            self._field[8][6].wLeft = True

            self._solve = ''
            self._task = 'Где-то в поле Робота находится вертикальная стена с отверстием в одну клетку,\n' \
                         ' размеры которой неизвестны. Робот из произвольной клетки должен дойти до\n' \
                         ' стены и закрасить клетки как показано в задании.\n'

        ##--------------------------------------------------------------------------------------------
        elif mn == 'task9':
            self._nc = 20
            self._nr = 20
            self._size = 25

            self.clear()

            self._r = rnd(1, self._nr)
            self._c = rnd(1, self._nc)

            c = rnd(2,16)
            r = rnd(2,16)
            w = rnd(3,8)
            h = rnd(3,8)
            if c + w >= self._nc: w = self._nc-c
            if r + h >= self._nc: h = self._nr-r

            for rcount in range(0,h):
                for ccount in range(0,w):
                    self._field[r + rcount][c+ccount].color = 'green'

            self._solve = ''

            self._task = 'На поле находится квадрат из закрашенных клеток. Вычислить и вывести на экран площадь квадрата.\n'

        ##--------------------------------------------------------------------------------------------
        elif mn == 'task10':
            self._nc = 15
            self._nr = 11
            self._size = 30
            self.clear()
            self._r = 2
            self._c = 1

            self._field[2][1].wUp = True
            self._field[2][2].wUp = True
            self._field[2][4].wUp = True
            self._field[2][5].wUp = True
            self._field[2][6].wUp = True
            self._field[2][8].wUp = True
            self._field[2][9].wUp = True
            self._field[2][11].wUp = True
            self._field[2][12].wUp = True
            self._field[2][13].wLeft = True

            self._field[3][1].wUp = True
            self._field[3][2].wUp = True
            self._field[3][3].wUp = True
            self._field[3][4].wUp = True
            self._field[3][6].wUp = True
            self._field[3][7].wUp = True
            self._field[3][8].wUp = True
            self._field[3][10].wUp = True
            self._field[3][11].wUp = True
            self._field[3][12].wLeft = True

            self._field[4][3].wLeft = True
            self._field[4][3].wUp = True
            self._field[4][4].wUp = True
            self._field[4][5].wUp = True
            self._field[4][6].wUp = True
            self._field[4][8].wUp = True
            self._field[4][9].wUp = True
            self._field[4][10].wUp = True
            self._field[4][11].wUp = True
            self._field[4][13].wLeft = True

            self._field[5][3].wLeft = True
            self._field[5][4].wLeft = True
            self._field[5][4].wUp = True
            self._field[5][6].wUp = True
            self._field[5][7].wUp = True
            self._field[5][8].wUp = True
            self._field[5][10].wUp = True
            self._field[5][11].wUp = True
            self._field[5][12].wUp = True

            self._field[6][3].wLeft = True
            self._field[6][4].wUp = True
            self._field[6][5].wLeft = True

            self._field[7][3].wUp = True
            self._field[7][4].wLeft = True
            self._field[7][6].wUp = True
            self._field[7][7].wLeft = True

            self._field[8][4].wUp = True
            self._field[8][5].wUp = True
            self._field[8][6].wLeft = True
            self._field[8][7].wUp = True
            self._field[8][8].wLeft = True

            self._field[9][6].wUp = True
            self._field[9][7].wLeft = True
            self._field[9][8].wUp = True
            self._field[9][9].wUp = True
            self._field[9][10].wLeft = True

            self._field[10][7].wUp = True
            self._field[10][9].wLeft = True
            self._field[10][10].wLeft = True

            self._endPoint = (10,1)
            self._solve = """
"""

            self._task = 'Необходимо провести Робота по коридору шириной в одну клетку из начального положения до конца коридора, \n' \
                         'закрашивая при этом все клетки коридора, которые имеют выход. Выходы размером в одну клетку располагаются \n' \
                         'произвольно по всей длине коридора. Коридор заканчивается тупиком. Коридор имеет два горизонтальных и \n' \
                         'диагональный участки. Пример коридора показан на рисунке.\n'

        elif mn == 'task11':
            self._nc = 15
            self._nr = 11
            self._size = 30
            self.clear()

            self._r = rnd(1, self._nr)
            self._c = rnd(1, self._nc)

            for i in range(1,self._nr):
                for j in range(1,self._nc):
                    self._field[i][j].text = str(rnd(0, 10))

            self._task = 'На поле 10х15 каждой в каждой клетке записана цифра (от 0 до 9).\n Закрасить квадрат 2х2 с наименьшей суммой значений клеток.'

        elif mn == 'task12':
            self._nc = 15
            self._nr = 6
            self._size = 30
            self.clear()

            self._r = 2
            self._c = 13

            self._field[2][2].wUp = True
            self._field[2][3].wLeft = True
            self._field[3][3].wLeft = True
            self._field[4][3].wLeft = True
            self._field[5][3].wUp = True
            self._field[5][4].wUp = True
            self._field[4][5].wLeft = True
            self._field[3][5].wLeft = True
            self._field[2][5].wLeft = True
            self._field[2][5].wUp = True
            self._field[2][6].wLeft = True
            self._field[3][6].wLeft = True
            self._field[4][6].wLeft = True
            self._field[5][6].wUp = True
            self._field[5][7].wUp = True
            self._field[5][8].wUp = True
            self._field[4][9].wLeft = True
            self._field[3][9].wLeft = True
            self._field[2][9].wLeft = True
            self._field[2][9].wUp = True
            self._field[2][10].wUp = True
            self._field[2][11].wLeft = True
            self._field[3][11].wLeft = True
            self._field[4][11].wLeft = True
            self._field[5][11].wUp = True
            self._field[4][12].wLeft = True
            self._field[3][12].wLeft = True
            self._field[2][12].wLeft = True
            self._field[2][12].wUp = True
            self._field[2][13].wUp = True


            self._task = 'Робот движется вдоль стены, профиль которой показан на рисунке,\n' \
                         ' от начального положения до конца стены. Необходимо закрасить\n' \
                         ' все внутренние углы стены, как показано на примере. Размеры стены\n могут быть произвольны.'

        elif mn == 'task13':
            self._nc = 20
            self._nr = 20
            self._size = 25

            self.clear()

            self._r = rnd(self._nr/2, self._nr)
            self._c = rnd(self._nc/2, self._nc)

            col = rnd(2, self._nc/2)
            row = rnd(4, self._nr/2)
            height = rnd(4, self._nr-4)

            if row + height >= self._nr:
                height = self._nr - row-1

            for i in range(row, row+height):
                self._field[i][col].wLeft = True

        ##--------------------------------------------------------------------------------------------

        ##--------------------------------------------------------------------------------------------
# сделать прямое управление с демонстрацией датчиков и возможностей
# при запуске робота создавать task.py и справочник :)
# сделать робота без клеток !!!
        ##--------------------------------------------------------------------------------------------
        ##--------------------------------------------------------------------------------------------
        else:
            print(mn)
            self._task = "Нет задачи с таким номером"
            self._test = '-'

        self._canvas.config(
            width=(self._size*(self._nc+1)),
            height=(self._size*(self._nr+1)))
        x = y = 1
        d = self._d
        d = 6
        self._robot = self._canvas.create_oval(
            x*self._size+d,y*self._size+d,
            x*self._size+self._size-d,y*self._size+self._size-d,
            outline = '#4400FF', width = 3)

        self._paintMap()

    lm = loadmap
    lt = left
    rt = right
    dn = down
    pt = paint
    sw = setWall
    wu = wallUp
    wd = wallDown
    wl = wallLeft
    wr = wallRight
    fu = freeUp
    fd = freeDown
    fl = freeLeft
    fr = freeRight
    cl = color
