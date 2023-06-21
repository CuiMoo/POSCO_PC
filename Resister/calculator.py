from tkinter import *
from colorDisplay import *

class Calculator:
    def __init__(self):
        self.colorList = {'black':{'color':'black','show':'black','value':0,'power':1},
                          'brown':{'color':'brown','show':'saddlebrown','value':1,'power':10},
                          'red':{'color':'red','show':'red','value':2,'power':100},
                          'orange':{'color':'orange','show':'dark orange','value':3,'power':1_000},
                          'yellow':{'color':'yellow','show':'yellow','value':4,'power':10_000},
                          'green':{'color':'green','show':'green','value':5,'power':100_000},
                          'blue':{'color':'blue','show':'blue','value':6,'power':1_000_000},
                          'violet':{'color':'violet','show':'dark violet','value':7,'power':10_000_000},
                          'grey':{'color':'grey','show':'grey','value':8,'power':100_000_000},
                          'white':{'color':'white','show':'white','value':9,'power':1_000_000_000},
                          }
        
        self.colorTolerance ={'brown':{'color':'brown','show':'saddlebrown','tolerance':1},
                             'red':{'color':'red','show':'red','tolerance':2},
                             'green':{'color':'green','show':'green','tolerance':0.005},
                             'blue':{'color':'blue','show':'blue','tolerance':0.0025},
                             'violet':{'color':'violet','show':'dark violet','tolerance':0.001},
                             'gold':{'color':'gold','show':'#FFD700','tolerance':0.05},
                             'silver':{'color':'silver','show':'#C0C0C0','tolerance':0.1},
                             'none':{'color':'none','show':'#e6aa5c','tolerance':0.2},
                             }
    

    def findColorKey(self,dictList,name,value):
        for key,val in dictList.items():
            if val[name] == value:
                return key


    def colorToData(self,Color):
        Color = Color
        ColorData = []
        for i in Color[:3]:
            ColorData.append(self.findColorKey(self.colorList,'show',i))
        ColorData.append(self.findColorKey(self.colorTolerance,'show',Color[3]))
        
        resistance = (self.colorList[ColorData[0]]['value']*10+ float(self.colorList[ColorData[1]]['value'])) * (self.colorList[ColorData[2]]['power'])
        #resistance = self.colorList[ColorData[0]]['value'] 
        #+(self.colorList[ColorData[1]]['value'])*0.1    *    (self.colorList[ColorData[2]]['power'])
        tolerance = self.colorTolerance[ColorData[3]]['tolerance']
        print(f'{resistance}tolerance: {tolerance}%')
        
        

# if __name__ =='__main__':
#     oCalculator =Calculator()
#     print(oCalculator.colorList)