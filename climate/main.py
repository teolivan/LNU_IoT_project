import dht
import machine
from machine import ADC, Pin
import time

# pin setup
dht11 = dht.DHT11(machine.Pin(22))     # DHT11 Constructor 
ldr = ADC(Pin(27))                     #LDR Constructor
led = Pin("LED", Pin.OUT)              #LED Contstructor
mcp9700 = machine.ADC(26)              #MCP9700 Constructor

# MCP9700 characteristics
V0C = 0.5  # Voltage output from MCP9700 at 0°C (0.5V)
TCS = 0.01  # Temperature coefficient of MCP9700 (10mV/°C or 0.01V/°C)
VREF = 3.3  # Reference voltage from the system (Raspberry Pi Pico W) (3.3V)
MAX_ADC_VALUE = 65535  # Maximum value for a 16-bit ADC


while True:
    try:
        # DHT11
        dht11.measure()
       # temperature = dht11.temperature() <-- could measure this, but the MCP9700 sensor is more accurate than the DHT11 at measuring the temperature
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
