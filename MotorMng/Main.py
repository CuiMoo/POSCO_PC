from tkinter import * 
from tkinter import ttk,messagebox
import constant
from tkcalendar import Calendar


class App:
    def __init__(self) -> None:
        self.root = Tk()
        self.root.title('POSCO-TCS Motor Management Record 1.0')
        self.root.state('zoomed')
        self.root.iconbitmap('Tools.ico')
        
        # Menubar 
        self.menubar = Menu(self.root)
        self.root.config(menu=self.menubar)
        # File Menu
        self.fileMenu = Menu(self.menubar,tearoff=0)
        self.menubar.add_cascade(label='File',menu=self.fileMenu)
        
        self.fileMenu.add_command(label='Open')
        self.fileMenu.add_command(label='Export')
        self.fileMenu.add_command(label='Exit',command=lambda:self.root.destroy())
       
        
        self.style =ttk.Style(self.root)
        self.style.configure('TRadiobutton',font=(None,50,'bold'))
        
        #---Tab---#
        self.tab = ttk.Notebook(self.root)
        self.tab.pack(fill=BOTH,expand=2)
        self.T1 = Frame(self.tab)
        self.tab.add(self.T1,text='VC-MOTOR')
        
        #--VC-Motor Image --#
        self.motorImg = PhotoImage(file='MOTOR.png')
        
        #-Radio-Button-#
        self.v = IntVar()
        self.v.set(1)

        
        ##---Frame--##
        #_--Selection--_#
        self.menuFrame =Frame(self.T1,width=200,height=200,bg='light grey')
        self.menuFrame.pack(fill=Y,side=LEFT)
        
        #-Section-#
        self.titleFram =Frame(self.T1,width=200,height=500)
        self.titleFram.pack(fill=X)
        
        #-Detail-#
        self.detial = Frame(self.T1,width=200,height=300)
        self.detial.pack(fill=BOTH)
        
        #-Font Set-#
        self.font =constant.font
        self.sectionTitle = StringVar()
        self.sectionTitle.set('ENTRY')
        
        self.currentMotor =StringVar()
        self.motorChossen = None
    

        

    def buttonDraw(self):
        pass
    
    
    def VCsectionSelect(self):
        if self.v.get() == 1:
            self.sectionTitle.set('ENTRY')
        elif self.v.get() == 2:
            self.sectionTitle.set('CENTER')
        elif self.v.get() == 3:
            self.sectionTitle.set('DELIVERY')
        print(self.v.get())
        
        
    def sectionSelect(self):
        R1 = Radiobutton(self.menuFrame,text='     ENTER     ',
                         value='1',variable=self.v,indicator=0,
                         background='light green',
                         command= lambda :self.VCsectionSelect())
        R1.pack(fill=X,ipady=10)
        
        R2 = Radiobutton(self.menuFrame,text='     CENTER     ',
                         value='2',variable=self.v,indicator=0,
                         background='light green',
                         command= lambda :self.VCsectionSelect())
        R2.pack(fill=X,ipady=10)
        
        R2 = Radiobutton(self.menuFrame,text='     DELIVERY     ',
                         value='3',variable=self.v,indicator=0,
                         background='light green',
                         command= lambda :self.VCsectionSelect())
        R2.pack(fill=X,ipady=10)
        

    def headDraw(self):
        L1 = Label(self.detial,image=self.motorImg)
        L1.grid(row=0,column=0)
        L2 = Label(self.titleFram,textvariable=self.sectionTitle,
                   font=(self.font,40,'bold'),fg='dark blue')
        L2.pack()
        
        L3 = Label(self.detial,textvariable=self.currentMotor,font=(self.font,30))
        L3.grid(row=0,column=1)
        
        self.motorChossen = ttk.Combobox(self.detial,width=15,textvariable=self.currentMotor,
                                         justify='center')
        self.motorChossen['values'] = constant.entryMotor
        self.motorChossen.grid(row=0,column=3,padx=10)
        self.motorChossen.current(0)
        
        Cal = Calendar(self.detial,selectmode='day',
                       year = 2023,month=7,
                       day = 15)
        Cal.grid(row=0,column=4)
        
    def runApp(self):
        self.headDraw()
        self.sectionSelect()

        
        self.root.mainloop()


if __name__ == '__main__':
    appRunner = App()
    appRunner.runApp()