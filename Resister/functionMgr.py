from tkinter import *
from tkinter import ttk,messagebox
from colorDisplay import *

class colorMgr:
    def __init__(self):
        self.vio ='#911ac4'
        self.colorList = {'black':{'color':'black','value':'0','power':1},
                          'brown':{'color':'brown','value':'1','power':10},
                          'red':{'color':'red','value':'2','power':100},
                          'orange':{'color':'orange','value':'3','power':1_000},
                          'yellow':{'color':'yellow','value':'4','power':10_000},
                          'green':{'color':'green','value':'5','power':100_000},
                          'blue':{'color':'blue','value':'6','power':1_000_000},
                          'violet':{'color':self.vio,'value':'7','power':10_000_000},
                          'grey':{'color':'grey','value':'8','power':100_000_000},
                          'white':{'color':'white','value':'9','power':1_000_000_000},
                          }
        

    def colorChoose(self):
        pass
    def colorChoosingMenu(self,master):
        for i,v in enumerate(self.colorList.values()):
            B = Button(master,text='',bg=v['color'])
            B.grid(row=0,column=i,padx=12,ipadx=6)       

