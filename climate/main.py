import dht
import machine
import time

dht11 = dht.DHT11(machine.Pin(22))     # DHT11 Constructor 


while True:
    try:
        dht11.measure()
       # temperature = dht11.temperature() <-- could measure this, but the MCP9700 sensor is more accurate than the DHT11 at measuring the temperature
        humidity = dht11.humidity()
        print("Humidity is " + str(humidity))
    except Exception as error:
        print("Exception occurred with humidity sensor DHT11", error)
    time.sleep(1)