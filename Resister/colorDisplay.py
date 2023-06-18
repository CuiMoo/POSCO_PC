from tkinter import *
from tkinter import ttk,messagebox


class colorDisplay():
    def __init__(self,frame):
        self.bodyColor ='#e6aa5c'
        self.colorList = {'black':{'color':'black','value':'0','power':1},
                          'brown':{'color':'saddlebrown','value':'1','power':10},
                          'red':{'color':'red','value':'2','power':100},
                          'orange':{'color':'dark orange','value':'3','power':1_000},
                          'yellow':{'color':'yellow','value':'4','power':10_000},
                          'green':{'color':'green','value':'5','power':100_000},
                          'blue':{'color':'blue','value':'6','power':1_000_000},
                          'violet':{'color':'dark violet','value':'7','power':10_000_000},
                          'grey':{'color':'grey','value':'8','power':100_000_000},
                          'white':{'color':'white','value':'9','power':1_000_000_000},
                          }
        
        self.colorTolerance ={'brown':{'color':'saddlebrown','tolerance':0.01},
                             'red':{'color':'red','tolerance':0.02},
                             'green':{'color':'green','tolerance':0.005},
                             'blue':{'color':'blue','tolerance':0.0025},
                             'violet':{'color':'dark violet','tolerance':0.001},
                             'gold':{'color':'#FFD700','tolerance':0.05},
                             'silver':{'color':'#C0C0C0','tolerance':0.1},
                             'none':{'color':self.bodyColor,'tolerance':0.2},
                             }
        
        self.colorUse = [self.colorList['brown']['color'],self.colorList['black']['color'],
                         self.colorList['red']['color'],self.colorTolerance['gold']['color']]
        #create button dict for store button list
        self.buttonList ={}        

        self.canvas = Canvas(frame,width=500,height=100)
        self.canvas.pack(pady=10)

        #resistor leg
        self.canvas.create_polygon([0,40,500,40,500,60,0,60],fill='grey',outline='white')

        #resistor body
        self.canvas.create_polygon([100,0,400,0,400,100,100,100],fill=self.bodyColor)
        
        #--------color choosing tab frame--------------------#
        self.colorChooseTab = Frame(frame,width=500,height=50)
        self.colorChooseTab.place(x=250,y=400)
        
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
        self.canvas.create_polygon([150,0,175,0,175,100,150,100],fill=self.colorUse[0])
        #color2
        self.canvas.create_polygon([200,0,225,0,225,100,200,100],fill=self.colorUse[1])
        #color3
        self.canvas.create_polygon([250,0,275,0,275,100,250,100],fill=self.colorUse[2])
        #color4
        self.canvas.create_polygon([325,0,350,0,350,100,325,100],fill=self.colorUse[3])
    
    def clearButton(self):
        for b in self.buttonList.values():
            b['button'].grid_forget()
        
    
    def colorButtonCreate(self,frame,number):

        if number !='4':
            for i,v in enumerate(self.colorList.values()):
                B = Button(frame,text=number,bg=v['color'])
                self.buttonList[v['color']] ={'button':B,'column':i}
                B.configure(command= lambda C=v,number=number: self.colorTabSelect(C,number))
                B.grid(row=0,column=i,padx=12,ipadx=6)
            
        else:
            for i,v in enumerate(self.colorTolerance.values()):
                B = Button(frame,text=number,bg=v['color'])
                self.buttonList[v['color']] ={'button':B,'column':i}
                B.configure(command= lambda C=v,number=number: self.colorTabSelect(C,number))
                B.grid(row=0,column=i,padx=12,ipadx=6)
        print(self.buttonList)        

        
    def colorSelect(self,number=''):
        self.colorChooseTab.place_forget()
        self.colorChooseTab.place(x=250,y=400)
        self.clearButton()
        self.colorButtonCreate(self.colorChooseTab,number)

        
    def colorTabSelect(self,color='',number=''):
        print(color['color'])
        n = int(number)-1
        self.colorUse[n] =color['color']
        print('color: ',self.colorUse)
        self.colorDraw()
        self.colorButtonDraw()

        #clear colorChooseTab for diapearance       
        self.colorChooseTab.place_forget()


    def colorButtonDraw(self):
        self.colorButtonMenu(self.colorChooseMenu)
        
        
    
    
    

        
       
# if __name__ == '__main__':
#     test = colorDisplay()

