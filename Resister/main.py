from tkinter import *
from tkinter import ttk,messagebox
from colorDisplay import *

class App:
    def __init__(self):
        self.root = Tk()
        self.root.geometry('1000x750')
        self.root.title('Resistor calculator')
        #layout
        self.Eint = ttk.Entry(self.root,font=(None,30))
        self.Eint.pack(pady=20)
        self.Bent = ttk.Button(self.root,text='Enter')
        self.Bent.pack(ipadx=10,ipady=10)
        Display = colorDisplay(self.root)
        Display.colorDraw('red','brown','blue','yellow')
        Bc1 = ttk.Button(self.root,text='')
        Bc1.pack()
        self.root.mainloop()




if __name__ == '__main__':
    appRunner =App()


