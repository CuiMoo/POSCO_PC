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
        
        self.colorTolerance ={'brown':{'color':'brown','show':'saddlebrown','tolerance':1,'code':'F'},
                             'red':{'color':'red','show':'red','tolerance':2,'code':'G'},
                             'orange':{'color':'orange','show':'dark orange','tolerance':0.05,'code':'W'},
                             'yellow':{'color':'yellow','show':'yellow','tolerance':0.02,'code':'P'},
                             'green':{'color':'green','show':'green','tolerance':0.5,'code':'D'},
                             'blue':{'color':'blue','show':'blue','tolerance':0.25,'code':'C'},
                             'violet':{'color':'violet','show':'dark violet','tolerance':0.1,'code':'B'},
                             'grey':{'color':'grey','show':'grey','tolerance':0.01,'code':'L'},
                             'gold':{'color':'gold','show':'#FFD700','tolerance':5,'code':'G'},
                             'silver':{'color':'silver','show':'#C0C0C0','tolerance':10,'code':'K'},
                             'none':{'color':'none','show':'#e6aa5c','tolerance':20,'code':'M'},
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
        
        resistance = (self.colorList[ColorData[0]]['value']*10+ float(self.colorList[ColorData[1]]['value']))\
                    * (self.colorList[ColorData[2]]['power'])

        tolorance = self.colorTolerance[ColorData[3]]['tolerance']
        code = self.colorTolerance[ColorData[3]]['code']
        #print(f'{resistance}tolerance: {tolorance}% ({code})')
        return resistance,tolorance,code
        
        

# if __name__ =='__main__':
#     oCalculator =Calculator()
#     print(oCalculator.colorList)