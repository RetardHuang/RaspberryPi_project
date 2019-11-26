import bluetooth

class pourBluz:
    bd_addr = "98:D3:21:FC:82:A8"  # arduino连接的蓝牙模块的地址
    port = 1
    bytesflag = bytes('\r\n',encoding='utf-8')
    def __init__(self):
        pass
    def BluetoothAddressChange(self,BluetoothAddress):
        self.bd_addr=BluetoothAddress
    def BluetoothPortChange(self,port):
        self.port=port
    def BytesFlagChange(self,NewFlag):
        self.bytesflag=bytes(NewFlag,encoding='utf-8')
    def connect(self):
        self.sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
        self.sock.connect((self.bd_addr, self.port))  # 创建连接
    def receive(self):
        receivedData=bytes()
        while True:
            naivedata=self.sock.recv(1024)#contains\r\n at last
            receivedData=receivedData+naivedata
            if naivedata.find(self.bytesflag)+1:
                break
            else:
                continue
        return receivedData
    def received_string(self):
        return str(self.receive(),'utf-8')
    def close(self):
        self.sock.close()  # 关闭连接


if __name__=='__main__':
    Jazz=pourBluz()
    while True:
        Jazz.connect()
        while True:
            try:
                print(Jazz.received_string())
            except:
                break#若连接不上则重新连接
