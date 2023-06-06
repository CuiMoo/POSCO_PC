from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from productdb import *


class ProductIcon:
    def __init__(self):
        self.quantity = None
        self.table_product = None
        self.v_radio = None
        
    def popup(self):
        #PGUI = Product GUI
        PGUI = Toplevel()
        PGUI.geometry('500x500')
        PGUI.title('Setting ---> Show product item icon')
        
        header = ['ID','Item code', 'Item title', 'Icon']
        hwidth = [50,70,200,70]

        self.table_product = ttk.Treeview(PGUI,columns=header, show='headings',height=15)
        self.table_product.pack()

        for hd,hw in zip(header,hwidth):
            self.table_product.column(hd,width=hw)
            self.table_product.heading(hd,text=hd)
        
        self.table_product.bind('<Double-1>',self.change_status)
        self.insert_table()    
        PGUI.mainloop()
        
    def insert_table(self):
        self.table_product.delete(*self.table_product.get_children()) 
        data = View_product_table_icon()
        print(data)
        for d in data:
            row = list(d) #convert tuple to list for data editting               
            check = View_product_status(row[0])
            #Show status of showing symbol
            if check[-1] == 'show':
                row.append('✔')
            self.table_product.insert('','end',value=row)
            
    def change_status(self,event=None):
        select = self.table_product.selection()
        pid = self.table_product.item(select)['values'][0]
        # print('PID:',pid)
        SGUI = Toplevel() #SGUI = status GUI
        SGUI.geometry('400x100')
        self.v_radio = StringVar()
        #radio button
        RB1 = ttk.Radiobutton(SGUI,text= 'Show icon',variable=self.v_radio,value='show',
                              command=lambda x=None: insert_product_status(int(pid),'show'))
        RB1.pack(pady=20)
        RB2 = ttk.Radiobutton(SGUI,text='No showing',variable=self.v_radio,value='',
                              command=lambda x=None: insert_product_status(int(pid),''))
        RB2.pack()
        # RB1.invoke() #set defualt of radio
        check = View_product_status(pid)
        print('CHECK:',check)
        if check[-1] == 'show':
            RB1.invoke()
        else:
            RB2.invoke()
        
        # Drop down
        # dropdown = ttk.Combobox(SGUI,values=['Show icon','No showing'])
        # dropdown.pack()
        # dropdown.set('Show icon')
        # dropdown.bind('<<ComboboxSelected>>',lambda x =None: print(dropdown.get()))
        def check_close():
            print('closed')
            SGUI.destroy()  #close popup window
            self.insert_table()
        SGUI.protocol('WM_DELETE_WINDOW',check_close)
        SGUI.mainloop()
    
    def command(self):
        self.popup()





class AddProduct:
    def __init__(self):
        self.v_productid = None
        self.v_title = None
        self.v_price = None
        self.v_imagepath = None
        self.MGUI = None
        
    def popup(self):
        self.MGUI = Toplevel()
        self.MGUI.geometry('500x600')
        self.MGUI.title('Add Product')
        
        self.v_productid = StringVar()
        self.v_title = StringVar()
        self.v_price = StringVar()
        self.v_imagepath = StringVar()
        
        L = Label(self.MGUI,text='Add product',font=(None,30))
        L.pack(pady=20)
        
        L = Label(self.MGUI,text='Product ID',font=(None,20)).pack()
        E1 = ttk.Entry(self.MGUI,textvariable=self.v_productid,font=(None,20))
        E1.pack(pady=10)
        
        L = Label(self.MGUI,text='Product Name',font=(None,20)).pack()
        E2 = ttk.Entry(self.MGUI,textvariable=self.v_title,font=(None,20))
        E2.pack(pady=10)
        
        L = Label(self.MGUI,text='Price',font=(None,20)).pack()
        E3 = ttk.Entry(self.MGUI,textvariable=self.v_price,font=(None,20))
        E3.pack(pady=10)
        
        L = Label(self.MGUI,textvariable=self.v_imagepath).pack()
        
        Bselect = ttk.Button(self.MGUI,text='Picture select ( 50 x 50 px)',command=self.selectfile)
        Bselect.pack(pady=10)
        
        Bsave = ttk.Button(self.MGUI,text='Save',command=self.saveproduct)
        Bsave.pack(pady=10,ipadx=20,ipady=10)
        
        
        
        self.MGUI.mainloop()
        
    def selectfile(self):
        #self.MGUI.lift()
        filetypes = (
                ('PNG','*.png'),
                ('All files','*.*')
            )
        select = filedialog.askopenfilename(title='Picture select file',initialdir='/',filetypes=filetypes)
        self.v_imagepath.set(select)
        self.MGUI.focus_force()  #after select the add product page path then freez the window above on main window
        self.MGUI.grab_set() # same as above
        
    def saveproduct(self):
        v1 = self.v_productid.get()
        v2 = self.v_title.get()
        v3 = float(self.v_price.get())
        v4 = self.v_imagepath.get()
        Insert_product(v1,v2,v3,v4)
        self.v_productid.set('')
        self.v_title.set('')
        self.v_price.set('')
        self.v_imagepath.set('')
        View_product()
        
    
    def command(self):
        self.popup()
        
if __name__ =='__main__':
    test = AddProduct()
        