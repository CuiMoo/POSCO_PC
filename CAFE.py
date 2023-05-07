from tkinter import *
from tkinter import ttk, messagebox
from datetime import datetime
import csv



window = Tk()
window.title('CuiMoo\'s Restaurant')
window.geometry('1500x750')


#Tab setting
tab = ttk.Notebook(window)
tab.pack(fill=BOTH,expand=1)

#font setting
Bfont = ttk.Style()  
Bfont.configure('TButton',font=('Bahnschrift',15))

T1 = Frame(tab)
T2 = Frame(tab)


icon_tab1 = PhotoImage(file='C:/Python310/learning_by_my_self/tkinter/CAFE/Coffee_icon.png')
icon_tab2 =PhotoImage(file='C:/Python310/learning_by_my_self/tkinter/CAFE/User.png')
late = PhotoImage(file='C:/Python310/learning_by_my_self/tkinter/CAFE/late.png')
expresso = PhotoImage(file='C:/Python310/learning_by_my_self/tkinter/CAFE/expesso.png')
cappuccino = PhotoImage(file='C:/Python310/learning_by_my_self/tkinter/CAFE/cappuccino.png')
green_tea = PhotoImage(file='C:/Python310/learning_by_my_self/tkinter/CAFE/green_tea.png')
hot_tea = PhotoImage(file='C:/Python310/learning_by_my_self/tkinter/CAFE/hot_tea.png')
milk_tea = PhotoImage(file='C:/Python310/learning_by_my_self/tkinter/CAFE/milk_tea.png')

tab.add(T1,text='CAFE',image=icon_tab1,compound='left')
tab.add(T2,text='Member',image=icon_tab2,compound='left')


#####Tab1######

#Raw0
#header = ['No','Title','Price','Quantity','Total']

allMenu = {}
product = {'latte':{'name':'Latte','price':30},
           'cappucino':{'name':'Cappucino','price':35},
           'espresso':{'name':'Espresso','price':40},
           'greenTea':{'name':'Green Tea','price':35},
           'milkTea':{'name':'Milk Tea','price':45},
           'hotTea':{'name':'Hot Tea','price':40},
           }

def UpdateTable():
    table.delete(*table.get_children())  #clear the previous data in table
    for i,m in enumerate(allMenu.values(),start=1):
        #m=['latte',30,1,30]
        table.insert('','end',value=[i,m[0],m[1],m[2],m[3]])


def AddMenu(name=''):
    if name not in allMenu:
        allMenu[name] = [product[name]['name'],product[name]['price'],1,product[name]['price']]
    else:
        quan = allMenu[name][2]+1
        total =quan * product[name]['price']
        allMenu[name] = [product[name]['name'],product[name]['price'],quan,total]

    print(allMenu)
    #Net worth
    count =sum([m[3] for m in allMenu.values()])
    v_total.set(f'{count:.2f}')
    UpdateTable()



####Buton###
CF1 = Frame(T1)
CF1.place(x=50,y=100)
coffees = ['Late','Cappuccino','Espresso','Green tea','Milk Tea','Hot Tea']
coffee_icon =[late,cappuccino,expresso,green_tea,milk_tea,hot_tea]

B1 = ttk.Button(CF1,text=coffees[0],image = coffee_icon[0],compound='top',command=lambda m='latte':AddMenu(m))
B1.grid(row=0,column=0,ipadx=20,ipady=10)

B2 = ttk.Button(CF1,text=coffees[1],image = coffee_icon[1],compound='top',command=lambda m='cappucino':AddMenu(m))
B2.grid(row=0,column=1,ipadx=20,ipady=10)

B3 = ttk.Button(CF1,text=coffees[2],image = coffee_icon[2],compound='top',command=lambda m='espresso':AddMenu(m))
B3.grid(row=0,column=2,ipadx=20,ipady=10) 

B4 = ttk.Button(CF1,text=coffees[3],image = coffee_icon[3],compound='top',command=lambda m='greenTea':AddMenu(m))
B4.grid(row=1,column=0,ipadx=20,ipady=10)

B5 = ttk.Button(CF1,text=coffees[4],image = coffee_icon[4],compound='top',command=lambda m='milkTea':AddMenu(m))
B5.grid(row=1,column=1,ipadx=20,ipady=10)  

B6 = ttk.Button(CF1,text=coffees[5],image = coffee_icon[5],compound='top',command=lambda m='hotTea':AddMenu(m))
B6.grid(row=1,column=2,ipadx=20,ipady=10)  




######table########################
CF2 = Frame(T1)
CF2.place(x=700,y=100) # position

header = ['No','Title','Price','Quantity','Total']
hwidth = [50,200,100,100,100]

table = ttk.Treeview(CF2,columns = header,show='headings',height=15)
table.pack()

for hd,hw in zip(header,hwidth):
    table.column(hd,width=hw)
    table.heading(hd,text=hd)

###################################

L = Label(T1,text='Total',font=(None,15))
L.place(x=700,y=450)

v_total = StringVar()
v_total.set('0.0')
LT = Label(T1,textvariable=v_total,font=(None,15))
LT.place(x=800,y=450)



def Reset():
    global allMenu  #Use global for set allMenu in global variables
    allMenu = {}
    table.delete(*table.get_children())
    v_total.set('0.0')
    Tstm =datetime.now().strftime('%y%m%d%H%M%S') #transection generate
    v_transection.set(Tstm)
     
Breset =ttk.Button(T1,text='Clear',command=Reset).place(x=900,y=500)

############Transaction ID########################
v_transection = StringVar()
Tstm =datetime.now().strftime('%y%m%d%H%M%S') #transection generate
v_transection.set(Tstm)
LTR =Label(T1,textvariable=v_transection,font=(None,10)).place(x=1150,y=30)

###Save Button#####
FB =Frame(T1)
FB.place(x=1150,y=500)

def writeToCSV(data, filename=''):
    with open(filename,'a',newline='',encoding='utf-8') as file:
        fw =csv.writer(file)  #file writer
        fw.writerow(data)



def AddTransection():
    #write to CSV('Transection.csv')
    stamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    transection = v_transection.get()
    print(transection,stamp,allMenu.values())
    for m in allMenu.values():
        m.insert(0,transection) #insert transection to m.index no.0
        m.insert(1,stamp) #insert stamp to m.index no.1
        writeToCSV(m,'transection.csv')
    Reset() #clear data
        
B = ttk.Button(FB,text='Save',command=AddTransection)
B.pack(ipadx=5,ipady=10)

#History New window
def HistoryWindow(event):
    Hist = Toplevel()  #similar with GUI =Tk()
    Hist.geometry('950x500')
    L = Label(Hist,text='Order History',font=(None,15)).pack()
    
    #History
    header = ['TS-ID','Datetime','Title','Price','Quantity','Total']
    hwidth = [100,135,200,100,100,100]

    table_history = ttk.Treeview(Hist,columns = header,show='headings',height=15)
    table_history.pack()

    for hd,hw in zip(header,hwidth):
        table_history.column(hd,width=hw)
        table_history.heading(hd,text=hd)

    #Update from CSV
    with open('transection.csv', newline='',encoding='utf-8') as file:
        fr = csv.reader(file) #file reader
        for row in fr:
            table_history.insert('',0,values=row)

    Hist.mainloop()

window.bind('<F1>',HistoryWindow)

################################-TAB2-Member-############################
# def Ent(window,text,strvar,font=('Bahnschrift',15)):
#     T = Label(window,text=text,font=(None,15)).pack()
#     E = ttk.Entry(window,textvariable=strvar,font=font)
#     return E

# def Ent2(window,text,strvar,font=('Bahnschrift',15)):
#     T = Label(window,text=text,font=(None,15)) #No Pack
#     E = ttk.Entry(window,textvariable=strvar,font=font)
#     return E,T

def Ent3(window,text,font=('Bahnschrift',15)):
    V_strvar = StringVar()
    T = Label(window,text=text,font=(None,15)).pack()
    E = ttk.Entry(window,textvariable=V_strvar,font=font,justify='center')
    return E,T,V_strvar


# v_fullName = StringVar
# E21 = Ent(T2,'Full Name',v_fullName)
# E21.place(x=300,y=50)

# v_tel = StringVar
# E22,L = Ent2(T2,'Telephone Number',v_tel)
# L.place(x=50,y=50)
# E22.place(x=50,y=100)

F21 = Frame(T2)   #Frame  on the tab no.2
F21.place(x=50,y=50)

v_membercode = StringVar()
v_membercode.set('M-1001')
L = Label(T2,text='Member ID',font=(None,10)).place(x=50,y=20)
LCode = Label(T2,textvariable=v_membercode,font=(None,13)).place(x=150,y=20)


E21,L,v_fullname = Ent3(F21,'Full Name')
E21.pack() 

E22,L,v_tel = Ent3(F21,'Tel. Number')
E22.pack()

E23,L,v_userType =Ent3(F21,'Member Type')
E23.pack()
v_userType.set('General')

E24,L,v_points =Ent3(F21,'Points')
E24.pack()
v_points.set('0')  #insert a defualt data of points 


def SaveMember():
    code = v_membercode.get()
    fullName = v_fullname.get()
    tel = v_tel.get()
    userType = v_userType.get()
    points = v_points.get()
    print(fullName,tel,userType,points)
    writeToCSV([code,fullName,tel,userType,points],'member.csv')  # save a member
    table_member.insert('',0,value=[code,fullName,tel,userType,points])


# E23.bind('<Return>',lambda x: print(v_userType.get()))
B = ttk.Button(F21,text='Save',command=SaveMember)
B.pack()


###########--Table for member showing--############
F21= Frame(T2)
F21.place(x=700,y=100) # position

header = ['Code','Name','Tel','Memer Type','Points']
hwidth = [50,200,100,100,100]

table_member = ttk.Treeview(F21,columns = header,show='headings',height=15)
table_member.pack()

for hd,hw in zip(header,hwidth):
    table_member.column(hd,width=hw)
    table_member.heading(hd,text=hd)


# Delete data in the selected table

def DeleteMember(event):
    select = table_member.selection() #select item
    data = table_member.item(select)['values']
    print(data)

table_member.bind('<Delete>',DeleteMember)

#Update Table

allMember ={}


def UpdateTable_Member():
    #Update from CSV
    with open('member.csv', newline='',encoding='utf-8') as file:
        fr = csv.reader(file) #file reader
        table_member.delete(*table_member.get_children())
        for row in fr:
            table_member.insert('',0,values=row)
            code = row[0] #get 
            allMember[code] = row
    print(allMember)



UpdateTable_Member()

window.mainloop()
