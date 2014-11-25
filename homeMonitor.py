
import sleep
import requests
import json
import cherrypy


//temp = requests.get("https://api.spark.io/v1/devices/***REMOVED***/tempf?access_token=***REMOVED***")
//hum = requests.get("https://api.spark.io/v1/devices/***REMOVED***/humidity?access_token=***REMOVED***")
//tempf = json.loads(temp.text)
//humidity = json.loads(hum.text)

def getTemp ():
    temp = requests.get("https://api.spark.io/v1/devices/***REMOVED***/tempf?access_token=***REMOVED***")
    tempf = json.loads(temp.text)
    return str(tempf["result"])
    
def getHum():
    hum = requests.get("https://api.spark.io/v1/devices/***REMOVED***/humidity?access_token=***REMOVED***")
    humidity = json.loads(hum.text)
    return str(humidity["result])


class TempPage(object):
    @cherrypy.expose
    def index(self):
        htmlpage = \
        """<html>
          <head></head>
          <body>
            <h1>Current Temp: {0!s}</h1>
            <h1>Current Humidity {1!s}</h1>
          </body>
        </html>"""
        return htmlpage.format(getTemp(), getHum())


if __name__ == '__main__':
    cherrypy.quickstart(TempPage())
    while True:
        getTemp()
        getHumidity()
        time.sleep(5000)
