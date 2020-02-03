import HexProcessing
import forBlueToothConnect as BTC
import re
import time
import numpy as np
import scipy.io as io
import ctypes
time.sleep(3)
player = ctypes.windll.kernel32
if __name__=='__main__':
    Jazz=BTC.pourBluz()
    Jazz.connect()
    Data=HexProcessing.BlueZHexUnit()
    EndTime=0
    for i in range(0,10):
        Jazz.naivesReceive()
        StartTime=time.time()
        player.Beep(1000,1000)
        while EndTime-StartTime<2:
            aLine=Jazz.naivesReceiveHex()
            Data.coupData(aLine)
            print(Data.ValueList)
            EndTime=time.time()
        player.Beep(1000,500)
        time.sleep(0.05)
        player.Beep(1000,500)
        time.sleep(0.05)
        print(len(Data.FullValueList))
        io.savemat('Signal/test_'+str(i)+'.mat',{'data': Data.FullValueList[-600:]})
        Data.allclear()
        time.sleep(4)#shit

    Jazz.close()#huangyifan
