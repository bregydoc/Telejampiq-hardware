
import RPi.GPIO as GPIO
import time
from threading import Thread


class HardwareLedRpi:
    def __init__(self, initThreads = False):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)

        GPIO.setup(32, GPIO.OUT)
        GPIO.setup(33, GPIO.OUT)
        GPIO.setup(35, GPIO.OUT)

        self.blue = GPIO.PWM(32, 100)
        self.green = GPIO.PWM(33, 100)
        self.red = GPIO.PWM(35, 100)

        self.blue.start(100.0)
        self.green.start(100.0)
        self.red.start(100.0)

    	self.onBusyFlag = False
    	self.onErrorFlag = False


    	self.busyThread = Thread(target=self.busy)
    	self.errorThread = Thread(target=self.error)

        if initThreads:
            self.runThreads()


    def runThreads(self):
        self.busyThread.start()
        self.errorThread.start()


    def startAll(self):
        self.blue.start(100.0)
        self.green.start(100.0)
        self.red.start(100.0)

    def cleanAll(self):
        self.red.stop()
        self.blue.stop()
        self.green.stop()

        GPIO.cleanup(32)
        GPIO.cleanup(35)
        GPIO.cleanup(33)


    def busy(self):
        vel = 1
    	while True:
    		while self.onBusyFlag:
    		    for i in range(0,100, vel):
    		        self.blue.ChangeDutyCycle(i)
    		        time.sleep(0.009)

        		time.sleep(0.1)

    		    for i in range(100, 0, -1*vel):
    		        self.blue.ChangeDutyCycle(i)
                    time.sleep(0.009)

            while not self.onBusyFlag:
    		    time.sleep(0.5)


    def error(self):
    	vel = 1
    	while True:
    		while self.onErrorFlag:
    		    for i in range(0,100, vel):
    		        self.red.ChangeDutyCycle(i)
    		        time.sleep(0.009)


    			time.sleep(0.1)


    		    for i in range(100, 0, -1*vel):
    		        self.red.ChangeDutyCycle(i)
    		        time.sleep(0.009)

    		while not self.onErrorFlag:
    			time.sleep(0.5)


    def onBusy(self):
    	self.blue.start(100.0)
    	self.onBusyFlag = True

    def stopBusy(self):
    	self.onBusyFlag = False
    	#self.blue.ChangeDutyCycle(100.0)
    	self.blue.stop()
    	GPIO.cleanup(32)
    	#self.cleanAll()

    def onError(self):

    	self.red.start(100.0)
    	self.onErrorFlag = True

    def stopError(self):
    	self.onErrorFlag = False
    	#self.red.ChangeDutyCycle(100.0)
    	self.red.stop()
    	GPIO.cleanup(35)
    	#self.cleanAll()

    def onStart(self):
        self.green.ChangeDutyCycle(0.0)

    def turnOfPrincipalLight(self):
    	self.green.stop()
    	GPIO.cleanup(33)


"""
EXAMPLE OF USE:

h = HardwareLedRpi()

h.onError()
time.sleep(4)
h.onBusy()
time.sleep(4)
h.stopBusy()
h.onStart()
time.sleep(4)
h.turnOfPrincipalLight()


import atexit
atexit.register(h.cleanAll)
"""
