from tkinter import *
from tkinter import ttk,messagebox
from functionMgr import *

class colorDisplay():
    def __init__(self,frame):
        self.canvas = Canvas(frame,width=500,height=300)
        self.canvas.pack(pady=10)
        #resistor leg
        self.canvas.create_polygon([0,240,500,240,500,260,0,260],fill='grey',outline='white')
        #resistor body
        self.canvas.create_polygon([100,200,400,200,400,300,100,300],fill='#e8be64')
   
    def stripColor(self,frame,C1,C2,C3,C4):
        Bc1 = Button(frame ,text='1',bg=C1)
        Bc1.grid(row=0,column=0,padx=12,ipadx=6)
        Bc2 = Button(frame ,text='2',bg=C2)
        Bc2.grid(row=0,column=1,padx=12,ipadx=6)
        Bc3 = Button(frame ,text='3',bg=C3)
        Bc3.grid(row=0,column=2,padx=12,ipadx=6)
        Bc4 = Button(frame ,text='4',bg=C4)
        Bc4.grid(row=0,column=3,padx=40,ipadx=6)
    
    
    def colorDraw(self,C1,C2,C3,C4):            
        #color1
        self.canvas.create_polygon([150,200,175,200,175,300,150,300],fill=C1)
        #color2
        self.canvas.create_polygon([200,200,225,200,225,300,200,300],fill=C2)
        #color3
        self.canvas.create_polygon([250,200,275,200,275,300,250,300],fill=C3)
        #color4
        self.canvas.create_polygon([325,200,350,200,350,300,325,300],fill=C4)
        
