from tkinter import *
from colorDisplay import *

class Calculator:
    def __init__(self):
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
    
    def colorToRealColor(self,color):
        for i,c in enumerate(color):
            Color = color
            if c == self.colorList['brown']['color']:
                Color[i] = 'brown'
            elif c == self.colorList['orange']['color']:
                Color[i]= 'orange'
            elif c == self.colorList['violet']['color']:
                Color[i] = 'violet'
            elif c== self.colorTolerance['gold']['color']:
                Color[i] = 'gold'
            elif c == self.colorTolerance['silver']['color']:
                Color[i] = 'silver'
            elif c == self.colorTolerance['none']['color']:
                Color[i] = 'none'
        print(Color)
        return Color
    def colorToData(self,Color):
        colorConvert = self.colorToRealColor(Color)
        # sign1=self.colorList[colorConvert[0]]['value']
        # sign2=self.colorList[colorConvert[1]]['value']
        # power=self.colorList[colorConvert[2]]['power']
        # tolerance=self.colorTolerance[colorConvert[3]]['power']
        # print(sign1,sign2,power,tolerance)
        print('convertdata',colorConvert)

# if __name__ =='__main__':
#     oCalculator =Calculator()
#     print(oCalculator.colorList)