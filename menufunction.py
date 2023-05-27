from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from productdb import *
class Addmember:
    def __init__(self):
        self.v_productid = None
        self.v_title = None
        self.v_price = None
        self.v_imagepath = None
        
    def popup(self):
        MGUI = Toplevel()
        MGUI.geometry('500x600')
        MGUI.title('Add Product')
        
        self.v_productid = StringVar()
        self.v_title = StringVar()
        self.v_price = StringVar()
        self.v_imagepath = StringVar()
        
        L = Label(MGUI,text='Add product',font=(None,30))
        L.pack(pady=20)
        
        L = Label(MGUI,text='Product ID',font=(None,20)).pack()
        E1 = ttk.Entry(MGUI,textvariable=self.v_productid,font=(None,20))
        E1.pack(pady=10)
        
        L = Label(MGUI,text='Product Name',font=(None,20)).pack()
        E2 = ttk.Entry(MGUI,textvariable=self.v_title,font=(None,20))
        E2.pack(pady=10)
        
        L = Label(MGUI,text='Price',font=(None,20)).pack()
        E3 = ttk.Entry(MGUI,textvariable=self.v_price,font=(None,20))
        E3.pack(pady=10)
        
        L = Label(MGUI,textvariable=self.v_imagepath).pack()
        
        Bselect = ttk.Button(MGUI,text='Picture select ( 50 x 50 px)',command=self.selectfile)
        Bselect.pack(pady=10)
        
        Bsave = ttk.Button(MGUI,text='Save',command=self.saveproduct)
        Bsave.pack(pady=10,ipadx=20,ipady=10)
        
        
        
        MGUI.mainloop()
        
    def selectfile(self):
        filetypes = (
                ('PNG','*.png'),
                ('All files','*.*')
            )
        select = filedialog.askopenfilename(title='Picture select file',initialdir='/',filetypes=filetypes)
        self.v_imagepath.set(select)
        
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
    test = Addmember()
        
