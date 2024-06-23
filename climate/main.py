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

leds = [green, yellow, red]
max_humidity = 0
min_humidity = 0

# MCP9700 characteristics
V0C = 0.5  # Voltage output from MCP9700 at 0°C (0.5V)
TCS = 0.01  # Temperature coefficient of MCP9700 (10mV/°C or 0.01V/°C)
VREF = 3.3  # Reference voltage from the system (Raspberry Pi Pico W) (3.3V)
MAX_ADC_VALUE = 65535  # Maximum value for a 16-bit ADC

# Menu 
print("--- Hello and welcome to the Climate Meter ---")
while True: 
    print("Please choose which plant you want to monitor the health with: ")
    print("Press 1 for orchid, 2 for moss, and 3 for cactus")
    choice = input("Enter your choice:")

    if choice == "1" or choice == "2" or choice == "3": 
        break
    else: 
        print("Sorry, the input was not valid, please choose between 1, 2 or 3")




def humidityEvaluation(name, humidity, min_humidity, max_humidity): 
    if humidity > min_humidity and humidity < max_humidity:
        leds[0].toggle()
        print("Humidity is " + str(humidity) + " which is good for a/an " + name)
    elif humidity < min_humidity and humidity > (min_humidity * 0.9): 
        leds[1].toggle()
        print("Humidity is " + str(humidity) + " which is a little low for a/an " + name)
    elif humidity < (min_humidity * 0.9): 
        leds[2].toggle()
        print("Humidity is " + str(humidity) + " which is very low for a/an " + name)
    elif humidity > max_humidity and humidity < (max_humidity * 1.1):
        leds[1].toggle()
        print("Humidity is " + str(humidity) + " which is a little high for a/an " + name)
    elif humidity > (max_humidity * 1.1): 
        leds[2].toggle()
        print("Humidity is " + str(humidity) + " which is very low for a/an " + name) 

    
def lightEvaluation(name, darkness, min_darkness, max_darkness):
    if darkness > min_darkness and darkness < max_darkness:
        leds[0].toggle()
        print("Darkness is " + str(darkness) + " which is good for a/an " + name)
    elif darkness < min_darkness and darkness > (min_darkness * 0.9): 
        leds[1].toggle()
        print("Darkness is " + str(darkness) + " which is not enough for a/an " + name)
    elif darkness < (min_darkness * 0.9): 
        leds[2].toggle()
        print("Darkness is " + str(darkness) + " which is way too little for a/an " + name)
    elif darkness > max_darkness and darkness < (max_darkness * 1.1):
        leds[1].toggle()
        print("Darkness is " + str(darkness) + " which is a little much for a/an " + name)
    elif darkness > (max_darkness * 1.1): 
        leds[2].toggle()
        print("Darkness is " + str(darkness) + " which is way too much for a/an " + name) 




# Main functionality of the program for the orchid choice
if choice == "1":
    min_humidity = 55 # https://www.justaddiceorchids.com/orchid-care-blog/just-add-ice-orchid-blog/bid/98302/how-does-humidity-affect-my-orchid
    max_humidity = 75 # https://www.justaddiceorchids.com/orchid-care-blog/just-add-ice-orchid-blog/bid/98302/how-does-humidity-affect-my-orchid
    name = "orchid"
    min_darkness = 40 # https://planterhoma.com/blogs/orchid-care/orchid-light-requirement
    max_darkness = 50 # https://planterhoma.com/blogs/orchid-care/orchid-light-requirement
    while True:
        try:
            # DHT11
            dht11.measure()
            # temperature = dht11.temperature() <-- could measure this, but the MCP9700 sensor is more accurate than the DHT11 at measuring the temperature
            # delta between dht11 and mcp9700 check value for temp, compare 
            humidity = dht11.humidity()
            humidityEvaluation(name, humidity, min_humidity, max_humidity)

            # LDR
            light = ldr.read_u16()
            darkness = round(light / 65535 * 100, 2)
            lightEvaluation(name, darkness, min_darkness, max_darkness)
            
            #MCP9700
            raw_adc_value = mcp9700.read_u16() # Read the raw ADC value (16-bit)
            voltage = (raw_adc_value / MAX_ADC_VALUE) * VREF # Convert the raw ADC value to voltage
            temperature = (voltage - V0C) / TCS # Temperature in Celsius
            print("Temperature: {:.2f} °C".format(temperature))

        except Exception as error:
            print("Exception occurred", error)
        time.sleep(1)

# Main functionality of the program for the moss choice
elif choice == 2: 
    min_humidity = 70 # https://mossclerks.co.uk/pages/moss-caring-guide
    max_humidity = 80 # https://mossclerks.co.uk/pages/moss-caring-guide
    name = "moss"
    min_darkness = 25 # https://greg.app/hypnum-moss-light-requirements/
    max_darkness = 45 # https://greg.app/hypnum-moss-light-requirements/
    while True:
        try:
            # DHT11
            dht11.measure()
            # temperature = dht11.temperature() <-- could measure this, but the MCP9700 sensor is more accurate than the DHT11 at measuring the temperature
            # delta between dht11 and mcp9700 check value for temp, compare 
            humidity = dht11.humidity()
            humidityEvaluation(name, humidity, min_humidity, max_humidity)

             # LDR
            light = ldr.read_u16()
            darkness = round(light / 65535 * 100, 2)
            lightEvaluation(name, darkness, min_darkness, max_darkness)
                 
            #MCP9700
            raw_adc_value = mcp9700.read_u16() # Read the raw ADC value (16-bit)
            voltage = (raw_adc_value / MAX_ADC_VALUE) * VREF # Convert the raw ADC value to voltage
            temperature = (voltage - V0C) / TCS # Temperature in Celsius
            print("Temperature: {:.2f} °C".format(temperature))

        except Exception as error:
            print("Exception occurred", error)
            time.sleep(1)

# Main functionality of the program for the cactus choice
elif choice == 3:  
    min_humidity = 40 # https://www.justaddiceorchids.com/orchid-care-blog/just-add-ice-orchid-blog/bid/98302/how-does-humidity-affect-my-orchid
    max_humidity = 60 # https://www.justaddiceorchids.com/orchid-care-blog/just-add-ice-orchid-blog/bid/98302/how-does-humidity-affect-my-orchid
    name = "cactus"
    min_darkness = 0 # https://www.gardenhealth.com/advice/plants-flowers/how-to-care-for-cacti-and-succulents
    max_darkness = 30 # https://www.gardenhealth.com/advice/plants-flowers/how-to-care-for-cacti-and-succulents
    while True:
        try:
            # DHT11
            dht11.measure()
            # temperature = dht11.temperature() <-- could measure this, but the MCP9700 sensor is more accurate than the DHT11 at measuring the temperature
            # delta between dht11 and mcp9700 check value for temp, compare 
            humidity = dht11.humidity()
            humidityEvaluation(name, humidity, min_humidity, max_humidity)

            # LDR
            light = ldr.read_u16()
            darkness = round(light / 65535 * 100, 2)
            lightEvaluation(name, darkness, min_darkness, max_darkness)
            
            #MCP9700
            raw_adc_value = mcp9700.read_u16() # Read the raw ADC value (16-bit)
            voltage = (raw_adc_value / MAX_ADC_VALUE) * VREF # Convert the raw ADC value to voltage
            temperature = (voltage - V0C) / TCS # Temperature in Celsius
            print("Temperature: {:.2f} °C".format(temperature))

        except Exception as error:
            print("Exception occurred", error)
            time.sleep(1)





