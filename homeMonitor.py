import requests
import json
import cherrypy


def getTemp ():
    requestTemp = requests.get("https://api.particle.io/v1/devices/<your-key-here>/tempf?access_token=<your-access-token>")
    tempf = json.loads(requestTemp.text)
    theTemp = "{:.1f}".format(tempf["result"])
    return theTemp
    # return str(tempf["result"])
    
def getHum():
    requestHum = requests.get("https://api.particle.io/v1/devices/<your-key-here>/humidity?access_token=<your-access-token>")
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
