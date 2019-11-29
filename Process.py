import numpy as np
from scipy.fftpack import fft,ifft
def proAWin(self,DataWithWindowLength):#What need to do after reveicing 3-second Data[AccXMean,,,AccXVar,,AccZVar,]
    Feature=np.empty(123)#123 is number of feature
    npData=np.array(self,DataWithWindowLength)
    npDaFr=fft(npData)
    #Feature[0]=np.mean(npData[:][0][0])#AccXMean
    #Feature[1]=np.mean(npData[:][0][1])#AccYMean
    #...........
    #Feature[3]=np.var(npData[:][0][1])#AccXVar
    #...........
    print(DataWithWindowLength)
    def stackWins(self):
        pass

