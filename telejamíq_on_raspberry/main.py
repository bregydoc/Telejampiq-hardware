import cms50dplus
import time
import os
import random
import commands
import sys

#from control_led import HardwareLedRpi
from simpleControlLed import SimpleHardwareLeds
from helperDB import HelperDB

def scanAvailableUSBDisp():
    r = commands.getstatusoutput('ls /dev/ttyUSB*')
    size = len(r)
    return r[1]


hdb = HelperDB()
pulsoximeter = cms50dplus.CMS50Dplus(scanAvailableUSBDisp())
sLeds = SimpleHardwareLeds()
pulsoximeter.connect()

sLeds.onBusy()


i = 0
def mainLoop():
    global i
    i+=1
    print "Iteracion numero " + str(i)
    try:
        while 1:
            sLeds.onBusy()
            r = pulsoximeter.getLiveData().next()
            sLeds.onOK()
            bSpO2 = r.bloodSpO2
            pulse = r.pulseRate
            if (not pulse==0) and (not bSpO2==0):
                currentTime = r.time
                requestPost = hdb.uploadDataToTelejampiqDB([bSpO2, pulse, hdb.parseDateString(time.strftime("%c"))])
                if requestPost.status_code==200 or requestPost.status_code==201:
                    print "UPLOAD OK"
                else:
                    print "UPLOAD FAILED"
            time.sleep(0.5)
    except Exception as e:
        sLeds.onError()
        time.sleep(0.2)
        mainLoop()
            print e


mainLoop()


"""
sLeds.onError()
while 1:
    resp = pulsoximeter.getLiveData().next()
    rBloodSpO2 = resp.bloodSpO2
    rPulseRate = resp.pulseRate
    print hdb.uploadDataToTelejampiqDB([rBloodSpO2, rPulseRate, hdb.parseDateString(time.strftime("%c"))])
    time.sleep(0.5)

"""
"""
hdb = HelperDB()


pulsoximeter = cms50dplus.CMS50Dplus(scanAvailableUSBDisp())
pulsoximeter.connect()

#statusLeds.onBusy()

def mainFunction():
    print pulsoximeter.getLiveData().next()



mainFunction()
"""
