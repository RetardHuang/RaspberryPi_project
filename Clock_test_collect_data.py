#This Program is aimed to collect data with of JY901 of 3 seconds.
from HexProcessing import BlueZHexUnit
from forBlueToothConnect import pourBluz
import time
Data=BlueZHexUnit()
Bluemodule=pourBluz()

def interval():#What need to do after reveicing 3-second Data
    print(Data.TruOut())


Bluemodule.connect()#Connect to bluetooth module
Starttime=time.time()#Record Start Time
while True:
    Data.coupData(Bluemodule.naivesReceiveHex())#Read Every string come from HC05.Process it ,and save them in Data.FullValueList
    Endtime=time.time()#Record time
    if Endtime-Starttime>=3:
        interval()
        Data.allclear()
        time.sleep(2)#This step can bed added to another thread
        Starttime=time.time()
    else:
        continue

