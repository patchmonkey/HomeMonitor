// This #include statement was automatically added by the Spark IDE.
#include "HTU21D/HTU21D.h"

// This #include statement was automatically added by the Spark IDE.
#include "MCP9808/MCP9808.h"




/*
Spark Core MCP9808 Temperature Sensor Library
By: Romain MP
Licence: GPL v3
*/


double tempf, tempc, humidity, alttemp;

MCP9808 mcp = MCP9808();
HTU21D htu = HTU21D();

void setup()
{
	Serial.begin(9600);
    
    delay(5000);
    
	Serial.println("MCP9808 test");

	while(! mcp.begin()){
	    Serial.println("MCP9808 not found");
	    delay(500);
	}
	
		while(! htu.begin()){
	    Serial.println("HTU21D not found");
	    delay(1000);
	}

	
	mcp.setResolution(MCP9808_SLOWEST);

	Serial.println("MCP9808 OK");
	Serial.println("HTU21D OK");
	Spark.variable("tempf", &tempf, DOUBLE);
	Spark.variable("humidity", &humidity, DOUBLE);
}

void loop()
{
   
    
    tempc = mcp.getTemperature();
    tempf = (9.0/5) * tempc + 32;
    humidity = htu.readHumidity();
    alttemp = htu.readTemperature();
    Serial.println("===================");
    Serial.print("Temp in F: "); Serial.println(tempf, 2);
	Serial.print("Temp in C: "); Serial.println(mcp.getTemperature(), 2);
	Serial.print("Hum: "); Serial.println(humidity);
	Serial.print("Alternative Temp: "); Serial.println(alttemp, 2);
	delay(5000);
}
