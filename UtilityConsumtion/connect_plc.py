
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
        

        fileName = self.mkDir(Year,Month,Day,Hr)

        #Insert or create CSV file 
        with open(fileName,'a',newline='',encoding='utf-8') as file:
            fw = csv.writer(file) # fw = file writer
            fw.writerow(data)
            print(f'recorded at {Month},{Day},Hr:{Hr}')


    def mkDir(self,Y,M,D,H):
        folderName = 'C:/Utility Record'
        dir_list = os.listdir(folderName)

        if str(Y) not in dir_list:
            pathF = os.path.join(folderName,str(Y))
            os.mkdir(pathF)

        path_Y = folderName + '/' + str(Y)
        dir_list_Y = os.listdir(path_Y)

        header = ('Time','NG-1','NG-2','N2','H2','Test(60)')

        if str(M) not in dir_list_Y:
            pathFM = os.path.join(path_Y,str(M))
            os.mkdir(pathFM)

            path_M1 = path_Y + '/' + str(M) + '/' + str(D) +'.csv'
            
            #Add the header into the first column of the file.
            with open(path_M1,'a',newline='',encoding='utf-8') as file:
                fw = csv.writer(file) # fw = file writer
                fw.writerow(header)
                
                
        path_M = path_Y + '/' + str(M) + '/' + str(D) +'.csv'

        if H == '00' :
            with open(path_M,'a',newline='',encoding='utf-8') as file:
                fw = csv.writer(file) # fw = file writer
                fw.writerow(header)


        return path_M
                    
    
if __name__ == '__main__':
    oRun = utilityPLC()

    while True:
        dataShow = oRun.dataCollect()
        time.sleep(1)