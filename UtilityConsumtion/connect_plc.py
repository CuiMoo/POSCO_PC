
import snap7
from snap7 import util
import time
import csv
import os


UtilityIP = '192.168.10'
RACK = 0
MODULE = 3



class utilityPLC:
    def __init__(self) -> None:
        self.plc = snap7.client.Client()
        self.plc.connect(UtilityIP,RACK,MODULE)  # IP PLC set
        self.plc.get_connected()   #Connect



    def dataCollect(self):
        boilerA_NG = self.plc.db_read(1037,112,4)               #DB1037.DBD112 GET READ
        boilerA_NG_flow  = util.get_real(boilerA_NG,0)          #BOILER A NG FLOW

        boilerB_NG = self.plc.db_read(1038,112,4)               #DB1038.DBD112 GET READ
        boilerB_NG_flow  = util.get_real(boilerB_NG,0)          #BOILER B NG FLOW
       

        N2 = self.plc.db_read(1003,15000,4)
        N2_Flow = util.get_real(N2,0)

        H2 = self.plc.db_read(1003,15100,4)
        H2_Flow = util.get_real(H2,0)


        return (boilerA_NG_flow,boilerB_NG_flow,N2_Flow,H2_Flow)
    

    
    def writeToCSV(self,data,Date):
        Year = Date[0]
        Month = Date[1]
        Day = Date[2]
        Hr = Date[3]
        Min = Date[4]
        Sec = Date[5]

        filename = f'{Day}'

        with open(filename,'a',newline='',encoding='utf-8') as file:
            fw = csv.writer(file) # fw = file writer
            fw.writerow(data)

    def mkDir(self):
        pass


    
if __name__ == '__main__':
    oRun = utilityPLC()

    while True:
        dataShow = oRun.dataCollect()
        time.sleep(1)