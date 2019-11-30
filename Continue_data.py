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
        Calculate.__init__(self,self.windowLength)
        self.leftedge=0
        self.stepLength=1
        self.windowFlag=False
    def setWindowLength(self,WindowLength):
        BlueZHexUnit.setWindowLength(self,WindowLength)
        self.FullFeature=np.empty([self.windowLength,self.featurenumber])

    def windowFowards(self):
        self.leftedge+=self.stepLength
    def windowData(self):
        return self.FullValueList[self.leftedge:self.leftedge+self.windowLength]
    def ifreach(self):
        return (self.leftedge+self.windowLength)>=len(self.FullValueList)
    def deleteTail(self):
        del self.FullValueList[0:-self.windowLength]
    ######################################
    def recognize(self):#DetectwindowData!
        print('Recog!')
        self.proAWin(self.windowData())
        pass
    ######################################
    def interval(self):#What need to do after reveicing 3-second Data
        print(self.TruOut())
    def lopClimb(self):#To Reconize the action
        while True:
            self.recognize()####################################3
            if self.ifreach():
                self.deleteTail()
                while True:
                    if self.windowFlag:
                        self.windowFlag=False
                        break
                    else:
                        time.sleep(0.0001)
            self.windowFowards()
    def lopcoupData(self):#To get the data, which need to be assgined into another thread
        global Bluemodule
        while True:
            self.coupData(Bluemodule.naivesReceiveHex())
            print('Rec!')
            self.windowFlag=True

if __name__=='__main__':
    Data= BHRecog()
    Data.setWindowLength(150)
    Bluemodule=pourBluz()
    Read = threading.Thread(target=Data.lopcoupData, name='ReadTheData')
    Clim = threading.Thread(target=Data.lopClimb, name='ClimbTheData')
    Bluemodule.connect()#Connect to bluetooth module
    Read.start()
    Clim.start()
    Read.join()
    Clim.join()




