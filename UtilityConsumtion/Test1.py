import snap7
from snap7 import util
import time


plc = snap7.client.Client()
plc.connect('192.168.10',0,3)
plc.get_connected()
print(plc.get_connected())

db1037 = snap7.util.DB(1037,bytearray(8))