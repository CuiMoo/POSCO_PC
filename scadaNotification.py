import pymcprotocol
import time
import requests
import schedule
from datetime import datetime
import threading

#---PLC CONFIGURATION---#
SCADA_IP = '192.168.1.5'
PORT = 2001
COMTYPE = 'binary'
Line_Token = 'xxxxx' # Token 


class SCADA:
    def __init__(self):
        try:
            self.pymc3e = pymcprotocol.Type3E()
            self.pymc3e.setaccessopt(commtype=COMTYPE)
            self.pymc3e.connect(ip=SCADA_IP,port=PORT)
            if self.pymc3e._is_connected:
                self.cpu_type, self.cpu_code = self.pymc3e.read_cputype()
                print(self.cpu_type,self.cpu_code)


        except:
            pass

        self.Line_Token = Line_Token  
        self.Line_url = 'https://notify-api.line.me/api/notify'
        self.headers = {'content-type':'application/x-www-form-urlencoded','Authorization':'Bearer '+self.Line_Token}

    def LineSpeed_Read(self):
        Lines_Speed = self.pymc3e.batchread_wordunits(headdevice='D5315',readsize=4)
        return Lines_Speed  #Lines_Speed = [entry,center-1,center-2,delivery]

    def Incomming_Volt(self):
        Incoming_Data = self.pymc3e.batchread_wordunits(headdevice='D4514',readsize=3)
        GIS_Volt = Incoming_Data[0]
        HV_10 = Incoming_Data[1]/1000
        PF = Incoming_Data[2]/100
        return GIS_Volt,HV_10,PF
    
    def HV10_Fualt(self):  #Incomming
        Logs = self.pymc3e.batchread_bitunits(headdevice='X0A7',readsize=7)
        HV_10_OCGR = Logs[0]
        HV_10_OCR  = Logs[1]
        HV_10_OVGR = Logs[2]
        HV_10_OVR = Logs[3]
        HV_10_UVR = Logs[6]
        return HV_10_OCGR,HV_10_OCR,HV_10_OVGR,HV_10_OVR,HV_10_UVR


    def Send_Line(self,data):
        try:
            session = requests.Session()
            text = {'message':data}
            session.post(self.Line_url,headers=self.headers,data=text)
        except:
            print('Line Sending Error')



class FactoryEvent:
    def __init__(self):
        self.Scada = SCADA()

    def Hourly_inform(self):
        Line_Speed = self.Scada.LineSpeed_Read()
        GIS_volt,HV_10_Volt,PF = self.Scada.Incomming_Volt()
        Time = datetime.now().strftime('[%Y/%m/%d] [%H:%M]')

        LineStatus_text = f'\n{Time}\n-------------\nEntry: {Line_Speed[0]} mpm\nCenter-1: {Line_Speed[1]} mpm\nCenter-2: {Line_Speed[2]}mpm\nDelivery: {Line_Speed[3]} mpm\n-------------\nGIS: {GIS_volt} kV\nHV-10: {HV_10_Volt} kV\nPF: {PF}\n-------------'
        
        self.Scada.Send_Line(LineStatus_text)

    def Routine_RunTime(self):
        Event_time = ['08:00','12:00','17:00','20:00','00:00','05:00']
        
        for T in Event_time:
            schedule.every().day.at(T).do(self.Hourly_inform)
       
        while True:
            schedule.run_pending()
            time.sleep(0.5)

    def Line_Issue(self):
        HV_10_OCGR_sent = False
        HV_10_OCR_sent = False
        HV_10_OVGR_sent = False
        HV_10_OVR_sent = False
        HV_10_UVR_sent = False
        Line_speed_sent = False
        
        while True:
            
            HV_10_OCGR,HV_10_OCR,HV_10_OVGR,HV_10_OVR,HV_10_UVR = self.Scada.HV10_Fualt()
            Line_Speed = self.Scada.LineSpeed_Read()
            
            #----OCGR---#
            if HV_10_OCGR and not HV_10_OCGR_sent:
                self.Scada.Send_Line('HV-10: OCGR Fault')
                HV_10_OCGR_sent = True
            
            elif not HV_10_OCGR and HV_10_OCGR_sent:
                self.Scada.Send_Line('HV-10: OCGR Recovery')
                HV_10_OCGR_sent = False
            

            #----OCR---#    
            if HV_10_OCR and not HV_10_OCR_sent:
                self.Scada.Send_Line('HV-10: OCR Fault')
                HV_10_OCR_sent = True
                
            elif not HV_10_OCR and HV_10_OCR_sent:
                self.Scada.Send_Line('HV-10: OCGR Recovery')
                HV_10_OCR_sent = False
            
            
            #---OVGR---#
            if HV_10_OVGR and not HV_10_OVGR_sent:
                self.Scada.Send_Line('HV-10: OVGR Fault')
                HV_10_OVGR_sent = False
                
            elif not HV_10_OVGR and HV_10_OVGR_sent:
                self.Scada.Send_Line('HV-10: OVGR Recovery')
                HV_10_OVGR_sent = False
                
            #---OVR---#
            if HV_10_OVR and not HV_10_OVR_sent:
                self.Scada.Send_Line('HV-10: OVR Fault')
                HV_10_OVR_sent = True
                
            elif not HV_10_OVR and HV_10_OVR_sent:
                self.Scada.Send_Line('HV-10: OVR Recovery')
                HV_10_OVR_sent = False
            
            #---UVR---#
            if HV_10_UVR and not HV_10_UVR_sent:
                self.Scada.Send_Line('HV-10: UVR Fault')
                HV_10_UVR_sent = True
                
            elif not HV_10_UVR and HV_10_UVR_sent:
                self.Scada.Send_Line('HV-10: UVR Recovey')
                HV_10_UVR_sent = False
                
            #---Center-1 Speed Abnormal---# 
            if Line_Speed[1] <= 1 and not Line_speed_sent:
                self.Scada.Send_Line('Line Trouble/Stop!!\nCall k.Dave&Max')
                Line_speed_sent = True
            
            elif not Line_Speed[1] <=5 and Line_speed_sent:
                self.Scada.Send_Line('Line Start!!')
                Line_speed_sent = False 
                                
            time.sleep(1)
            
    def scanTime(self):
        Job1 = threading.Thread(target=self.Routine_RunTime)
        Job2 = threading.Thread(target=self.Line_Issue)
        Job1.start()
        Job2.start()
        Job1.join()
        Job2.join()
        
                
                   
if __name__ == '__main__':
    Line_Event = FactoryEvent()
    Line_Event.scanTime()

        

        
    
