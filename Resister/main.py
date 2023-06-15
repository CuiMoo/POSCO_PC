from tkinter import *
from tkinter import ttk,messagebox
from colorDisplay import *
from functionMgr import *

class App:
    def __init__(self):
        #initial data
        self.root = Tk()
        self.root.geometry('1000x750')
        self.root.title('Resistor calculator')
        #layout
        self.Eint = ttk.Entry(self.root,font=(None,30))
        self.Eint.pack(pady=20)
        self.Bent = ttk.Button(self.root,text='Enter')
        self.Bent.pack(ipadx=10,ipady=10)
        
        
        oDisplay = colorDisplay(self.root)
        oDisplay.colorDraw('red','brown','blue','yellow')
        
        #--------color choosing tab frame--------------------#
        self.colorChooseTab = Frame(self.root,width=500,height=50)
        self.colorChooseTab.pack(pady=10)
        
        #--------color choosing menu frame--------------------#
        self.colorChooseMenu = Frame(self.root,width=500,height=50)
        self.colorChooseMenu.pack()
          
        #strip Selectlor
        oDisplay.stripColor(self.colorChooseMenu,'yellow','yellow','yellow','yellow')
  
        #--------color button menu tab--------------------#
        oColorMgr =colorMgr()
        oColorMgr.colorChoosingMenu(self.colorChooseTab)
        print(oColorMgr.colorList)
        
        
        
        
        self.root.mainloop()

if __name__ == '__main__':
    appRunner =App()
