from tkinter import * 
from tkinter import ttk,messagebox


class App:
    def __init__(self) -> None:
        self.root = Tk()
        self.root.title('POSCO-TCS Motor Management Record')
        self.root.state('zoomed')
        self.root.iconbitmap('Tools.ico')
        #---Tab---#
        self.tab = ttk.Notebook(self.root)
        self.tab.pack(fill=BOTH,expand=2)
        self.T1 = Frame(self.tab)
        self.tab.add(self.T1,text='VC-MOTOR')
        self.motorImg = PhotoImage(file='VCMOTOR.png')

    def buttonDraw(self):
        pass
        
    def PicDraw(self):
        L1 = Label(self.T1,image=self.motorImg)
        L1.place(x=0,y=0)
    def runApp(self):
        self.PicDraw()





        
        self.root.mainloop()


if __name__ == '__main__':
    appRunner = App()
    appRunner.runApp()