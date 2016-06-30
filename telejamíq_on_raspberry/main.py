import cms50dplus
import time
import os
import random
import commands

#from control_led import HardwareLedRpi
from helperDB import HelperDB

def scanAvailableUSBDisp():
    r = commands.getstatusoutput('ls /dev/ttyUSB*')
    size = len(r)
    return r[1]


hdb = HelperDB()
pulsoximeter = cms50dplus.CMS50Dplus(scanAvailableUSBDisp())
pulsoximeter.connect()





while 1:
    resp = pulsoximeter.getLiveData().next()
    rBloodSpO2 = resp.bloodSpO2
    rPulseRate = resp.pulseRate
    print hdb.uploadDataToTelejampiqDB([rBloodSpO2, rPulseRate, hdb.parseDateString(time.strftime("%c"))])
    time.sleep(0.5)

"""
hdb = HelperDB()


pulsoximeter = cms50dplus.CMS50Dplus(scanAvailableUSBDisp())
pulsoximeter.connect()

#statusLeds.onBusy()

def mainFunction():
    print pulsoximeter.getLiveData().next()



mainFunction()
"""
