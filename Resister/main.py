from tkinter import *
from tkinter import ttk,messagebox
from colorDisplay import *


class App:
    def __init__(self):
        #initial data
    
        self.root = Tk()
        self.root.geometry('1000x600')
        self.root.title('Resistor calculator')

        self.root.iconbitmap('Resistor.ico')
        self.L=Label(self.root,text='Resistor Calculator',font=('AR DELANEY',50),fg='dark green')
        self.L.pack(pady=20)
        self.dataPad = Frame(self.root,width=100,height=50)
        self.dataPad.pack(pady=20)
        #layout
        self.Eint = ttk.Entry(self.dataPad,font=(None,30))
        self.Eint.grid(row=0,column=0,padx=10)
        self.Bent = ttk.Button(self.dataPad,text='Enter')
        self.Bent.grid(row=0,column=1,ipady=15,ipadx=20)
        
        
        oDisplay = colorDisplay(self.root)
        oDisplay.colorDraw()

        
        
        oDisplay.colorButtonDraw()
          
          
        self.root.mainloop()

if __name__ == '__main__':
    appRunner =App()

