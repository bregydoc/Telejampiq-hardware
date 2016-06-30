import RPi.GPIO as GPIO
from threading import *

class SimpleHardwareLeds:
    def __init__(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)

        self.redLed = 35
        self.greenLed = 33
        self.blueLed = 32
        self.ledsArray = [self.redLed, self.greenLed, self.blueLed]

        GPIO.setup(self.redLed, GPIO.OUT)
        GPIO.setup(self.greenLed, GPIO.OUT)
        GPIO.setup(self.blueLed, GPIO.OUT)



    def digitalWrite(self, pin, state = 1):
        if state==1:
            GPIO.output(pin, GPIO.HIGH)
        elif state==0:
            GPIO.output(pin, GPIO.LOW)
        else:
            return -1

    def onBusy(self):
        for i in range(len(self.ledsArray)):
            self.digitalWrite(self.ledsArray[i], 1)
        self.digitalWrite(self.blueLed, 0)

    def onError(self):
        for i in range(len(self.ledsArray)):
            self.digitalWrite(self.ledsArray[i], 1)
        self.digitalWrite(self.redLed, 0)

    def onOK(self):
        for i in range(len(self.ledsArray)):
            self.digitalWrite(self.ledsArray[i], 1)
        self.digitalWrite(self.greenLed, 0)

    def stopBusy(self):
        self.digitalWrite(self.blueLed, 1)
    def stopError(self):
        self.digitalWrite(self.redLed, 1)
    def noOk(self):
        self.digitalWrite(self.greenLed, 1)
