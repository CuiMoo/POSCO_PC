from tkinter import * 
from tkinter import ttk,messagebox,font
import constant
from tkcalendar import Calendar
from datetime import datetime



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
        self.menubar.add_cascade(label='File',menu=self.fileMenu,font=10)
        
        self.fileMenu.add_command(label='Open')
        self.fileMenu.add_command(label='Export')
        self.fileMenu.add_command(label='Exit',command=lambda:self.root.destroy())
       
        
        self.style =ttk.Style(self.root)
        self.style.configure('TRadiobutton',font=(constant.font,50,'bold'))
        
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
        self.titleFram =Frame(self.T1,width=500,height=100)
        self.titleFram.pack(fill=X)
        
        #-Detail-#
        self.hDetail = Frame(self.T1,width=200,height=300)
        self.hDetail.pack(fill=X)
        
        #-Font Set-#
        self.font =constant.font
        self.sectionTitle = StringVar()
        self.sectionTitle.set('ENTRY')
        
        self.currentMotor =StringVar()
        self.motorData = constant.entryMotor

        self.h1Frame = Frame(self.hDetail,width=500,height=500)
        self.h1Frame.grid(row=0,column=0,padx=10)

        self.h2Frame = Frame(self.hDetail,width=500,height=500,bg='#66ffcc')
        self.h2Frame.grid(row=0,column=1,padx=10)

        self.h3Frame = Frame(self.hDetail,width=500,height=500,bg='#ccccff')
        self.h3Frame.grid(row=0,column=2,padx=10)

        self.h4Frame = Frame(self.hDetail,width=500,height=500,bg='#80e5ff')
        self.h4Frame.grid(row=0,column=3,padx=10)

        self.fontCom =font.Font(family=constant.font,size=12)

    

        

    def buttonDraw(self):
        pass
    
    
    def VCsectionSelect(self):
        self.motorChossen.pack_forget()
        if self.v.get() == 1:
            self.sectionTitle.set('ENTRY')
            # self.motorData == constant.entryMotor
            self.motorChossen = ttk.Combobox(self.h1Frame,width=15,textvariable=self.currentMotor,
                                         justify='center',font=self.fontCom)
        
            self.motorChossen['values'] = constant.entryMotor
            self.motorChossen.current(0)
            self.motorChossen.pack()

        elif self.v.get() == 2:
            self.sectionTitle.set('CENTER')
            # self.motorData == constant.centerMotor
            self.motorChossen = ttk.Combobox(self.h1Frame,width=15,textvariable=self.currentMotor,
                                         justify='center',font=self.fontCom)
            
            self.motorChossen['values'] = constant.centerMotor
            self.motorChossen.current(0)
            self.motorChossen.pack()

        elif self.v.get() == 3:
            self.sectionTitle.set('DELIVERY')
            # self.motorData == constant.deliveryMotor
            self.motorChossen = ttk.Combobox(self.h1Frame,width=15,textvariable=self.currentMotor,
                                         justify='center',font=self.fontCom)

            self.motorChossen['values'] = constant.deliveryMotor
            self.motorChossen.current(0)
            self.motorChossen.pack()



        
        
    def sectionSelect(self):
        
        R1 = Radiobutton(self.menuFrame,text='     ENTER     ',
                         value='1',variable=self.v,indicator=0,
                         background='#ff8566',
                         command= lambda :self.VCsectionSelect())
        R1.pack(fill=X,ipady=10)
        
        R2 = Radiobutton(self.menuFrame,text='     CENTER     ',
                         value='2',variable=self.v,indicator=0,
                         background='#ff8566',
                         command= lambda :self.VCsectionSelect())
        R2.pack(fill=X,ipady=10)
        
        R2 = Radiobutton(self.menuFrame,text='     DELIVERY     ',
                         value='3',variable=self.v,indicator=0,
                         background='#ff8566',
                         command= lambda :self.VCsectionSelect())
        R2.pack(fill=X,ipady=10)
        

    def headDraw(self):

        motorName = Label(self.h1Frame,textvariable=self.currentMotor,font=(self.font,30))
        motorName.pack()
        L1 = Label(self.h1Frame,image=self.motorImg)
        L1.pack()

        sectionName = Label(self.titleFram,textvariable=self.sectionTitle,
                   font=(self.font,40,'bold'),fg='dark blue')
        sectionName.pack()



        self.motorChossen = ttk.Combobox(self.h1Frame,width=15,textvariable=self.currentMotor,
                                         justify='center',font=self.fontCom)
        
        self.motorChossen['values'] = self.motorData
        self.motorChossen.pack()
        self.motorChossen.current(0)

        #-Calendar-#
        y = int(datetime.now().strftime('%Y'))
        m = int(datetime.now().strftime('%m'))
        d = int(datetime.now().strftime('%d'))
        Cal = Calendar(self.h4Frame,selectmode='day',
                       year = y,month=m,
                       day = d)
        Cal.place(x=125,y=0)
        print('y:',y,'m:',m,'d:',d)


    def runApp(self):
        self.headDraw()
        self.sectionSelect()

        
        self.root.mainloop()


if __name__ == '__main__':
    appRunner = App()
    appRunner.runApp()