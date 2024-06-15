import dht
import machine
from machine import ADC, Pin
import time

# pin setup
dht11 = dht.DHT11(machine.Pin(22))     # DHT11 Constructor 
ldr = ADC(Pin(27))                     #LDR Constructor
led = Pin("LED", Pin.OUT)              #LED Contstructor


while True:
    try:
        dht11.measure()
       # temperature = dht11.temperature() <-- could measure this, but the MCP9700 sensor is more accurate than the DHT11 at measuring the temperature
        humidity = dht11.humidity()
        print("Humidity is " + str(humidity))
        light = ldr.read_u16()
        darkness = round(light / 65535 * 100, 2)
        if darkness >= 70:
            print("Darkness is {}%, LED turned on".format(darkness))
            led.on()
        else:
            print("It is enough light, no need to turn the LED on")
            led.off()
    except Exception as error:
        print("Exception occurred with humidity sensor DHT11", error)
    time.sleep(1)



