from tkinter import*
from tkinter import ttk,messagebox
import csv
from datetime import datetime

############---Root---#############
root = Tk()
root.title('Motors management')
root.state('zoomed')

############--Tab Setting--#############
Tab =ttk.Notebook(root)
Tab.pack(fill=BOTH,expand=1)

T1 = Frame(Tab)

icon_tab1 = PhotoImage(file='C:/Python310/learning_by_my_self/tkinter/Motor/electricmotor.png')
Motor_Img =PhotoImage(file='C:/Python310/learning_by_my_self/tkinter/Motor/motor.png')
Tab1_name = 'ENTRY SECTION'
Tab.add(T1,text= Tab1_name,image=icon_tab1,compound='left')

####--Data--###
# allData = {}
# MotorData = {'VC-POR-01','VC-POR-02','VC-1BR-01','VC-1BR-02', 'VC-1BR-03', 'VC-1BR-04', 'VC-2BR-01','VC-2BR-01','VC-ELT-01','VC-ELT-02'}

########---Function---#######

##Input_button####

def ET(window,text,unit,font=(None,15)):
    v_strvar = StringVar()
    T1 = Label(window,text=text,font=(None,15))
    E = ttk.Entry(window,textvariable=v_strvar,font=font,justify='right')
    T2 = Label(window,text=unit,font=font)
    return (E,T1,v_strvar,T2)

##-Write to CSV file-##
def writetoCSV(data,filename = ''):
    with open(filename,'a',newline ='',encoding='utf-8') as file:
        fw = csv.writer(file)  #fw = file writer
        fw.writerow(data)

##-Save Record-##
def SaveRecord():
    date = datetime.now().strftime('%Y-%m-%d')
    time = datetime.now().strftime('%H:%M:%S')
    motorName = CurrentMotor.get()
    section = Tab1_name
    volt = v_volt.get()
    Ir = v_ampR.get()
    Is = v_ampS.get()
    It = v_ampT.get()
    Vib1 = v_Vib1.get()
    Vib2 = v_Vib2.get()
    Temp1 = v_Temp1.get()
    Temp2 = v_Temp2.get()
    writetoCSV([date,time,motorName,section,volt,Ir,Is,It,Vib1,Vib2,Temp1,Temp2],'Motor_record.csv')
    UpdateTable_record()

    v_ampR.set('0')
    v_ampS.set('0')
    v_ampT.set('0')
    v_Vib1.set('0')
    v_Vib2.set('0')
    v_Temp1.set('0')
    v_Temp2.set('0')

##--UpdateToCSV--##
def UpdateToCSV(data,filename=''):
    with open(filename,'w',newline='',encoding='utf-8') as file:
        fw =csv.writer(file)
        fw.writerows(data)

##--update table
allRecord ={}

def UpdateTable_record():
    with open('Motor_record.csv',newline='',encoding='utf-8') as file:
        fr = csv.reader(file)
        table_record.delete(*table_record.get_children()) #clear table
        for row in fr:
            table_record.insert('',0,values=row)
            timeRec = row[1]
            allRecord[timeRec] = row

    print('allRec',allRecord)        
                             
##--Delete data in selected table
def DeleteData(event):
    global allRecord
    select = table_record.selection()  #selected item
    data = table_record.item(select)['values']
    print(data)
    print(data[1])
    del allRecord[data[1]]
    print(data)
    UpdateToCSV(list(allRecord.values()),'Motor_record.csv')
    UpdateTable_record()
    
    
########--Table--#########
F12 = Frame(T1,width=700,height=700)
F12.place(x=800,y=75)
header = ['Date','Time','Motor Name','Section','Voltage','Ir','Is','It','Vibration DE','Vibration NDE','Temp DE','Temp NDE']
hwidth = [100,100,120,100,75,50,50,50,100,100,100,100]

table_record = ttk.Treeview(F12,columns=header,show='headings',height=25)
table_record.pack()

for hd,hw in zip(header,hwidth):
    table_record.column(hd,width=hw)
    table_record.heading(hd,text=hd)


########---Tab1---##########
L1 = Label(T1,text=Tab1_name,font=(None,30,'bold')).pack()
CF1 =Frame(T1)
CF1.place(x=1,y=1)


#####-Combobox-####
L3 = Label(T1,text='Motor Select',font=(None,12,'bold')).place(x=505,y=20)
CurrentMotor = StringVar()
MotorChossen = ttk.Combobox(T1,width=15,textvariable=CurrentMotor,justify='center')
MotorChossen['values'] =('VC-POR-01',
                         'VC-POR-02',
                         'VC-1BR-01',
                         'VC-1BR-02',
                         'VC-1BR-03',
                         'VC-1BR-04',
                         'VC-2BR-01',
                         'VC-2BR-02',
                         'VC-ELT-01',
                         'VC-ELT-02')

MotorChossen.place(x=500,y=50)
MotorChossen.current(0)

L2 = Label(T1,textvariable=CurrentMotor,font=(None,30)).place(x=75,y=150)

MotorPic =Label(T1,image=Motor_Img)
MotorPic.place(x=50,y=200)

E11,L11,v_volt,L12 = ET(T1,'Voltage:','V.')
E11.place(x=450,y=100)
E11.focus()
L11.place(x=350,y=100)
L12.place(x=680,y=100)
v_volt.set('380')

E12,L13,v_ampR,L14 = ET(T1,'Current R:','A.')
E12.place(x=450,y=150)
L13.place(x=350,y=150)
L14.place(x=680,y=150)

E13,L15,v_ampS,L16 = ET(T1,'Current S:','A.')
E13.place(x=450,y=200)
L15.place(x=350,y=200)
L16.place(x=680,y=200)

E14,L17,v_ampT,L18 = ET(T1,'Current T:','A.')
E14.place(x=450,y=250)
L17.place(x=350,y=250)
L18.place(x=680,y=250)


L = Label(T1,text='Vibration',font=(None,15)).place(x=525,y=300)
E15,L19,v_Vib1,L20 = ET(T1,'DE:','mm/s')
E15.place(x=450,y=350)
L19.place(x=350,y=350)
L20.place(x=680,y=350)

E16,L21,v_Vib2,L22 = ET(T1,'NDE:','mm/s')
E16.place(x=450,y=400)
L21.place(x=350,y=400)
L22.place(x=680,y=400)

L = Label(T1,text='Temperature',font=(None,15)).place(x=505,y=450)
E15,L23,v_Temp1,L24= ET(T1,'DE:','C')
E15.place(x=450,y=500)
L23.place(x=350,y=500)
L24.place(x=680,y=500)

E16,L25,v_Temp2,L26 = ET(T1,'NDE:','C')
E16.place(x=450,y=550)
L25.place(x=350,y=550)
L26.place(x=680,y=550)


Bsave = ttk.Button(T1,text='Save',command=SaveRecord)
Bsave.place(x=525,y=600)
# Bsave.bind('<Return>',lambda x:SaveRecord)

table_record.bind('<Delete>',DeleteData)

UpdateTable_record()

root.mainloop()
