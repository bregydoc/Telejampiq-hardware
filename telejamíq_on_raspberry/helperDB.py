import requests
import time

class HelperDB:
    def __init__(self):
        self.url = "http://jfteledev.azurewebsites.net/api/Sensors"
        self.monthsAndYourNumbers = {'Jan' : 1,'Feb' : 2,'Mar' : 3,'Apr' : 4,'May' : 5,'Jun' : 6,'Jul' : 7,'Aug' : 8,'Sep' : 9, 'Oct' : 10,'Nov' : 11,'Dec' : 12}

    def getJsonOfSensors(self):
        r = requests.get(self.url)

        if r.status_code == 200:
            return r.json()
        else:
            return -1

    def removeDataOfDB(self, x):
        urlx = self.url + "/?id=" + str(x)
        r = requests.delete(urlx)

        if r.status_code == 200:
            return r.json()
        else:
            return -1

    def uploadDataToTelejampiqDB(self, data, autoId = True, id = 0):
        if autoId==True:
            idt = len(self.getJsonOfSensors()) + 1
        else:
            idt = id
        pulse = data[0]
        bloodSpO2 = data[1]
        fecha1 = self.parseDateString(time.strftime("%c"))
        fecha2 = data[2]
        dictToUpload = {"Id": idt, "valor1": pulse, "valor2": bloodSpO2, "fecha1": fecha1, "fecha2": fecha2}
        print dictToUpload
        r = requests.post(self.url, data = dictToUpload)
        return r.json

    def removeAllDataOfDB(self):
        jsonResp = self.getJsonOfSensors()
        size = len(jsonResp)
        for i in range(size):
            post = self.removeDataOfDB(jsonResp[i]["Id"])
            print post

    def parseDateString(self, data):
        dF = data.split(" ")
        return dF[len(dF)-1]+"-"+str(self.monthsAndYourNumbers[dF[1]])+"-"+dF[2]+dF[0][0]+dF[3]
