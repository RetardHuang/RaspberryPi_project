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
    StartTime=time.time()
    EndTime=0
    player.Beep(1000,1000)
    while EndTime-StartTime<3:
        aLine=Jazz.naivesReceiveHex()
        Data.coupData(aLine)
        print(Data.ValueList)
        EndTime=time.time()
    player.Beep(1000,500)
    print('Shit')
    print(Data.FullValueList)
    io.savemat('test.mat',{'data': Data.FullValueList})

    Jazz.close()
