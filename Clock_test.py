from HexProcessing import BlueZHexUnit
from forBlueToothConnect import pourBluz
import time
Data=BlueZHexUnit()
Bluemodule=pourBluz()

def interval():#What need to do after reveicing 3-second Data
    print(Data.TruOut())
    Data.allclear()


Bluemodule.connect()#Connect to bluetooth module
Starttime=time.time()#Record Start Time
while True:
    Data.split(Bluemodule.naivesReceiveHex())#Read Every string come from HC05
    Data.coupData()#Process it ,and save them in Data.FullValueList
    Endtime=time.time()#Record time
    if Endtime-Starttime>=3:
        interval()
        time.sleep(2)#This step can add another thread
        Starttime=time.time()
    else:
        continue

