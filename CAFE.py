from tkinter import *
from tkinter import ttk, messagebox



window = Tk()
window.title('CUIMOO\'S COFFEE')
window.geometry('1500x750')


#Tab setting
tab = ttk.Notebook(window)
tab.pack(fill=BOTH,expand=1)

#font setting
Bfont = ttk.Style()  
Bfont.configure('TButton',font=('AR BERKLEY',15))

T1 = Frame(tab)


icon_tab1 = PhotoImage(file='C:/Python310/learning_by_my_self/tkinter/CAFE/Coffee_icon.png')
late = PhotoImage(file='C:/Python310/learning_by_my_self/tkinter/CAFE/late.png')
expresso = PhotoImage(file='C:/Python310/learning_by_my_self/tkinter/CAFE/expesso.png')
cappuccino = PhotoImage(file='C:/Python310/learning_by_my_self/tkinter/CAFE/cappuccino.png')
green_tea = PhotoImage(file='C:/Python310/learning_by_my_self/tkinter/CAFE/green_tea.png')
hot_tea = PhotoImage(file='C:/Python310/learning_by_my_self/tkinter/CAFE/hot_tea.png')
milk_tea = PhotoImage(file='C:/Python310/learning_by_my_self/tkinter/CAFE/milk_tea.png')

tab.add(T1,text='CAFE',image=icon_tab1,compound='left')


#Tab1

CF1 = Frame(T1)
CF1.place(x=50,y=100)
coffees = ['Late','Cappuccino','Espresso','Green tea','Milk Tea','Hot Tea']
coffee_icon =[late,cappuccino,expresso,green_tea,milk_tea,hot_tea]

B1 = ttk.Button(CF1,text=coffees[0],image = coffee_icon[0],compound='top')
B1.grid(row=0,column=0,ipadx=20,ipady=10)

B2 = ttk.Button(CF1,text=coffees[1],image = coffee_icon[1],compound='top')
B2.grid(row=0,column=1,ipadx=20,ipady=10)

B3 = ttk.Button(CF1,text=coffees[2],image = coffee_icon[2],compound='top')
B3.grid(row=0,column=2,ipadx=20,ipady=10) 

B4 = ttk.Button(CF1,text=coffees[3],image = coffee_icon[3],compound='top')
B4.grid(row=1,column=0,ipadx=20,ipady=10)

B5 = ttk.Button(CF1,text=coffees[4],image = coffee_icon[4],compound='top')
B5.grid(row=1,column=1,ipadx=20,ipady=10)  

B6 = ttk.Button(CF1,text=coffees[5],image = coffee_icon[5],compound='top')
B6.grid(row=1,column=2,ipadx=20,ipady=10)  




#table
CF2 = Frame(T1)
CF2.place(x=700,y=100) # position

header = ['No','Title','Price','Quantity','Total']
hwidth = [50,200,100,100,100]

table = ttk.Treeview(CF2,columns = header,show='headings',height=15)
table.pack()

for hd,hw in zip(header,hwidth):
    table.column(hd,width=hw)
    table.heading(hd,text=hd)




window.mainloop()
