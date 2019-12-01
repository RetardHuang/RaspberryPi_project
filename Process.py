import numpy as np
import time
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
        self.Feature[1]=np.mean(npData[:][0][1])#AccYMean
        self.Feature[2]=np.mean(npData[:][0][2])#AccYMean
        self.Feature[3]=np.mean(npData[:][1][0])#AccXMean
        self.Feature[4]=np.mean(npData[:][1][1])#AccYMean
        self.Feature[5]=np.mean(npData[:][1][2])#AccYMean
        #...........
        #self.Feature[3]=np.var(npData[:][0][1])#AccXVar
        #...........
        print(DataWithWindowLength)
        #return Feature
    def putin(self,WhereInAll):
        self.FullFeature[WhereInAll]=self.Feature
    def SavewithLabel(self,LabelOfTheTest):
        LabelArray=np.full((self.windowLength,self.featurenumber),LabelOfTheTest)
        np.save((time.strftime("Dataoutput/Data_%b%d_%H_%M_Type", time.localtime())+str(LabelOfTheTest)),self.FullFeature)
        np.save((time.strftime("Dataoutput/Label_%b%d_%H_%M_Type", time.localtime())+str(LabelOfTheTest)),LabelArray)
