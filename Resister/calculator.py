from colorDisplay import *
import math

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
        
        self.convertColor = {'band1':'','band2':'','band3':'','band4':'gold'}
    

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

        return resistance,tolorance,code
        
    def dataToColor(self,data):
    
        if (data/10_000_000_000)>=1:
            print(': ',data/10_000_000_000)
            self.convertColor['band3'] = 'white'
            self.convertColor['band2'] = self.findBand2(data/10_000_000_000)
            self.convertColor['band1'] = self.findBand1(data/10_000_000_000)
        elif (data /1_000_000_000)>=1:
            print(data /1_000_000_000)
            self.convertColor['band3'] = 'grey'
            self.convertColor['band2'] = self.findBand2(data/1_000_000_000)
            self.convertColor['band1'] = self.findBand1(data/1_000_000_000)
        elif (data/100_000_000)>=1:
            print(data/100_000_000)
            self.convertColor['band3'] = 'violet'
            self.convertColor['band2'] = self.findBand2(data/100_000_000)
            self.convertColor['band1'] = self.findBand1(data/100_000_000)
        elif (data/10_000_000)>=1:
            print(data/10_000_000)
            self.convertColor['band3'] = 'blue'
            self.convertColor['band2'] = self.findBand2(data/10_000_000)
            self.convertColor['band1'] = self.findBand1(data/10_000_000)            
        elif (data/1_000_000)>=1:
            print(data/1_000_000)
            self.convertColor['band3'] = 'green'
            self.convertColor['band2'] = self.findBand2(data/1_000_000)
            self.convertColor['band1'] = self.findBand1(data/1_000_000)
        elif (data/100_000)>=1:
            print(': ',data/100_000)
            self.convertColor['band3'] = 'yellow'
            self.convertColor['band2'] = self.findBand2(data/100_000)
            self.convertColor['band1'] = self.findBand1(data/100_000)
        elif (data/10_000)>=1:
            print(data/10_000)
            self.convertColor['band3'] = 'orange'
            self.convertColor['band2'] = self.findBand2(data/10_000)
            self.convertColor['band1'] = self.findBand1(data/10_000)     
        elif (data/1_000)>=1:
            print(': ',data/1_000)
            self.convertColor['band3'] = 'red'
            self.convertColor['band2'] = (self.findBand2(data/1_000))
            self.convertColor['band1'] = self.findBand1(data/1_000)
        elif (data/100)>=1:
            print(': ',data/100)
            self.convertColor['band3'] = 'brown'
            self.convertColor['band2'] = (self.findBand2(data/100))
            self.convertColor['band1'] = self.findBand1(data/100)
        else:
            print(': ',data/10)
            self.convertColor['band3'] = 'black'
            self.convertColor['band2'] = (self.findBand2(data/10))
            self.convertColor['band1'] = self.findBand1(data/10)

        return self.convertColor
    

    def findColor(self,data):
        if data == 0:
            return 'black'
        elif data == 1:
            return 'brown'
        elif data == 2:
            return 'red'
        elif data == 3:
            return 'orange'
        elif data == 4:
            return 'yellow'
        elif data == 5:
            return 'green'
        elif data == 6:
            return 'blue'
        elif data == 7:
            return 'violet'
        elif data == 8:
            return 'grey'
        elif data == 9:
            return 'white'

    def findBand2(self,data):
        data1 =data%1
        data2 = data1*10
        data4 = data2//1
        data3 = data2%1

        if data3>=0.5:
            data3 = math.ceil(data3)

        else:
            data3 = math.floor(data3)
        band2 = data4 + data3
        if band2 ==10:
            band2 =9
        print('band2: ',band2)
        return(self.findColor(band2))
        
        
    def findBand1(self,data):
        band1 = data//1
        print('band1: ',band1)
        return(self.findColor(band1))



# if __name__ =='__main__':
#     oCalculator =Calculator()
#     print(oCalculator.colorList)