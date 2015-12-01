from random import randrange as rnd, choice, shuffle
from tkinter import *
import itertools, time, copy
import time
  
root = Tk()
root.geometry('800x600')
  
canv = Canvas(root, bg = 'white')
canv.pack(fill = BOTH, expand = 1)

nr = 10
nc = 12
m = 24
y0 = x0 = m


class cell():
    def __init__(self):
        self.n = 0
        self.bomb = 0
        self.mode = 'closed'
        
def new_game():
    global a
    a = [[cell() for c in range(nc)] for r in range(nr)]
    bomb_count = 18
    while bomb_count > 0:
        r = rnd(nr) 
        c = rnd(nc) 
        if not a[r][c].bomb:
            a[r][c].bomb = 1
            bomb_count -= 1
    
    for r in range(nr):
        for c in range(nc):
            k = 0
            for dr in [-1,0,1]:
                for dc in [-1,0,1]:
                    rr = r + dr
                    cc = c + dc
                    if rr in range(nr) and cc in range(nc):
                        if a[rr][cc].bomb:
                            k += 1
            a[r][c].n = k
    
    paint()




def paint():
    canv.delete(ALL)
    for r in range(nr):
        for c in range(nc):
            x = x0 + c*m
            y = y0 + r*m
            if a[r][c].mode == 'opened':
                if not a[r][c].bomb:
                    canv.create_rectangle(x,y,x+m,y+m, fill = 'white')
                    if a[r][c].n > 0:
                        canv.create_text(x+m//2,y+m//2, text = a[r][c].n)
                else:
                    canv.create_rectangle(x,y,x+m,y+m, fill = 'red')
            elif a[r][c].mode == 'closed':
                canv.create_rectangle(x,y,x+m,y+m, fill = 'gray')
            elif a[r][c].mode == 'flag':
                canv.create_rectangle(x,y,x+m,y+m, fill = 'orange')

def cell_change(r,c,button):
    if a[r][c].mode == 'closed':
        if button == 1:
            time.sleep(0.001)
            a[r][c].mode = 'opened'
            if a[r][c].n == 0:
                for dr in [-1,0,1]:
                    for dc in [-1,0,1]:
                        rr = r + dr
                        cc = c + dc
                        if rr in range(nr) and cc in range(nc):
                            paint()
                            canv.update()
                            cell_change(rr,cc,1)
                
                
            if a[r][c].bomb:
                print('boom!!!')
        elif button == 3:
            a[r][c].mode = 'flag'
    elif a[r][c].mode == 'flag' and button == 3:
         a[r][c].mode = 'closed'

    

def click(event):
    r = (event.y - y0)//m
    c = (event.x - x0)//m
    if r in range(nr) and c in range(nc):
        cell_change(r,c,event.num)
    paint()
    
new_game()        
    
    
canv.bind('<1>',click)    
canv.bind('<3>',click)    
mainloop()



from random import randrange as rnd, choice
from tkinter import *
import time, math
from random import randrange as rnd, choice
from tkinter import *
import time, math
from PIL import Image, ImageTk
 
 
root = Tk()
fr = Frame(root)
root.geometry('800x600')
bt = Button(root,width= 8, text = 'new')
bt.pack()
 
image = Image.open("3.jpg")
photo = ImageTk.PhotoImage(image)
 
canv = Canvas(root, bg = 'white')
canv.pack(fill=BOTH,expand=1)
 
 
class new_gamer():
    def __init__(self,x = 400, y = 300):
        self.x = x
        self.y = y
        r = self.r = 20
        self.id = canv.create_oval(x - r, y - r, x + r, y + r, fill = 'blue', width=5)
         
    def shot(self,target):
        tx = target.x
        ty = target.y
        s = canv.create_line(self.x,self.y,tx,ty,fill = 'orange', width = 4)
        canv.update()
        time.sleep(0.04)
        target.hit()
        canv.delete(s)
        canv.update()
         
 
class new_spider():
    def __init__(self, x = 0, y = 0, r = 20, color = 'red'):
        self.x = x
        self.y = y
        self.r = r
        self.v = 8
        self.angle = 0
        self.color = color
        
        self.id = canv.create_oval(self.x-self.r,self.y -self.r, self.x + self.r, self.y + self.r, fill = color)
        self.mode = 'on'
 
    def hit(self):
        global spiders
        if self.r > 10:
            canv.delete(self.id)
            spiders.pop(spiders.index(self))
            x = int(self.x)
            y = int(self.y)
            r = 5
            spiders += [new_spider(x-3*r,y-3*r,r, 'gray')]
            spiders += [new_spider(x+3*r,y+3*r,r, 'gray')]
            for sp in spiders[-4:]:
                sp.v = 1
             
        else:
            canv.delete(self.id)
            spiders.pop(spiders.index(self))
     
    def move(self,x,y):
        self.angle = math.atan2((self.y-y),(self.x-x))
        self.x -= self.v*(math.cos(self.angle))
        self.y -= self.v*(math.sin(self.angle))
        canv.coords(self.id,self.x-self.r,self.y -self.r, self.x + self.r, self.y + self.r)
         
colors = ['red','blue','green']
 
def new(event=0):
    global spiders, gamer
    spiders = []
    canv.delete(ALL)
    for xx in range(0,800,144):
        for yy in range(0,600,144):
            canv.create_image(xx,yy, anchor=NW, image=photo)
    class t():
        pass
    t.x = 100
    t.y = 100
    add_spiders(t)
 
    t.x = 400
    t.y = 100
    add_spiders(t)
 
    t.x = 700
    t.y = 100
    add_spiders(t)
 
    t.x = 700
    t.y = 500
    add_spiders(t)
 
    t.x = 100
    t.y = 500
    add_spiders(t)
     
    gamer = new_gamer(400,300)
sleep = 0.04
def task(event):
    live = 1
    while live:
        if spiders:
            target = spiders[0]
            td = math.sqrt(((target.x-gamer.x)**2+(target.y-gamer.y)**2))
            for spider in spiders:
                spider.move(gamer.x,gamer.y)
                d = math.sqrt((spider.x-gamer.x)**2+(spider.y-gamer.y)**2)
                if d < (gamer.r + target.r):
                    live = 0
                if td > d:
                    target = spider
                    td = d
            if live:
                gamer.shot(target)
        canv.update()
        time.sleep(sleep)
 
def add_spiders(event):
    global spiders
    x = int(event.x)
    y = int(event.y)
    r = 100
    for z in range(5):
        spiders += [new_spider(rnd(x-r,x+r),rnd(y-r,y),15, choice(colors))]
     
             
bt.bind('<Button-1>',new)
canv.bind('<Button-3>',task)
canv.bind('<Button-1>',add_spiders)
 
new()
 
mainloop()
