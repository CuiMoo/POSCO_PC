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
        self.L=Label(self.root,text='Resistor Calculator',font=('Cooper Black',50),fg='green')
        self.L.pack(pady=20)
        
        self.dataPad = Frame(self.root,width=100,height=50)
        self.dataPad.pack(pady=20)
        
        oDisplay = colorDisplay(self.root)

        oDisplay.DataBox(self.dataPad)
        oDisplay.colorDraw()

        #layout
        # Draw a entry box
       
        #Draw a enter button
        
        oDisplay.enterButton(self.dataPad)
        oDisplay.colorButtonDraw()
          
          
        self.root.mainloop()

if __name__ == '__main__':
    appRunner =App()