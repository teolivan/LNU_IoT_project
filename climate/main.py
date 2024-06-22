import dht
import machine
import time
from machine import ADC, Pin
#from picozero import LED

# pin setup
dht11 = dht.DHT11(machine.Pin(22))     # DHT11 Constructor 
ldr = ADC(Pin(27))                     # LDR Constructor
led = Pin("LED", Pin.OUT)              # LED Contstructor
mcp9700 = machine.ADC(26)              # MCP9700 Constructor
red = machine.Pin(19, machine.Pin.OUT)                          # LED 5mm red diffuse 1500mcd Constructor
green = machine.Pin(20, machine.Pin.OUT)                         # LED 5mm green diffuse 1500mcd Constructor
yellow = machine.Pin(21, machine.Pin.OUT)                        # LED 5mm yellow diffuse 1500mcd Constructor


# MCP9700 characteristics
V0C = 0.5  # Voltage output from MCP9700 at 0°C (0.5V)
TCS = 0.01  # Temperature coefficient of MCP9700 (10mV/°C or 0.01V/°C)
VREF = 3.3  # Reference voltage from the system (Raspberry Pi Pico W) (3.3V)
MAX_ADC_VALUE = 65535  # Maximum value for a 16-bit ADC


while True:
    try:
        yellow.toggle()
        green.toggle()
        
        red.toggle()
        # DHT11
        dht11.measure()
       # temperature = dht11.temperature() <-- could measure this, but the MCP9700 sensor is more accurate than the DHT11 at measuring the temperature
       # delta between dht11 and mcp9700 check value for temp, compare 
        humidity = dht11.humidity()
        print("Humidity is " + str(humidity))

        # LDR
        light = ldr.read_u16()
        darkness = round(light / 65535 * 100, 2)
        if darkness >= 70:
            print("Darkness is {}%, LED turned on".format(darkness))
            led.on()
        else:
            print("It is enough light, no need to turn the LED on")
            led.off()
        
        #MCP9700
        raw_adc_value = mcp9700.read_u16() # Read the raw ADC value (16-bit)
        voltage = (raw_adc_value / MAX_ADC_VALUE) * VREF # Convert the raw ADC value to voltage
        temperature = (voltage - V0C) / TCS # Temperature in Celsius
        print("Temperature: {:.2f} °C".format(temperature))

    except Exception as error:
        print("Exception occurred", error)
    time.sleep(1)



