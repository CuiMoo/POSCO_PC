import snap7
from snap7 import util
import time
import csv
import os
import pandas as pd


UtilityIP = '192.168.0.10'   
RACK = 0
MODULE = 3



class UtilityPLC:
    def __init__(self) -> None:
        try:
            self.plc = snap7.client.Client()
            self.plc.connect(UtilityIP,RACK,MODULE)  # IP PLC set
            self.plc.get_connected()   #Connect
        except:
            pass

    def dataCollect(self):
        boilerA_NG = self.plc.db_read(1037,112,4)               #DB1037.DBD112 GET READ
        boilerA_NG_flow  = util.get_real(boilerA_NG,0)          #BOILER A NG FLOW

        boilerB_NG = self.plc.db_read(1038,112,4)               #DB1038.DBD112 GET READ
        boilerB_NG_flow  = util.get_real(boilerB_NG,0)          #BOILER B NG FLOW

        furNG = self.plc.db_read(1003,1600,4)                   #DB1003.DBD1600 Get read                              
        furNG_flow = util.get_real(furNG,0)                     #Furnace Flow
               

        N2 = self.plc.db_read(1003,15000,4)                     #DB1003.DBD15000 GET READ
        N2_Flow = util.get_real(N2,0)                           #N2 FLOW

        H2 = self.plc.db_read(1003,15100,4)                     #DB1003.DBD112 GET READ
        H2_Flow = util.get_real(H2,0)                           #H2 FLOW



        return boilerA_NG_flow,boilerB_NG_flow,furNG_flow,N2_Flow,H2_Flow
    

    
    def writeToCSV(self,data,Date):
        Year = Date[0]
        Month = Date[1]
        Day = Date[2]
        Hr = Date[3]
        

        fileName1 = self.mkDir(Year,Month,Day,Hr)
        fileName2 = fileName1+ '.csv'

        #Insert or create CSV file 
        with open(fileName2,'a',newline='',encoding='utf-8') as file:
            fw = csv.writer(file) # fw = file writer
            fw.writerow(data)
            # print(f'recorded at {Month}/{Day}, Hr:{Hr}')
        try:
            self.csvToExcel(fileName1)
        except:
            print('the exel file is openned!')


    def mkDir(self,Y,M,D,H):
        folderName = 'C:/Utility Record'
        #folderName = 'C:/test1'
        dir_list = os.listdir(folderName)
        header = ('Date','Time','NG-1','NG-2','Fce-NG','N2','H2','Test(60)')

        if str(Y) not in dir_list:
            pathF = os.path.join(folderName,str(Y))
            os.mkdir(pathF)
            path_Y = folderName + '/' + str(Y)
            path = path_Y+'/'+str(M)+'.csv'
            
            with open(path,'a',newline='',encoding='utf-8') as file:
                fw = csv.writer(file) # fw = file writer
                fw.writerow(header)
                
        path_Y = folderName + '/' + str(Y)
        path = path_Y+'/'+str(M)

        #Create separated folders by Y-M-D
        """
        dir_list_Y = os.listdir(path_Y)
        if str(M) not in dir_list_Y:
            pathFM = os.path.join(path_Y,str(M))
            os.mkdir(pathFM)

            path_M1 = path_Y + '/' + str(M) + '/' + str(D) +'.csv'
            
            #Add the header into the first column of the file.
            with open(path_M1,'a',newline='',encoding='utf-8') as file:
                fw = csv.writer(file) # fw = file writer
                fw.writerow(header)
                
                
        path_M = path_Y + '/' + str(M) + '/' + str(D) +'.csv'
        """
        if D == '01' and H =='00' :
            with open((path+'.csv'),'a',newline='',encoding='utf-8') as file:
                fw = csv.writer(file) # fw = file writer
                fw.writerow(header)

        return path
                    

    def csvToExcel(self,FileName):
        cFile = FileName + '.csv'
        df = pd.read_csv(cFile)
        xFile = FileName+'.xlsx'
        df.to_excel(xFile,sheet_name='consumption',index=False)

    
if __name__ == '__main__':
    oRun = UtilityPLC()

    while True:
        dataShow = oRun.dataCollect()
        time.sleep(1)