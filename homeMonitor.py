import requests
import json
import cherrypy


def getTemp ():
    requestTemp = requests.get("https://api.spark.io/v1/devices/***REMOVED***/tempf?access_token=***REMOVED***")
    tempf = json.loads(requestTemp.text)
    theTemp = "{:.1f}".format(tempf["result"])
    return theTemp
    # return str(tempf["result"])
    
def getHum():
    requestHum = requests.get("https://api.spark.io/v1/devices/***REMOVED***/humidity?access_token=***REMOVED***")
    humidity = json.loads(requestHum.text)
    theHumidity = "{:.1f}".format(humidity["result"])
    return theHumidity

def writeTemps():
    f = open("temps.json", mode='w')
    json.dump({'temp': getTemp(), 'hum': getHum()}, f, indent=4)
    f.close()


class TempPage(object):
    @cherrypy.expose
    def index(self):
        return file('index.html')

    @cherrypy.expose
    def sense(self):
        return json.dumps({'temp': getTemp(), 'hum': getHum()}, indent=4)




if __name__ == '__main__':
    cherrypy.config.update(
    {'server.socket_host': '0.0.0.0'} )
    cherrypy.config.update({'server.socket_port': 8085})
    cherrypy.quickstart(TempPage())

    while True:
        getTemp()
        getHumidity()
        writeTemps()
        time.sleep(5000)
