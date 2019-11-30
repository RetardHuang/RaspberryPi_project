import numpy as np
#from scipy.fftpack import fft,ifft
#This is used to calculate each feature of the Data
class Calculate:
    featurenumber=10
    windowLength=150
    def __init__(self,WindowLength):
        self.Feature=np.empty(self.featurenumber)#uninitialized feature
        self.windowLength=WindowLength
        self.FullFeature=np.empty([self.windowLength,self.featurenumber])
    def proAWin(self,DataWithWindowLength):#What need to do after reveicing 3-second Data[AccXMean,,,AccXVar,,AccZVar,]
        npData=np.array(DataWithWindowLength)
        #npDaFr=fft(npData)
        self.Feature[0]=np.mean(npData[:][0][0])#AccXMean
        #self.Feature[1]=np.mean(npData[:][0][1])#AccYMean
        #...........
        #self.Feature[3]=np.var(npData[:][0][1])#AccXVar
        #...........
        print(DataWithWindowLength)
        #return Feature
    def putin(self,WhereInAll):
        self.FullFeature[WhereInAll]=self.Feature

def Save():
    pass
