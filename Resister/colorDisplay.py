from tkinter import *
from tkinter import ttk,messagebox


class colorDisplay():
    def __init__(self,frame):
        self.colorList = {'black':{'color':'black','value':'0','power':1},
                          'brown':{'color':'brown','value':'1','power':10},
                          'red':{'color':'red','value':'2','power':100},
                          'orange':{'color':'orange','value':'3','power':1_000},
                          'yellow':{'color':'yellow','value':'4','power':10_000},
                          'green':{'color':'green','value':'5','power':100_000},
                          'blue':{'color':'blue','value':'6','power':1_000_000},
                          'violet':{'color':'dark violet','value':'7','power':10_000_000},
                          'grey':{'color':'grey','value':'8','power':100_000_000},
                          'white':{'color':'white','value':'9','power':1_000_000_000},
                          }
        self.colorUse = ['red','red','orange','yellow']        

        self.canvas = Canvas(frame,width=500,height=300)
        self.canvas.pack(pady=10)
        #resistor leg
        self.canvas.create_polygon([0,240,500,240,500,260,0,260],fill='grey',outline='white')
        #resistor body
        self.canvas.create_polygon([100,200,400,200,400,300,100,300],fill='#e8be64')
        
                #--------color choosing tab frame--------------------#
        self.colorChooseTab = Frame(frame,width=500,height=50)
        self.colorChooseTab.place(x=250,y=500)
        
        #--------color choosing menu frame--------------------#
        self.colorChooseMenu = Frame(frame,width=500,height=50)
        self.colorChooseMenu.pack()
   
    def colorButtonMenu(self,frame):
        Bc1 = Button(frame ,text='1',bg=self.colorUse[0],command=lambda x='1':self.colorSelect(x))
        Bc1.grid(row=0,column=0,padx=12,ipadx=6)
        Bc2 = Button(frame ,text='2',bg=self.colorUse[1],command=lambda x='2':self.colorSelect(x))
        Bc2.grid(row=0,column=1,padx=12,ipadx=6)
        Bc3 = Button(frame ,text='3',bg=self.colorUse[2],command=lambda x='3':self.colorSelect(x))
        Bc3.grid(row=0,column=2,padx=12,ipadx=6)
        Bc4 = Button(frame ,text='4',bg=self.colorUse[3],command=lambda x='4':self.colorSelect(x))
        Bc4.grid(row=0,column=3,padx=40,ipadx=6)
    
    
    def colorDraw(self):            
        #color1
        self.canvas.create_polygon([150,200,175,200,175,300,150,300],fill=self.colorUse[0])
        #color2
        self.canvas.create_polygon([200,200,225,200,225,300,200,300],fill=self.colorUse[1])
        #color3
        self.canvas.create_polygon([250,200,275,200,275,300,250,300],fill=self.colorUse[2])
        #color4
        self.canvas.create_polygon([325,200,350,200,350,300,325,300],fill=self.colorUse[3])
        
    
    def colorChoosingMenu(self,frame,number):
        for i,v in enumerate(self.colorList.values()):
            B = Button(frame,text='',bg=v['color'])
            B.configure(command= lambda C=v,number=number: self.colorTabSelect(C,number))
            B.grid(row=0,column=i,padx=12,ipadx=6)
            
    
    def colorButtonDraw(self):
        self.colorButtonMenu(self.colorChooseMenu)
        
    def colorSelect(self,number=''):
        self.colorChooseTab.place(x=250,y=500)
        self.colorChoosingMenu(self.colorChooseTab,number)

        
    def colorTabSelect(self,color='',number=''):
        print(color['color'])
        n = int(number)-1
        self.colorUse[n] =color['color']
        print('color: ',self.colorUse)
        self.colorDraw()
        self.colorButtonDraw()
        
        
        self.colorChooseTab.place_forget()
        
        
    
    
    

        
       
# if __name__ == '__main__':
#     test = colorDisplay()