class SuperBase: # Предок предка
    def do(self):
        print('Метод суперпредка!')
class Base1(SuperBase):   # Предок 1
    def do_it(self):
        print('Метод предка 1')
class Base2:   # Предок 2
    def do_it(self):
        print('Метод предка 2')
class Derived(Base1, Base2):   # Наследник
    def do_it_by_myself(self):
        print('Метод наследника')

d = Derived()   # инстанциация
d.do()
d.do_it()
d.do_it_by_myself()