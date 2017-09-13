class Base:
    def hello(self):
        print("Hello! I'm base class!")

class Derived(Base):
    def hello(self):
        print("Hello! I'm derived class!")

b = Base()
d = Derived()
b.hello()
d.hello()