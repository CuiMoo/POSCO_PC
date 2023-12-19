from tkinter import *
from connect_plc import *
from datetime import datetime
import threading
import time



class Showdata:
    def __init__(self) -> None:
        # UI configuration
        self.root = Tk()
        self.root.geometry('1800x300')
        self.root.title('POSCO-TCS Utility Consumption Monitoring')
        self.root.iconbitmap('Computer.ico')
        self.root.config(bg='black')
        
        back_ground = 'black'
        font = 'Tahoma'
        head_color = 'yellow'
        flow_title_color = 'green'
        flow_sum_color = 'orange'
        flow_meter_color ='red'


        self.oPLC = UtilityPLC()

        self.V_NG_boiler_A_Flow = StringVar()
        self.V_NG_boiler_B_Flow = StringVar()
        self.V_Fce_Flow = StringVar()
        self.V_N2_Flow = StringVar()
        self.V_H2_Flow = StringVar()
        self.V_FT_test = StringVar()



        self.NG_boiler_A_Flow = 0
        self.NG_boiler_B_Flow = 0
        self.Fce_Flow = 0
        self.N2_Flow = 0
        self.H2_Flow = 0
        self.flow_test = 0


        self.V_NG_boiler_A_FlowMeter = StringVar()
        self.V_NG_boiler_B_FlowMeter = StringVar()
        self.V_Fce_FlowMeter = StringVar()
        self.V_N2_FlowMeter = StringVar()
        self.V_H2_FlowMeter = StringVar()
        self.V_FT_testMeter = StringVar()

        self.V_Status = StringVar()

        
        self.NG1_sum = 0
        self.NG2_sum = 0
        self.Fce_sum = 0
        self.N2_sum = 0
        self.H2_sum = 0
        self.FT_test_sum = 0


        

        self.data = None
        self.Fce_Flow_Cal = 0
        self.Tnow = None

        self.Header = Frame(self.root,width=1600,height=100,bg=back_ground)
        self.Header.pack()

        L = Label(self.Header,text='POSCO-TCS CONSUMPTION MONITORING',font=(font,35,'bold'),fg=head_color,bg=back_ground)
        L.pack(pady=20)

        self.detail = Frame(self.root,width=1600,height=150,background=back_ground)
        self.detail.pack()
        #---NG Boiler A---
        L1 = Label(self.detail,text='NG BOILER:A',font=(font,30,'bold'),fg=flow_title_color,bg=back_ground)
        L1.grid(row=1,column=0,padx=20)
        L2 = Label(self.detail,textvariable=self.V_NG_boiler_A_Flow,font=(font,20),fg=flow_sum_color,bg=back_ground)
        L2.grid(row=2,column=0,padx=20)

        #---NG Boiler B---
        L3 = Label(self.detail,text='NG BOILER:B',font=(font,30,'bold'),fg=flow_title_color,bg=back_ground)
        L3.grid(row=1,column=1,padx=20)
        L4 = Label(self.detail,textvariable=self.V_NG_boiler_B_Flow,font=(font,20),fg=flow_sum_color,bg=back_ground)
        L4.grid(row=2,column=1,padx=20)

        #---F'ce Flow---
        L5 = Label(self.detail,text="NG-F'ce Flow",font=(font,30,'bold'),fg=flow_title_color,bg=back_ground)
        L5.grid(row=1,column=2,padx=20)
        L6 = Label(self.detail,textvariable=self.V_Fce_Flow,font=(font,20),fg=flow_sum_color,bg=back_ground)
        L6.grid(row=2,column=2,padx=20)

        #---N2 Flow---
        L7 = Label(self.detail,text='N2 Flow',font=(font,30,'bold'),fg=flow_title_color,bg=back_ground)
        L7.grid(row=1,column=3,padx=20)
        L8 = Label(self.detail,textvariable=self.V_N2_Flow,font=(font,20),fg=flow_sum_color,bg=back_ground)
        L8.grid(row=2,column=3,padx=20)

        #---H2 Flow---       
        L9 = Label(self.detail,text='H2 Flow',font=(font,30,'bold'),fg=flow_title_color,bg=back_ground)
        L9.grid(row=1,column=4,padx=20)
        L10 = Label(self.detail,textvariable=self.V_H2_Flow,font=(font,20),fg=flow_sum_color,bg=back_ground)
        L10.grid(row=2,column=4,padx=20)

        #---Test Flow---
        L11 = Label(self.detail,text='Ref. Flow',font=(None,30,'bold'),fg=flow_title_color,bg=back_ground)
        L11.grid(row=1,column=5,padx=20)
        L12 = Label(self.detail,textvariable=self.V_FT_test,font=(None,20),fg=flow_sum_color,bg=back_ground)
        L12.grid(row=2,column=5,padx=20)


        #---NG Boiler A Flow meter---
        L13 = Label(self.detail,textvariable=self.V_NG_boiler_A_FlowMeter,font=(font,20),fg=flow_meter_color,bg=back_ground)
        L13.grid(row=3,column=0,padx=20)

        #---NG Boiler B Flow meter---
        L14 = Label(self.detail,textvariable=self.V_NG_boiler_B_FlowMeter,font=(font,20),fg=flow_meter_color,bg=back_ground)
        L14.grid(row=3,column=1,padx=20)

        #---Fce Flow meter---
        L15 = Label(self.detail,textvariable=self.V_Fce_FlowMeter,font=(font,20),fg=flow_meter_color,bg=back_ground)
        L15.grid(row=3,column=2,padx=20)

        #---N2 meter---
        L16 = Label(self.detail,textvariable=self.V_N2_FlowMeter,font=(font,20),fg=flow_meter_color,bg=back_ground)
        L16.grid(row=3,column=3,padx=20)

        #---H2 meter---
        L17 = Label(self.detail,textvariable=self.V_H2_FlowMeter,font=(font,20),fg=flow_meter_color,bg=back_ground)
        L17.grid(row=3,column=4,padx=20)

        #---Flow Ref. at 60--
        L18 = Label(self.detail,textvariable=self.V_FT_testMeter,font=(font,20),fg=flow_meter_color,bg=back_ground)
        L18.grid(row=3,column=5,padx=20)


            

    def dataGetUpdate(self):
        boiler_A_Flow_T1 = self.NG1_sum
        boiler_B_Flow_T1 = self.NG2_sum
        Fce_Flow_T1 = self.Fce_sum
        N2_Flow_T1 = self.N2_sum
        H2_Flow_T1 = self.H2_sum
        Test_Flow_T1 = self.FT_test_sum

        T1 = datetime.now().strftime('%H:%M:%S')
        print(f'Time: {T1}')

        while True:

            self.V_NG_boiler_A_Flow.set(f'{self.NG1_sum:.1f} Nm3')
            self.V_NG_boiler_B_Flow.set(f'{self.NG2_sum:.1f} Nm3')
            self.V_Fce_Flow.set(f'{self.Fce_sum:.1f} Nm3')
            self.V_N2_Flow.set(f'{self.N2_sum:.1f} Nm3')
            self.V_H2_Flow.set(f'{self.H2_sum:.1f} Nm3')
            self.V_FT_test.set(f'{self.FT_test_sum:.1f} Nm3')

            self.V_NG_boiler_A_FlowMeter.set(f'{self.NG_boiler_A_Flow:.1f} Nm3/hr')
            self.V_NG_boiler_B_FlowMeter.set(f'{self.NG_boiler_B_Flow:.1f} Nm3/hr')
            self.V_Fce_FlowMeter.set(f'{self.Fce_Flow_Cal:.1f} Nm3/hr')
            self.V_N2_FlowMeter.set(f'{self.N2_Flow:.1f} Nm3/hr')
            self.V_H2_FlowMeter.set(f'{self.H2_Flow:.1f} Nm3/hr')
            self.V_FT_testMeter.set(f'{self.flow_test:.1f} Nm3/hr')


     
            self.Tnow = datetime.now().strftime('%Y %m %d %H %M %S').split(' ')
            Tr = f'{self.Tnow[3]}:{self.Tnow[4]}'      
            date = f'{self.Tnow[1]}/{self.Tnow[2]}'    
        

            if self.Tnow[4]  == '00'  and self.Tnow[5] == '00': #int(Tnow[4])%1 == 0 and int(Tnow[5]) == 0: | Tnow[4]  == '00'  and Tnow[5] == '00':
                Boiler_A_Flow_rec = self.NG1_sum - boiler_A_Flow_T1
                Boiler_B_Flow_rec = self.NG2_sum - boiler_B_Flow_T1
                Fce_Flow_rec = self.Fce_sum - Fce_Flow_T1
                N2_Flow_rec = self.N2_sum - N2_Flow_T1
                H2_flow_rec = self.H2_sum - H2_Flow_T1
                test_flow_rec = self.FT_test_sum - Test_Flow_T1


                NG_A_Rec = round(Boiler_A_Flow_rec)
                NG_B_Rec = round(Boiler_B_Flow_rec)
                Fce_Rec = round(Fce_Flow_rec)
                N2_Rec = round(N2_Flow_rec)
                H2_Rec = round(H2_flow_rec)
                test_Rec = round(test_flow_rec)


                self.oPLC.writeToCSV((date,Tr,NG_A_Rec,NG_B_Rec,Fce_Rec,N2_Rec,
                                      H2_Rec,test_Rec),self.Tnow)

                boiler_A_Flow_T1 = self.NG1_sum
                boiler_B_Flow_T1 = self.NG2_sum
                Fce_Flow_T1 = self.Fce_sum
                N2_Flow_T1 = self.N2_sum
                H2_Flow_T1= self.H2_sum
                Test_Flow_T1 = self.FT_test_sum

                

            time.sleep(1)

    def flowSum(self):
        #inital starting data
        NG1_sum1 = 0
        NG1_sum2 = 0

        NG2_sum1 = 0
        NG2_sum2 = 0

        Fce_sum1 = 0
        Fce_sum2 = 0

        N2_sum1 = 0
        N2_sum2 = 0

        H2_sum1 = 0
        H2_sum2 = 0

        FT_sum1 = 0
        FT_sum2 = 0
        dt = 0.1


        while True:

            t1 = time.time()
            try:
                data = self.oPLC.dataCollect()
                self.flow_test = 60
            except:
                data = (0,0,0,0,0)
                self.oPLC = UtilityPLC()  # Re-Connect
                self.flow_test = 0

            self.NG_boiler_A_Flow = data[0]
            self.NG_boiler_B_Flow = data[1]
            self.Fce_Flow = data[2]
            self.N2_Flow = data[3]
            self.H2_Flow = data[4]


            #Furnace flow accuracy set
            if self.Fce_Flow > 3500:
                self.Fce_Flow_Cal = self.Fce_Flow - 6.0

            elif self.Fce_Flow >= 3000 and self.Fce_Flow < 3500 :
                self.Fce_Flow_Cal = self.Fce_Flow - 5.7871

            elif self.Fce_Flow >= 2000 and self.Fce_Flow < 3000:
                self.Fce_Flow_Cal = self.Fce_Flow - 4.6296

            elif self.Fce_Flow >= 500 and self.Fce_Flow < 2000:
                self.Fce_Flow_Cal = self.Fce_Flow - 3.4722
            
            else:
                self.Fce_Flow_Cal = self.Fce_Flow - 2.3148

                if self.Fce_Flow_Cal < 0:
                    self.Fce_Flow_Cal = 0
                        

            # deltaFlow in cycle time
            try:
                dNG1 = self.NG_boiler_A_Flow/(3600/dt) 
                dNG2 = self.NG_boiler_B_Flow/(3600/dt)
                dFce = self.Fce_Flow_Cal/(3600/dt)
                dN2 = self.N2_Flow/(3600/dt)
                dH2 = self.H2_Flow/(3600/dt)
                dFt = self.flow_test/(3600/dt)
            
            except ZeroDivisionError:
                dNG1 = 0
                dNG2 = 0
                dFce = 0
                dN2 = 0
                dH2 = 0
                dFt = 0

            ####Summation every cycle time#################
            NG1_sum1 = NG1_sum1 + dNG1
            NG2_sum1 = NG2_sum1 + dNG2
            Fce_sum1 = Fce_sum1 +dFce
            N2_sum1 = N2_sum1 + dN2
            H2_sum1 = H2_sum1 + dH2
            FT_sum1 = FT_sum1 + dFt


            if NG1_sum1 >=1:
                NG1_sum2 +=1
                NG1_sum1 -=1

            if NG2_sum1 >=1:
                NG2_sum2 +=1
                NG2_sum1 -=1

            if Fce_sum1 >=1:
                Fce_sum2 +=1
                Fce_sum1 -=1

            if N2_sum1>=1:
                N2_sum2 +=1
                N2_sum1 -=1

            if H2_sum1>=1:
                H2_sum2 +=1
                H2_sum1 -=1

            if FT_sum1>=1:
                FT_sum2+=1
                FT_sum1-=1
                            
            ###################################
            self.NG1_sum = NG1_sum1 + NG1_sum2
            self.NG2_sum = NG2_sum1 + NG2_sum2
            self.Fce_sum = Fce_sum1 + Fce_sum2
            self.N2_sum = N2_sum1 + N2_sum2
            self.H2_sum = H2_sum1 + H2_sum2
            self.FT_test_sum = FT_sum1 + FT_sum2

            if self.Tnow[2] == '01' and self.Tnow[3] == '00' and self.Tnow[4] == '00' and self.Tnow[5] == '00':
                self.NG1_sum = 0
                self.NG2_sum = 0
                self.Fce_sum = 0
                self.N2_sum = 0
                self.H2_sum = 0
                self.FT_test_sum = 0

                NG1_sum1 = 0
                NG2_sum1 = 0
                Fce_sum1 = 0
                N2_sum1 = 0
                H2_sum1 = 0
                FT_sum1 = 0

                NG1_sum2 = 0
                NG2_sum2 = 0
                Fce_sum2 = 0
                N2_sum2 = 0
                H2_sum2 = 0
                FT_sum2 = 0
                
                      
            t2 = time.time()
            dt = t2-t1

#Threading program
    def scanTime(self):
        task1 = threading.Thread(target=self.flowSum)
        task2 = threading.Thread(target=self.dataGetUpdate)        
        task1.start()
        task2.start()
        self.root.mainloop()


if __name__ == '__main__':
    appRun = Showdata()
    start = appRun.scanTime()