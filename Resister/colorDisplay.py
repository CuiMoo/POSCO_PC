from tkinter import *
from tkinter import ttk,messagebox
from calculator import *

oCalculator = Calculator()

class colorDisplay():
    def __init__(self,frame):
        self.bodyColor ='#e6aa5c'

        self.colorList =oCalculator.colorList

        self.colorTolerance =oCalculator.colorTolerance
        self.colorUse = [self.colorList['brown']['show'],self.colorList['black']['show'],
                         self.colorList['red']['show'],self.colorTolerance['gold']['show']]
        #create button dict for store button list
        self.buttonList ={}         
        self.canvas = Canvas(frame,width=500,height=100)
        self.canvas.pack(pady=10)
        #Data box
        self.boxText = None
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
    

    def colorButtonDraw(self):
        self.colorButtonMenu(self.colorChooseMenu)

    def colorDraw(self):
        #color1
        self.canvas.create_polygon([150,0,175,0,175,100,150,100],fill=self.colorUse[0])
        #color2
        self.canvas.create_polygon([200,0,225,0,225,100,200,100],fill=self.colorUse[1])
        #color3
        self.canvas.create_polygon([250,0,275,0,275,100,250,100],fill=self.colorUse[2])
        #color4
        self.canvas.create_polygon([325,0,350,0,350,100,325,100],fill=self.colorUse[3])
    
    def DataBox(self,frame):
        self.boxText = StringVar()
        self.colorTodata(self.colorUse)
        self.showData = ttk.Entry(frame,font=(None,30),textvariable=self.boxText)
        self.showData.grid(row=0,column=0,padx=10)

    def enterButton(self,frame):
        self.enter = ttk.Button(frame,text='Enter')
        self.enter.grid(row=0,column=1,ipady=15,ipadx=20)

    def clearButton(self):
        for b in self.buttonList.values():
            b['button'].grid_forget()
        
    
    def colorButtonCreate(self,frame,number):

        if number !='4':
            for i,v in enumerate(self.colorList.values()):
                B = Button(frame,text=number,bg=v['show'])
                self.buttonList[v['color']] ={'button':B,'column':i}
                B.configure(command= lambda C=v,number=number: self.colorTabSelect(C,number))
                B.grid(row=0,column=i,padx=12,ipadx=6)
            
        else:
            for i,v in enumerate(self.colorTolerance.values()):
                B = Button(frame,text=number,bg=v['show'])
                self.buttonList[v['color']] ={'button':B,'column':i}
                B.configure(command= lambda C=v,number=number: self.colorTabSelect(C,number))
                B.grid(row=0,column=i,padx=12,ipadx=6)
        

        
    def colorSelect(self,number=''):
        self.colorChooseTab.place_forget()
        self.colorChooseTab.place(x=250,y=400)
        self.clearButton()
        self.colorButtonCreate(self.colorChooseTab,number)

        
    def colorTabSelect(self,color='',number=''):
        n = int(number)-1
        self.colorUse[n] =color['show']
        print('color: ',self.colorUse)
        self.colorDraw()
        self.colorButtonDraw()
        self.colorTodata(self.colorUse)

        #clear colorChooseTab for diapearance       
        self.colorChooseTab.place_forget()

    def colorTodata(self,color):
        resistance,tolorance,code = oCalculator.colorToData(color)
        self.boxText.set(f'{resistance} Ω ± {tolorance}% ({code})')
        print(resistance,tolorance,code)
        



 
        
              
# if __name__ == '__main__':
#     test = colorDisplay()

