import pymcprotocol
import time
import requests
import schedule
from datetime import datetime

#---PLC CONFIGURATION---#
SCADA_IP = '192.168.1.5'
PORT = 2001
COMTYPE = 'binary'
#---LINE SETTING---#
LINE_TOKEN = 'HG24FTEBSGTcPAb4AnrEkPOLeAx5evRpYIrQ1vryiWj' #Moo's Token (Name:Myung)
#-----------------------#
Event_time = ['08:00','12:00','17:00','20:00','00:00','05:00'] # Time to report

#------Telegram---Setting--#
TELE_TOKEN = '8098237803:AAEh49Oh1eInH2NCZj4TtTBmtjNIF9aXa8E' #EIC's Telegram setting
TELE_CHATID = '-1002448948486'


#---VAMP-Address---# 
VAMP_ADDR = {'HV-10':'X0A7',
             'LV-06':'X0B0',
             'LV-07':'X023D',
             'LV-08':'X0244',
             'UHV-01':'X026C',
             'UHV-02':'X0273',
             'UHV-03':'X027A',
             'UHV-04':'X0281',
             'UHV-05':'X0288',
             'UHV-06':'X028F',
             'UHV-07':'X0296'             
             }

class SCADA:
    def __init__(self):
        try:
            self.pymc3e = pymcprotocol.Type3E()
            self.pymc3e.setaccessopt(commtype=COMTYPE)
            self.pymc3e.connect(ip=SCADA_IP,port=PORT)
            if self.pymc3e._is_connected:
                self.cpu_type, self.cpu_code = self.pymc3e.read_cputype()
                print(self.cpu_type,self.cpu_code,': connected')


        except:
            print('Connection is failure')

        self.Line_Token = LINE_TOKEN  
        self.Line_url = 'https://notify-api.line.me/api/notify'
        self.headers = {'content-type':'application/x-www-form-urlencoded','Authorization':'Bearer '+self.Line_Token}

        self.TELE_Token = TELE_TOKEN
        self.TELE_ID = TELE_CHATID
        self.TELE_URL = f'https://api.telegram.org/bot{self.TELE_Token}/sendMessage'
        
    def LineSpeed_Read(self):
        try:
            Lines_Speed = self.pymc3e.batchread_wordunits(headdevice='D5315',readsize=4)
            return Lines_Speed  #Lines_Speed = (entry,center-1,center-2,delivery)
        except:
            return None

    def Incomming(self):
        try:
            Incoming_Data = self.pymc3e.batchread_wordunits(headdevice='D4514',readsize=3)
            GIS_Volt = Incoming_Data[0]
            HV_10 = Incoming_Data[1]/1000
            PF = Incoming_Data[2]/100
            Power = self.pymc3e.batchread_wordunits(headdevice='D4706',readsize=1)
            Energy = self.pymc3e.batchread_wordunits(headdevice='D4717',readsize=2)
            converted_energy = round(((Energy[0]*2147483647)/3276700)/1000)                
            return GIS_Volt,HV_10,PF,Power[0],converted_energy
        except:
            return 0,0,0,0,0
        
    def VAMP_Fault(self,ADDR):
        try:
            Logs = self.pymc3e.batchread_bitunits(headdevice=ADDR,readsize=7)
            OCGR = Logs[0]
            OCR = Logs[1]
            OVGR = Logs[2]
            OVR = Logs[3]
            UVR = Logs[6]
            return OCGR,OCR,OVGR,OVR,UVR
        except:
            return 0,0,0,0,0
    

    def Generator(self):
        try:
            Logs = self.pymc3e.batchread_bitunits(headdevice='X23B',readsize=2)
            Gen1_Run = Logs[0]
            Gen2_Run = Logs[1]
            return Gen1_Run,Gen2_Run
        except:
            return 0,0
        
    def Com_Converters(self):
        try:
            CONVERTERS = self.pymc3e.batchread_bitunits(headdevice='X22F',readsize=2) #ACB status
            CONV_I = self.pymc3e.batchread_wordunits(headdevice='D4517',readsize=2)  # Current of converters
            CONV1 = CONVERTERS[0] #LV13
            CONV2 = CONVERTERS[1] #LV14
            CONV1_I = CONV_I[0] #LV13 current
            CONV2_I = CONV_I[1] #LV14 current
            return CONV1,CONV2,CONV1_I,CONV2_I
        except:
            return 0,0,0,0
        
    def CONDENSER(self):
        try:
            CS = self.pymc3e.batchread_bitunits(headdevice='X080',readsize=5)
            CS1 = CS[0] #X80 
            CS2 = CS[2] #X82
            CS3 = CS[4] #X84
            if CS1:
                C1 = 'ON'
            else:
                C1 = 'OFF'
            
            if CS2:
                C2 = 'ON'
            else:
                C2 = 'OFF'
            
            if CS3:
                C3 = 'ON'
            else:
                C3 = 'OFF'
            return C1,C2,C3
        except:
            return None,None,None
            
        
    def Send_Line(self,data):
        try:
            session = requests.Session()
            text = {'message':data}
            session.post(self.Line_url,headers=self.headers,data=text)
        except:
            print('Line Sending Error')
            
            
    def Send_Telegram(self,data):
        try:
            respone = requests.post(
                self.TELE_URL,json={'chat_id':self.TELE_ID,'text':data})
            print(respone.text)
            
        except:
            print('Telegram Sending Error')
            
        

#---------------------------------------------------------------------#

class FactoryEvent(SCADA):
    def __init__(self):
        super().__init__()
        self.Line_speed_sent = [False,False]
        self.HV10_Logs_sent = [False,False,False,False,False] #[OCGR,OCR,OVGR,OVR,UVR]
        self.LV06_Logs_sent = [False,False,False,False,False] #[OCGR,OCR,OVGR,OVR,UVR]
        self.LV07_Logs_sent = [False,False,False,False,False] #[OCGR,OCR,OVGR,OVR,UVR]
        self.LV08_Logs_sent = [False,False,False,False,False] #[OCGR,OCR,OVGR,OVR,UVR]
        self.UHV01_Logs_sent = [False,False,False,False,False] #[OCGR,OCR,OVGR,OVR,UVR]
        self.UHV02_Logs_sent = [False,False,False,False,False] #[OCGR,OCR,OVGR,OVR,UVR]
        self.UHV03_Logs_sent = [False,False,False,False,False] #[OCGR,OCR,OVGR,OVR,UVR]
        self.UHV04_Logs_sent = [False,False,False,False,False] #[OCGR,OCR,OVGR,OVR,UVR]
        self.UHV05_Logs_sent = [False,False,False,False,False] #[OCGR,OCR,OVGR,OVR,UVR]
        self.UHV06_Logs_sent = [False,False,False,False,False] #[OCGR,OCR,OVGR,OVR,UVR]
        self.UHV07_Logs_sent = [False,False,False,False,False] #[OCGR,OCR,OVGR,OVR,UVR]
        self.Gens_Logs_sent = [False,False] #[Gen1,Gen2]
        self.converters_sent = False
        self.converters_error_sent = False
        self.PF_sent = False
        self.GIS_sent = [False,False] #[OverSent,LowSent]
        self.HV_10_sent = [False,False] #[OverSent,LowSent]
        

    def Hourly_inform(self):
        Line_Speed = self.LineSpeed_Read()
        GIS_volt,HV_10_Volt,PF,Power,Energy = self.Incomming()
        CS1,CS2,CS3 = self.CONDENSER()
        
        Time = datetime.now().strftime('[%Y/%m/%d] [%H:%M]')

        Plant_Status_text = f'\n{Time}\n--------REPORT--------\nGIS: {GIS_volt} kV\nHV-10: {HV_10_Volt} kV\nEnergy: {Energy:,} GWh\nPower: {Power:,} kW\nPF: {PF:.2f}[{CS1},{CS2},{CS3}]\n-------------------------\nEntry: {Line_Speed[0]} mpm\nCenter-1: {Line_Speed[1]} mpm\nCenter-2: {Line_Speed[2]} mpm\nDelivery: {Line_Speed[3]} mpm\n-------------------------'
        self.Send_Line(Plant_Status_text)
        self.Send_Telegram(Plant_Status_text)


    def Vamp_Status_Check(self,**VAMP):
        #---------------OCGR---------------#
        if VAMP['OCGR'] and not VAMP['Sent'][0]:
            self.Send_Line(f'\n{VAMP['Name1']} [{VAMP['Name2']}]: OCGR Fault')
            self.Send_Telegram(f'\n{VAMP['Name1']} [{VAMP['Name2']}]: OCGR Fault')
            VAMP['Sent'][0] = True
            
        elif not VAMP['OCGR'] and VAMP['Sent'][0]:
            self.Send_Line(f'\n{VAMP['Name1']} [{VAMP['Name2']}]: OCGR Recovered')
            self.Send_Telegram(f'\n{VAMP['Name1']} [{VAMP['Name2']}]: OCGR Recovered')
            VAMP['Sent'][0] = False
            
        #---------------OCR---------------#
        if VAMP['OCR'] and not VAMP['Sent'][1]:
            self.Send_Line(f'\n{VAMP['Name1']} [{VAMP['Name2']}]: OCR Fault')
            self.Send_Telegram(f'\n{VAMP['Name1']} [{VAMP['Name2']}]: OCR Fault')
            VAMP['Sent'][1] = True
            
        elif not VAMP['OCR'] and VAMP['Sent'][1]:
            self.Send_Line(f'\n{VAMP['Name1']} [{VAMP['Name2']}]: OCR Recovered')
            self.Send_Telegram(f'\n{VAMP['Name1']} [{VAMP['Name2']}]: OCR Recovered')
            VAMP['Sent'][1] = False
            
        #---------------OVGR---------------#
        if VAMP['OVGR'] and not VAMP['Sent'][2]:
            self.Send_Line(f'\n{VAMP['Name1']} [{VAMP['Name2']}]: OVGR Fault')
            self.Send_Telegram(f'\n{VAMP['Name1']} [{VAMP['Name2']}]: OVGR Fault')
            VAMP['Sent'][2] = True
            
        elif not VAMP['OVGR'] and VAMP['Sent'][2]:
            self.Send_Line(f'\n{VAMP['Name1']} [{VAMP['Name2']}]: OVGR Recovered')
            self.Send_Telegram(f'\n{VAMP['Name1']} [{VAMP['Name2']}]: OVGR Recovered')
            VAMP['Sent'][2] = False
            
        #---------------OVR---------------#
        if VAMP['OVR'] and not VAMP['Sent'][3]:
            self.Send_Line(f'\n{VAMP['Name1']} [{VAMP['Name2']}]: OVR Fault')
            self.Send_Telegram(f'\n{VAMP['Name1']} [{VAMP['Name2']}]: OVR Fault')
            VAMP['Sent'][3] = True
        
        elif not VAMP['OVR'] and VAMP['Sent'][3]:
            self.Send_Line(f'\n{VAMP['Name1']} [{VAMP['Name2']}]: OVR Recovered')
            self.Send_Telegram(f'\n{VAMP['Name1']} [{VAMP['Name2']}]: OVR Recovered')
            VAMP['Sent'][3] = False
        
        #---------------UVR---------------#
        if VAMP['UVR'] and not VAMP['Sent'][4]:
            self.Send_Line(f'\n{VAMP['Name1']} [{VAMP['Name2']}]: UVR Fault')
            self.Send_Telegram(f'\n{VAMP['Name1']} [{VAMP['Name2']}]: UVR Fault')
            VAMP['Sent'][4] = True
            
        elif not VAMP['UVR'] and VAMP['Sent'][4]:
            self.Send_Line(f'\n{VAMP['Name1']} [{VAMP['Name2']}]: UVR Recovered')
            self.Send_Telegram(f'\n{VAMP['Name1']} [{VAMP['Name2']}]: UVR Recovered')
            VAMP['Sent'][4] = False
            
            return VAMP['Sent']
        
        
    def Line_Issue(self):
        for T in Event_time:
            schedule.every().day.at(T).do(self.Hourly_inform)
            
        while True:            
            HV_10_OCGR,HV_10_OCR,HV_10_OVGR,HV_10_OVR,HV_10_UVR = self.VAMP_Fault(VAMP_ADDR['HV-10'])
            LV_06_OCGR,LV_06_OCR,LV_06_OVGR,LV_06_OVR,LV_06_UVR = self.VAMP_Fault(VAMP_ADDR['LV-06'])
            LV_07_OCGR,LV_07_OCR,LV_07_OVGR,LV_07_OVR,LV_07_UVR = self.VAMP_Fault(VAMP_ADDR['LV-07'])
            LV_08_OCGR,LV_08_OCR,LV_08_OVGR,LV_08_OVR,LV_08_UVR = self.VAMP_Fault(VAMP_ADDR['LV-08'])
            UHV_01_OCGR,UHV_01_OCR,UHV_01_OVGR,UHV_01_OVR,UHV_01_UVR = self.VAMP_Fault(VAMP_ADDR['UHV-01'])
            UHV_02_OCGR,UHV_02_OCR,UHV_02_OVGR,UHV_02_OVR,UHV_02_UVR = self.VAMP_Fault(VAMP_ADDR['UHV-02'])
            UHV_03_OCGR,UHV_03_OCR,UHV_03_OVGR,UHV_03_OVR,UHV_03_UVR = self.VAMP_Fault(VAMP_ADDR['UHV-03'])
            UHV_04_OCGR,UHV_04_OCR,UHV_04_OVGR,UHV_04_OVR,UHV_04_UVR = self.VAMP_Fault(VAMP_ADDR['UHV-04'])
            UHV_05_OCGR,UHV_05_OCR,UHV_05_OVGR,UHV_05_OVR,UHV_05_UVR = self.VAMP_Fault(VAMP_ADDR['UHV-05'])
            UHV_06_OCGR,UHV_06_OCR,UHV_06_OVGR,UHV_06_OVR,UHV_06_UVR = self.VAMP_Fault(VAMP_ADDR['UHV-06'])
            UHV_07_OCGR,UHV_07_OCR,UHV_07_OVGR,UHV_07_OVR,UHV_07_UVR = self.VAMP_Fault(VAMP_ADDR['UHV-07'])
            Gen1_Run,Gen2_Run = self.Generator()
            Line_Speed = self.LineSpeed_Read()
            CONV1,CONV2,CONV1_I,CONV2_I = self.Com_Converters()
            GIS_Volt,HV_10_Volt,PF,Power,energy = self.Incomming()
            CS1,CS2,CS3 = self.CONDENSER()


            #---HV-10---# Incoming
            self.Vamp_Status_Check(Name1='HV-10',Name2='INCOMING',OCGR=HV_10_OCGR,OCR=HV_10_OCR,OVGR=HV_10_OVGR,
                                                         OVR=HV_10_OVR,UVR=HV_10_UVR,Sent=self.HV10_Logs_sent)
            #---LV-06---# Premelting
            self.Vamp_Status_Check(Name1='LV-06',Name2='PRE-MELTING POT',OCGR=LV_06_OCGR,OCR=LV_06_OCR,OVGR=LV_06_OVGR,
                                                          OVR=LV_06_OVR,UVR=LV_06_UVR,Sent=self.LV06_Logs_sent)
             
            #---LV-07---# GA POT
            self.Vamp_Status_Check(Name1='LV-07',Name2='GA POT',OCGR=LV_07_OCGR,OCR=LV_07_OCR,OVGR=LV_07_OVGR,
                                                          OVR=LV_07_OVR,UVR=LV_07_UVR,Sent=self.LV07_Logs_sent)
            
            #--LV-08---# GI POT
            self.Vamp_Status_Check(Name1='LV-08',Name2='GI POT',OCGR=LV_08_OCGR,OCR=LV_08_OCR,OVGR=LV_08_OVGR,
                                                          OVR=LV_08_OVR,UVR=LV_08_UVR,Sent=self.LV08_Logs_sent)
            
            #---UHV-01---# Cooling motor A
            self.Vamp_Status_Check(Name1='UHV-01',Name2='COOLING MOTOR:A',OCGR=UHV_01_OCGR,OCR=UHV_01_OCR,OVGR=UHV_01_OVGR,
                                                          OVR=UHV_01_OVR,UVR=UHV_01_UVR,Sent=self.UHV01_Logs_sent)
            
            #---UHV-02---# Cooling motor B
            self.Vamp_Status_Check(Name1='UHV-02',Name2='COOLING MOTOR:B',OCGR=UHV_02_OCGR,OCR=UHV_02_OCR,OVGR=UHV_02_OVGR,
                                                          OVR=UHV_02_OVR,UVR=UHV_02_UVR,Sent=self.UHV02_Logs_sent)
            
            #---UHV-03---# Cooling motor C
            self.Vamp_Status_Check(Name1='UHV-03',Name2='COOLING MOTOR:C',OCGR=UHV_03_OCGR,OCR=UHV_03_OCR,OVGR=UHV_03_OVGR,
                                                          OVR=UHV_03_OVR,UVR=UHV_03_UVR,Sent=self.UHV03_Logs_sent)
            
            #---UHV-04---# Cooling motor D
            self.Vamp_Status_Check(Name1='UHV-04',Name2='COOLING MOTOR:D',OCGR=UHV_04_OCGR,OCR=UHV_04_OCR,OVGR=UHV_04_OVGR,
                                                          OVR=UHV_04_OVR,UVR=UHV_04_UVR,Sent=self.UHV04_Logs_sent)
            
            #---UHV-05---# Air Compressor motor A
            self.Vamp_Status_Check(Name1='UHV-05',Name2='AIR COMPRESSOR:A',OCGR=UHV_05_OCGR,OCR=UHV_05_OCR,OVGR=UHV_05_OVGR,
                                                          OVR=UHV_05_OVR,UVR=UHV_05_UVR,Sent=self.UHV05_Logs_sent)
            
            #---UHV-06---# Air Compressor motor B
            self.Vamp_Status_Check(Name1='UHV-06',Name2='AIR COMPRESSOR:B',OCGR=UHV_06_OCGR,OCR=UHV_06_OCR,OVGR=UHV_06_OVGR,
                                                          OVR=UHV_06_OVR,UVR=UHV_06_UVR,Sent=self.UHV06_Logs_sent)
            
            #---UHV-05---# Air Compressor motor C
            self.Vamp_Status_Check(Name1='UHV-07',Name2='AIR COMPRESSOR:C',OCGR=UHV_07_OCGR,OCR=UHV_07_OCR,OVGR=UHV_07_OVGR,
                                                          OVR=UHV_07_OVR,UVR=UHV_07_UVR,Sent=self.UHV07_Logs_sent)
            
            #--Generator--#
            if Gen1_Run and not self.Gens_Logs_sent[0]:
                self.Send_Line('\nGENERATOR1: Started')
                self.Send_Telegram('\nGENERATOR1: Started')
                self.Gens_Logs_sent[0] = True
                
            elif not Gen1_Run and self.Gens_Logs_sent[0]:
                self.Send_Line('\nGENERATOR1: Stopped')
                self.Send_Telegram('\nGENERATOR1: Stopped')
                self.Gens_Logs_sent[0] = False
            
            if Gen2_Run and not self.Gens_Logs_sent[1]:
                self.Send_Line('\nGENERATOR2: Started')
                self.Send_Telegram('\nGENERATOR2: Started')
                self.Gens_Logs_sent[1] = True
            
            elif not Gen2_Run and self.Gens_Logs_sent[1]:
                self.Send_Line('\nGENERATOR2: Stopped')
                self.Send_Telegram('\nGENERATOR2: Stopped')
                self.Gens_Logs_sent[1] = False
            
            #---Center-1 Speed Abnormal---#
            if Line_Speed[1] <= 1 and not self.Line_speed_sent[0]:
                self.Send_Line(f'\nCGL Stopped or Trouble: {Line_Speed[1]} mpm')
                self.Send_Telegram(f'\nCGL Stopped or Trouble: {Line_Speed[1]} mpm')
                self.Line_speed_sent[0] = True            
            elif Line_Speed[1] >5 and self.Line_speed_sent[0]:
                self.Line_speed_sent[0] = False
                
            #---Line start Notify--#    
            if Line_Speed[1] >= 5 and not self.Line_speed_sent[1]:
                self.Send_Line(f'\nCGL Started!: {Line_Speed[1]} mpm')
                self.Send_Telegram(f'\nCGL Started!: {Line_Speed[1]} mpm')
                self.Line_speed_sent[1] = True            
            elif Line_Speed[1] <5 and self.Line_speed_sent[1]:
                self.Line_speed_sent[1] = False
                                        
            #--COMMON CONVERTER STOP--#
            if CONV1 and CONV2 and (CONV1_I >10 or CONV2_I >10) and not self.converters_sent :
                self.Send_Line('\nCONVERTERS: Started')
                self.Send_Telegram('\nCONVERTERS: Started')
                self.converters_sent = True
            elif ((not CONV1 or not CONV2) or (CONV1_I == 0 or CONV2_I == 0)) and self.converters_sent:
                self.Send_Line('\nCONVERTERS: Stopped')
                self.Send_Telegram('\nCONVERTERS: Stopped')
                self.converters_sent = False
            
            #--COMMON CONVERTER DIFF CHECK--# during line stop

            if Line_Speed[0] == 0 and Line_Speed[1] == 0 and Line_Speed[2] == 0 and Line_Speed[3] == 0: # check only line stop
                if abs(CONV1_I - CONV2_I) > 20 and not self.converters_error_sent:
                    self.Send_Line(f'\nCONVERTERS current differ!!\nCONV1: {CONV1_I}A. & CONV2: {CONV2_I}A.')
                    self.Send_Telegram(f'\nCONVERTERS current differ!!\nCONV1: {CONV1_I}A. & CONV2: {CONV2_I}A.')
                    self.converters_error_sent = True
                    
                elif abs(CONV1_I - CONV2_I) <5 and self.converters_error_sent:
                    self.converters_error_sent = False 

            #--Power Factor Check--#
            if PF < 0.85 and not self.PF_sent:
                self.Send_Line(f'\nPF is low: {PF:.2f}\nCS1: {CS1}\nCS2: {CS2}\nCS3: {CS3}')
                self.Send_Telegram(f'\nPF is low: {PF:.2f}\nCS1: {CS1}\nCS2: {CS2}\nCS3: {CS3}')
                self.PF_sent = True
                
            elif PF > 0.87 and self.PF_sent:
                self.Send_Line(f'\nPF is normal: {PF:.2f}\nCS1: {CS1}\nCS2: {CS2}\nCS3: {CS3}')
                self.Send_Telegram(f'\nPF is normal: {PF:.2f}\nCS1: {CS1}\nCS2: {CS2}\nCS3: {CS3}')
                self.PF_sent = False
                
            #--GIS Over Voltage--#
            if GIS_Volt > 125 and not self.GIS_sent[0]:
                self.Send_Line(f'GIS voltage is over. ({GIS_Volt}kV)')
                self.Send_Telegram(f'GIS voltage is over. ({GIS_Volt}kV)')
                self.GIS_sent[0] = True
                
            elif GIS_Volt <122 and self.GIS_sent[0]:
                self.Send_Line(f'GIS voltage is normal. ({GIS_Volt}kV)')
                self.Send_Telegram(f'GIS voltage is normal. ({GIS_Volt}kV)')
                self.GIS_sent[0] = False

            #--GIS Low Voltage--#
            if GIS_Volt < 105 and not self.GIS_sent[1]:
                self.Send_Line(f'GIS is low. ({GIS_Volt}kV)')
                self.Send_Telegram(f'GIS is low. ({GIS_Volt}kV)')
                self.GIS_sent[1] = True
                
            elif GIS_Volt > 110 and self.GIS_sent[1]:
                self.Send_Line(f'GIS is normal. ({GIS_Volt}kV)')
                self.Send_Telegram(f'GIS is normal. ({GIS_Volt}kV)')
                self.GIS_sent[1] = False                
            
            
            #--HV-10 Over Voltage--#
            if HV_10_Volt > 7 and not self.HV_10_sent[0]:
                self.Send_Line(f'HV-10 voltage is over. ({HV_10_Volt}kV)')
                self.Send_Telegram(f'HV-10 voltage is over. ({HV_10_Volt}kV)')                
                self.HV_10_sent[0] = True
                
            elif HV_10_Volt < 6.7 and self.HV_10_sent[0]:
                self.Send_Line(f'HV-10 voltage is normal. ({HV_10_Volt}kV)')
                self.Send_Telegram(f'HV-10 voltage is normal. ({HV_10_Volt}kV)')
                self.HV_10_sent[0] = False
            
            #--HV-10 Low Voltage--#
            if HV_10_Volt < 6.2 and not self.HV_10_sent[1]:
                self.Send_Line(f'HV-10 voltage is low. ({HV_10_Volt}kV)')
                self.Send_Telegram(f'HV-10 voltage is low. ({HV_10_Volt}kV)')
                self.HV_10_sent[1] = True
            elif HV_10_Volt > 6.4 and self.HV_10_sent[1]:
                self.Send_Line(f'HV-10 voltage is normal. ({HV_10_Volt}kV)')
                self.Send_Telegram(f'HV-10 voltage is normal. ({HV_10_Volt}kV)')
                self.HV_10_sent[1] = False
                                             
            schedule.run_pending()   
            time.sleep(0.5)
            
                  
if __name__ == '__main__':
    Line_Event = FactoryEvent()
    Line_Event.Line_Issue()
