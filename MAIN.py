import time
import traceback

from pymodbus.client.sync import ModbusSerialClient as pyRtu

slavesArr = [2]
iterSp = 100
regsSp = 10
portNbr = 21
portName = 'com22'
baudrate = 9600
timeoutSp = 0.018 + regsSp * 0

siting_RTU = {
    "method": 'rtu',
    "port": 'COM4',
    "baudrate": 9600,
    "timeout": 0.1,
              }

pymc = pyRtu(siting_RTU)

errCnt = 0
startTs = time.time()
for i in range(iterSp):
    for slaveId in slavesArr:
        try:
            pymc.read_holding_registers(0, regsSp, unit=slaveId)
        except:
            errCnt += 1
            tb = traceback.format_exc()
stopTs = time.time()
timeDiff = stopTs - startTs
print("pymodbus:\ttime to read %s x %s (x %s regs): %.3f [s] / %.3f [s/req]" % (len(slavesArr), iterSp,
                                                                                regsSp, timeDiff, timeDiff / iterSp))
if errCnt > 0:
    print("   !pymodbus:\terrCnt: %s; last tb: %s" % (errCnt, tb))

pymc.close()

