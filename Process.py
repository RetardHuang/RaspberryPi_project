import numpy as np
import time
import joblib
import traceback
#from scipy.fftpack import fft,ifft
#This is used to calculate each feature of the Data
class Calculate:
    featurenumber=6
    windowLength=400
    Labelstate=0
    def __init__(self):
        self.Feature=np.empty(self.featurenumber)#uninitialized feature
        self.FullFeature=np.zeros([self.windowLength,self.featurenumber])
    def proAWin(self,DataWithWindowLength):#What need to do after reveicing 3-second Data[AccXMean,,,AccXVar,,AccZVar,]
        npData=np.array(DataWithWindowLength)
        #npDaFr=fft(npData)
        try:
            self.Feature[0]=np.mean(npData[:][0][0])#AccXMean
            self.Feature[1]=np.mean(npData[:][0][1])#AccYMean
            self.Feature[2]=np.mean(npData[:][0][2])#AccZMean
            self.Feature[3]=np.mean(npData[:][1][0])#GXMean
            self.Feature[4]=np.mean(npData[:][1][1])#GYMean
            self.Feature[5]=np.mean(npData[:][1][2])#GZMean
        except IndexError:
            print('Having not received enough data')
        print(self.Feature)
    def loadModel(self):#Load the joblib model
        self.model=joblib.load('rtcs.model')
    def featureRecognize(self):#Start recognize by machine learning
        self.Labelstate=self.model.predict(self.Feature.reshape(1,-1))
        pass
    def putin(self,WhereInAll):
        self.FullFeature[WhereInAll]=self.Feature
    def SavewithLabel(self,LabelOfTheTest):
        LabelArray=np.full((self.windowLength,self.featurenumber),LabelOfTheTest)
        np.save((time.strftime("Dataoutput/Data_%b%d_%H_%M_Type", time.localtime())+str(LabelOfTheTest)),self.FullFeature)
        np.save((time.strftime("Dataoutput/Label_%b%d_%H_%M_Type", time.localtime())+str(LabelOfTheTest)),LabelArray)
