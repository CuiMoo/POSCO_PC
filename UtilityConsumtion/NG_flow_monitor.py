from tkinter import *
from connect_plc import *
from datetime import datetime
import threading
import time




class Showdata:
    def __init__(self) -> None:
        self.root = Tk()
        self.root.geometry('1400x150')
        self.root.title('Utility Consumption Monitoring')
        self.oPLC = utilityPLC()

        self.V_NG_boiler_A_Flow = StringVar()
        self.V_NG_boiler_B_Flow = StringVar()
        self.V_N2_Flow = StringVar()
        self.V_H2_Flow = StringVar()
        self.V_FT_test = StringVar()

        self.NG_boiler_A_Flow = 0
        self.NG_boiler_B_Flow = 0
        self.N2_Flow = 0
        self.H2_Flow = 0
        self.flow_test = 0

        self.V_NG_boiler_A_FlowMeter = StringVar()
        self.V_NG_boiler_B_FlowMeter = StringVar()
        self.V_N2_FlowMeter = StringVar()
        self.V_H2_FlowMeter = StringVar()
        self.V_FT_testMeter = StringVar()

        
        self.NG1_sum = 0
        self.NG2_sum = 0
        self.N2_sum = 0
        self.H2_sum =0
        self.FT_test_sum = 0
        

        self.data = None

        L1 = Label(self.root,text='NG BOILER A',font=(None,30,'bold'))
        L1.grid(row=1,column=0,padx=20)
        L2 = Label(self.root,textvariable=self.V_NG_boiler_A_Flow,font=(None,20))
        L2.grid(row=2,column=0,padx=20)

        L3 = Label(self.root,text='NG BOILER B',font=(None,30,'bold'))
        L3.grid(row=1,column=1,padx=20)
        L4 = Label(self.root,textvariable=self.V_NG_boiler_B_Flow,font=(None,20))
        L4.grid(row=2,column=1,padx=20)

        L5 = Label(self.root,text='N2 Flow',font=(None,30,'bold'))
        L5.grid(row=1,column=2,padx=20)
        L6 = Label(self.root,textvariable=self.V_N2_Flow,font=(None,20))
        L6.grid(row=2,column=2,padx=20)

        L7 = Label(self.root,text='H2 Flow',font=(None,30,'bold'))
        L7.grid(row=1,column=3,padx=20)
        L8 = Label(self.root,textvariable=self.V_H2_Flow,font=(None,20))
        L8.grid(row=2,column=3,padx=20)

        L9 = Label(self.root,text='Test Flow',font=(None,30,'bold'))
        L9.grid(row=1,column=4,padx=20)
        L10 = Label(self.root,textvariable=self.V_FT_test,font=(None,20))
        L10.grid(row=2,column=4,padx=20)

        L11 = Label(self.root,textvariable=self.V_NG_boiler_A_FlowMeter,font=(None,20))
        L11.grid(row=3,column=0,padx=20)

        L12 = Label(self.root,textvariable=self.V_NG_boiler_B_FlowMeter,font=(None,20))
        L12.grid(row=3,column=1,padx=20)

        L13 = Label(self.root,textvariable=self.V_N2_FlowMeter,font=(None,20))
        L13.grid(row=3,column=2,padx=20)

        L13 = Label(self.root,textvariable=self.V_H2_FlowMeter,font=(None,20))
        L13.grid(row=3,column=3,padx=20)

        L13 = Label(self.root,textvariable=self.V_FT_testMeter,font=(None,20))
        L13.grid(row=3,column=4,padx=20)

            

    def dataGetUpdate(self):
        boiler_A_Flow_T1 = self.NG1_sum
        boiler_B_Flow_T1 = self.NG2_sum
        N2_Flow_T1 = self.N2_sum
        H2_Flow_T1 = self.H2_sum
        Test_Flow_T1 = self.FT_test_sum

        T1 = datetime.now().strftime('%H:%M:%S')
        print(f'Time: {T1}')

        while True:

            self.V_NG_boiler_A_Flow.set(f'{self.NG1_sum:.3f} Nm3')
            self.V_NG_boiler_B_Flow.set(f'{self.NG2_sum:.3f} Nm3')
            self.V_N2_Flow.set(f'{self.N2_sum:.3f} Nm3')
            self.V_H2_Flow.set(f'{self.H2_sum:.3f} Nm3')
            self.V_FT_test.set(f'{self.FT_test_sum:.3f} Nm3')

            self.V_NG_boiler_A_FlowMeter.set(f'{self.NG_boiler_A_Flow:.3f} Nm3/hr')
            self.V_NG_boiler_B_FlowMeter.set(f'{self.NG_boiler_B_Flow:.3f} Nm3/hr')
            self.V_N2_FlowMeter.set(f'{self.N2_Flow:.3f} Nm3/hr')
            self.V_H2_FlowMeter.set(f'{self.H2_Flow:.3f} Nm3/hr')
            self.V_FT_testMeter.set(f'{self.flow_test:.3f} Nm3/hr')

            Tnow = datetime.now().strftime('%Y %m %d %H %M %S').split(' ')
            Tr = datetime.now().strftime('%H:%M')
        

            if Tnow[4]  == '00'  and Tnow[5] == '00':   
                Boiler_A_Flow_rec = self.NG1_sum - boiler_A_Flow_T1
                Boiler_B_Flow_rec = self.NG2_sum - boiler_B_Flow_T1
                N2_Flow_rec = self.N2_sum - N2_Flow_T1
                H2_flow_rec = self.H2_sum - H2_Flow_T1
                test_flow_rec = self.FT_test_sum - Test_Flow_T1

                print(f'Time:{Tnow} Test Flow rec: {test_flow_rec:.3f}\n\
time:{Tnow} Boiler A: {Boiler_A_Flow_rec:.3f}\n\
time:{Tnow} Boiler B: {Boiler_B_Flow_rec:.3f}\n\
time:{Tnow} N2: {N2_Flow_rec:.3f}\n\
time:{Tnow} H2: {H2_flow_rec:.3f}\n----------------')
                
                NG_A_Rec = round(Boiler_A_Flow_rec)
                NG_B_Rec = round(Boiler_B_Flow_rec)
                N2_Rec = round(N2_Flow_rec)
                H2_Rec = round(H2_flow_rec)
                test_Rec = round(test_flow_rec)


                self.oPLC.writeToCSV((Tr,NG_A_Rec,NG_B_Rec,N2_Rec,
                                      H2_Rec,test_Rec),Tnow)

                boiler_A_Flow_T1 = self.NG1_sum
                boiler_B_Flow_T1 = self.NG2_sum
                N2_Flow_T1 = self.N2_sum
                H2_Flow_T1= self.H2_sum
                Test_Flow_T1 = self.FT_test_sum
                print(f'Test flow:{Test_Flow_T1}\n---------')


            time.sleep(1)

    def flowSum(self):
        
        N2_sum1 = 0
        N2_sum2 = 0

        NG1_sum1 = 0
        NG1_sum2 = 0

        NG2_sum1 = 0
        NG2_sum2 = 0

        H2_sum1 = 0
        H2_sum2 = 0

        FT_sum1 = 0
        FT_sum2 = 0
        dt = 0.1
        while True:
            t1 = time.time()
            data = self.oPLC.dataCollect()
            self.NG_boiler_A_Flow = data[0]
            self.NG_boiler_B_Flow = data[1]
            self.N2_Flow = data[2]
            self.H2_Flow = data[3]
            self.flow_test = 60

            #
            # deltaFlow in cycle time 
            dNG1 = self.NG_boiler_A_Flow/(3600/dt) 
            dNG2 = self.NG_boiler_B_Flow/(3600/dt)
            dN2 = self.N2_Flow/(3600/dt)
            dH2 = self.H2_Flow/(3600/dt)
            dFt = self.flow_test/(3600/dt)

            NG1_sum1 = NG1_sum1 + dNG1
            NG2_sum1 = NG2_sum1 + dNG2
            N2_sum1 = N2_sum1 + dN2
            H2_sum1 = H2_sum1 + dH2
            FT_sum1 = FT_sum1 + dFt

            if NG1_sum1 >=1:
                NG1_sum2 +=1
                NG1_sum1 -=1

            if NG2_sum1 >=1:
                NG2_sum2 +=1
                NG2_sum1 -=1

            if N2_sum1>=1:
                N2_sum2 +=1
                N2_sum1 -=1

            if H2_sum1>=1:
                H2_sum2 +=1
                H2_sum1 -=1

            if FT_sum1>=1:
                FT_sum2+=1
                FT_sum1-=1
                
            
            self.NG1_sum = NG1_sum1 + NG1_sum2
            self.NG2_sum = NG2_sum1 + NG2_sum2
            self.N2_sum = N2_sum1 + N2_sum2
            self.H2_sum = H2_sum1 + H2_sum2
            self.FT_test_sum = FT_sum1 + FT_sum2

            # print(f'NG1 Flow: {self.NG1_sum:.3f} NG2 Flow: {self.NG2_sum:.3f} N2 Flow: {self.N2_sum:.3f}\
            # H2 Flow: {self.H2_sum:.3f} FT test {self.FT_test_sum:.3f}')
            

            t2 = time.time()
            dt = t2-t1
    


    def scanTime(self):
        task1 = threading.Thread(target=self.flowSum)
        task2 = threading.Thread(target=self.dataGetUpdate)

        
        task1.start()
        task2.start()
        self.root.mainloop()


if __name__ == '__main__':
    appRun = Showdata()
    start = appRun.scanTime()