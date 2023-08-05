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

        #-Menu button-#
        self.comFrame =Frame(self.T1,width=300,height=50,bg='#76b5c5')
        self.comFrame.pack(fill=X,pady=5)
        
        #-Font Set-#
        self.font =constant.font
        self.sectionTitle = StringVar()
        self.sectionTitle.set('ENTRY')
        
        self.currentMotor =StringVar()
        self.motorData = constant.entryMotor

        self.h1Frame = Frame(self.hDetail,width=500,height=300)
        self.h1Frame.grid(row=0,column=0,padx=10)

        self.h2Frame = Frame(self.hDetail,width=500,height=300)
        self.h2Frame.grid(row=0,column=1,padx=10)

        self.h3Frame = Frame(self.hDetail,width=500,height=300)
        self.h3Frame.grid(row=0,column=2,padx=10)

        self.h4Frame = Frame(self.hDetail,width=300,height=300)
        self.h4Frame.grid(row=0,column=3,padx=10)

        self.h5Frame = Frame(self.hDetail,width=500,height=300,bg='light blue')
        self.h5Frame.grid(row=0,column=4,padx=10)

        self.fontCom =font.Font(family=constant.font,size=12)


        self.vTempDE = None
        self.vTempNDE = None
        self.vVibDE_V= None
        self.vViNDE_H = None
        self.vViNDE_A = None
        self.vBodyTemp = None
        
    
    def VCsectionSelect(self):
        self.motorChossen.pack_forget()
        if self.v.get() == 1:  #Entry
            self.sectionTitle.set('ENTRY')
            self.motorChossen = self.motorSelect(self.h1Frame,constant.entryMotor)
            self.motorChossen.pack()


        elif self.v.get() == 2: #Center
            self.sectionTitle.set('CENTER')
            self.motorChossen = self.motorSelect(self.h1Frame,constant.centerMotor)
            self.motorChossen.pack()


        elif self.v.get() == 3: #Delivery
            self.sectionTitle.set('DELIVERY')
            self.motorChossen = self.motorSelect(self.h1Frame,constant.deliveryMotor)
            self.motorChossen.pack()
    
    def motorSelect(self,window,data):
        #combo box for motor selection
        SelectionBox = ttk.Combobox(window,width=15,textvariable=self.currentMotor,
                                         justify='center',font=self.fontCom)
        
        SelectionBox['values'] = data
        SelectionBox['state'] = 'readonly'
        SelectionBox.current(0)
        return SelectionBox
        
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

        #-Create a combo box-#
        self.motorChossen = self.motorSelect(self.h1Frame,self.motorData)
        self.motorChossen.pack()


        #-Calendar-#
        L = Label(self.h4Frame,text='DATE',font=(self.font,15,'bold'))
        L.grid(row=0,column=0,pady=10)
        y = int(datetime.now().strftime('%Y'))
        m = int(datetime.now().strftime('%m'))
        d = int(datetime.now().strftime('%d'))
        Cal = Calendar(self.h4Frame,selectmode='day',
                       year = y,month=m,
                       day = d)
        Cal.grid(row=1,column=0,padx=10)

    def menuBar(self):
        E01 = ttk.Button(self.comFrame,text='SAVE')
        E01.pack(pady=5,ipady=12)
        E02 = ttk.Button(self.comFrame,text='EDITE')
        E02.pack(pady=5,ipady=12)
        E03 = ttk.Button(self.comFrame,text='NEW')
        E03.pack(pady=5,ipady=12)       


    def inputBoxSet(self,window,text1,text2,font):
        v_strVar = StringVar()
        T1 = Label(window,text=text1,font=font)
        E = ttk.Entry(window,textvariable=v_strVar,font=self.fontCom,justify='right')
 
        T2 = Label(window,text=text2,font=self.fontCom)
        return T1,E,v_strVar,T2
        
    def bearingTemp(self):
        #-Bearing Temp-#
        TH1 = Label(self.h2Frame,text='BEARING TEMP',font=(self.font,12,'bold'))
        TH1.grid(row=0,column=1)
        T11,E11,self.vTempDE,T12 = self.inputBoxSet(self.h2Frame,'DE','°C',self.fontCom)
        T11.grid(row=1,column=0,pady=5)
        E11.grid(row=1,column=1,pady=5)
        T12.grid(row=1,column=2,pady=5)


        T13,E14,self.vTempNDE,T15 = self.inputBoxSet(self.h2Frame,'NDE','°C',self.fontCom)
        T13.grid(row=2,column=0,pady=5)
        E14.grid(row=2,column=1,pady=5)
        T15.grid(row=2,column=2,pady=5)

        #-Vibration-#
        TH2 = Label(self.h2Frame,text='VIBRATION',font=(self.font,12,'bold'))
        TH2.grid(row=3,column=1)
        T16,E17,self.vVibDE_V,T18 = self.inputBoxSet(self.h2Frame,'Vertical','mm/s',self.fontCom)
        T16.grid(row=4,column=0,pady=5)
        E17.grid(row=4,column=1,pady=5)
        T18.grid(row=4,column=2,pady=5)

        T19,E20,self.vViNDE_H,T21 = self.inputBoxSet(self.h2Frame,'Horizontal','mm/s',self.fontCom)
        T19.grid(row=5,column=0,pady=5)
        E20.grid(row=5,column=1,pady=5)
        T21.grid(row=5,column=2,pady=5)

        
        T22,E23,self.vViNDE_A,T24 = self.inputBoxSet(self.h2Frame,'Airial','mm/s',self.fontCom)
        T22.grid(row=6,column=0,pady=5)
        E23.grid(row=6,column=1,pady=5)
        T24.grid(row=6,column=2,pady=5)
        
        #-Lubrication level-#                
        TH3 = Label(self.h2Frame,text='LUBRICATION LEVEL',font=(self.font,12,'bold'))
        TH3.grid(row=7,column=1)
        T31,E32,self.vBodyTemp,T33 = self.inputBoxSet(self.h2Frame,'Oil Level','%',self.fontCom)
        T31.grid(row=8,column=0,pady=5)
        E32.grid(row=8,column=1,pady=5)
        T33.grid(row=8,column=2,pady=5)

        #-Text box-#
        L = Label(self.h3Frame,text='Comment',font=(self.font,15,'bold'))
        L.grid(row=0,column=0)
        TE1 = self.remarkBox(self.h3Frame)
        TE1.grid(row=1,column=0)
        # E01 = ttk.Button(self.h3Frame,text='SAVE',command='top')
        # E01.grid(row=2,column=0,ipadx=10,ipady=10)
        # E02 = ttk.Button(self.h3Frame,text='SAVE',command='top')
        # E02.grid(row=2,column=1,ipadx=10,ipady=10)
        
        self.vTempDE.set('0')
        self.vTempNDE.set('0')
        self.vVibDE_V.set('0')
        self.vViNDE_H.set('0')
        self.vViNDE_A.set('0')
        self.vBodyTemp.set('0')

    def remarkBox(self,window):
        T = Text(window,height=10,width=32,font=self.font)
        return T
    
    def historyTable(self,window):
        header = ['No','motor name','date']
        hwidth = [100,300,100,100]
        hisTable = ttk.Treeview(window,columns=header,show='headings',height=15)
        hisTable.pack()
        for hd,hw in zip(header,hwidth):
            hisTable.column(hd,width=hw)
            hisTable.heading(hd,text=hd)
        
        

    def runApp(self):
        self.headDraw()
        self.sectionSelect()
        self.bearingTemp()
        self.menuBar()
        self.historyTable(self.h5Frame)
        self.root.mainloop()


if __name__ == '__main__':
    appRunner = App()
    appRunner.runApp()