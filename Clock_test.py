from HexProcessing import BlueZHexUnit
from forBlueToothConnect import pourBluz
import time
Data=BlueZHexUnit()
Bluemodule=pourBluz()

def interval():
    print(Data.TruOut())
    Data.allclear()


Bluemodule.connect()
Starttime=time.time()
while True:
    aLine=Bluemodule.naivesReceiveHex()
    Data.split(aLine)
    Data.coupData()
    Endtime=time.time()
    if Endtime-Starttime>=3:
        interval()
        time.sleep(2)
        Starttime=time.time()
    else:
        continue

