import HexProcessing
import forBlueToothConnect as BTC
import re
import time
import numpy as np
import scipy.io as io
import ctypes
player = ctypes.windll.kernel32

if __name__=='__main__':
    Jazz=BTC.pourBluz()
    Jazz.connect()
    Data=HexProcessing.BlueZHexUnit()
    EndTime=0
    for i in range(0,5):
        Jazz.naivesReceive()
        StartTime=time.time()
        while EndTime-StartTime<2:
            aLine=Jazz.naivesReceiveHex()
            Data.coupData(aLine)
            print(Data.ValueList)
            EndTime=time.time()
        print('Shit')
        print(len(Data.FullValueList))
        io.savemat('Signal/test_'+str(i)+'.mat',{'data': Data.FullValueList[-600:]})
        Data.allclear()
        time.sleep(3)

    Jazz.close()
