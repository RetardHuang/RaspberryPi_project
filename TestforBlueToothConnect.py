import forBlueToothConnect as fB
co=fB.pourBluz()
co.connect()
received=bytearray(co.receive())
print (received)