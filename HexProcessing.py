import forBlueToothConnect as BTC
import re
class BlueZHexUnit:
    def __init__(self):
        self.HexList=list(['']*4)
        self.ValueList=list(['']*4)
        self.ucRxBuffer=list(['']*100)
        self.ucRxCnt = 0  # 0 at initial
        self.FullHexList=list()
        self.FullValueList=list()
    def split(self,ReceivedHexString):
        pattern = re.compile('.{2}')
        self.HexPairs=pattern.findall(ReceivedHexString)#This two is use to split with interval two
    def coupData(self):
        for aPair in self.HexPairs:
            self.ucRxBuffer[self.ucRxCnt] = aPair
            self.ucRxCnt += 1  # 0 at initial
            if self.ucRxBuffer[0]!='55':
                self.ucRxCnt = 0
                continue
            if self.ucRxCnt < 11:
                continue
            else:
                if self.ucRxBuffer[1] == '51':
                    self.HexList[0] = self.ucRxBuffer[2:8]
                    smList=[]
                    for i in [0,2,4]:
                        smList.append(((int((self.HexList[0][i+1]),16)<< 8) | (int(self.HexList[0][i],16))) / 32768 * 16 )
                    self.ValueList[0]=smList
                elif self.ucRxBuffer[1] == '52':
                    self.HexList[1] = self.ucRxBuffer[2:8]
                    smList=[]
                    for i in [0,2,4]:
                        smList.append(((int((self.HexList[1][i+1]),16)<< 8) | (int(self.HexList[1][i],16))) / 32768 * 2000 )
                    self.ValueList[1]=smList
                elif self.ucRxBuffer[1] == '53':
                    self.HexList[2] = self.ucRxBuffer[2:8]
                    smList=[]
                    for i in [0,2,4]:
                        smList.append(((int((self.HexList[2][i+1]),16)<< 8) | (int(self.HexList[2][i],16))) / 32768 * 180 )
                    self.ValueList[2]=smList
                elif self.ucRxBuffer[1] == '54':
                    self.HexList[3] = self.ucRxBuffer[2:8]
                    smList=[]
                    for i in [0,2,4]:
                        smList.append(((int((self.HexList[3][i+1]),16)<< 8) | (int(self.HexList[3][i],16))) )
                    self.ValueList[3]=smList

                    self.FullHexList.append(self.HexList)
                    self.FullValueList.append(self.ValueList)
                self.ucRxCnt =0
    def TruOut(self):
        print(len(self.FullValueList))
        return self.FullValueList[0:149]
    def allclear(self):
        self.HexList=list(['']*4)
        self.ValueList=list(['']*4)
        self.FullValueList=list()
        self.FullHexList=list()


if __name__=='__main__':
    Jazz=BTC.pourBluz()
    Jazz.connect()
    Data=BlueZHexUnit()
    while True:
        aLine=Jazz.naivesReceiveHex()
        Data.split(aLine)
        Data.coupData()
        print(Data.ValueList)
