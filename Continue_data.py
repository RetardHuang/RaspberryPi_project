#This Program is aimed to collect data with of JY901 of 3 seconds.
from HexProcessing import BlueZHexUnit
from forBlueToothConnect import pourBluz
import time
import threading

from Process import Calculate
import numpy as np
#from scipy.fftpack import fft,ifft

global Data, Bluemodule
class BHRecog(BlueZHexUnit,Calculate):
    def __init__(self):#Init Step must contain the length of window
        BlueZHexUnit.__init__(self)
        Calculate.__init__(self)
        self.leftedge=0
        self.stepLength=3
        self.climbFlag=False
    ######################################
    def recognize(self):#DetectwindowData!
        print('Data pool is full, start a recognition')
        self.proAWin(self.FullValueList[0:self.windowLength])
    ######################################
    def setWindowLength(self,wlength):
        self.windowLength=wlength
    def lopClimb(self):#To Reconize the action
        while True:
            if len(self.FullValueList) > self.windowLength:
                del self.FullValueList[0:self.stepLength]
                print('windowLength is',self.windowLength)
                print('Pool length is',len(self.FullValueList))
                self.recognize()####################################
    def lopcoupData(self):#To get the data, which need to be assgined into another thread
        global Bluemodule
        while True:
            print('Receiving a new data train')
            self.coupDaa(Bluemodule.naivesReceiveHex())

if __name__=='__main__':
    Data= BHRecog()
    Data.setWindowLength(600)
    Bluemodule=pourBluz()
    Bluemodule.connect()#Connect to bluetooth module
    Read = threading.Thread(target=Data.lopcoupData, name='ReadTheData')
    Clim = threading.Thread(target=Data.lopClimb, name='ClimbTheData')
    Read.start()
    Clim.start()
    Read.join()
    Clim.join()




