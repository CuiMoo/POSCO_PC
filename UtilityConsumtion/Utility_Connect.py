import snap7
from snap7 import util
import time

plc = snap7.client.Client()
plc.connect('192.168.10',0,3)
plc.get_connected()
print(plc.get_connected())


while True:
    # db1 = plc.db_read(1031,16,4)
    # t1 = util.get_int(db1,0)
    # db2 = plc.db_read(1031,18,4)
    # t2 = util.get_int(db2,0)
    boiler_A_NG = plc.db_read(1037,112,4)
    boiler_A_NGflow = util.get_real(boiler_A_NG,0)

    boiler_B_NG = plc.db_read(1038,112,4)
    boiler_B_NGflow = util.get_real(boiler_B_NG,0)
    
    print(f'NG Boiler A: {boiler_A_NGflow} NM3 & NG Boiler A: {boiler_B_NGflow} NM3')
    time.sleep(1)
    



    