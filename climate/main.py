import dht
import machine
import time
from machine import ADC, Pin
from mqtt import MQTTClient   # For use of MQTT protocol to talk to Adafruit IO
import micropython            # Needed to run any MicroPython code
import random                 # Random number generator
import keys                   # Contain all keys used here
import wifiConnection         # Contains functions to connect/disconnect from WiFi 
from machine import Pin       # Define pin


# Pin setup
dht11 = dht.DHT11(machine.Pin(22))                              # DHT11 Constructor 
ldr = ADC(Pin(27))                                              # LDR Constructor
led = Pin("LED", Pin.OUT)                                       # LED Contstructor
mcp9700 = machine.ADC(26)                                       # MCP9700 Constructor
red = machine.Pin(19, machine.Pin.OUT)                          # LED 5mm red diffuse 1500mcd Constructor
green = machine.Pin(20, machine.Pin.OUT)                        # LED 5mm green diffuse 1500mcd Constructor
yellow = machine.Pin(21, machine.Pin.OUT)                       # LED 5mm yellow diffuse 1500mcd Constructor

leds = [green, yellow, red]
#humidityLED = 0
#lightLED = 0
#temperatureLED = 0

# MCP9700 characteristics
V0C = 0.5  # Voltage output from MCP9700 at 0°C (0.5V)
TCS = 0.01  # Temperature coefficient of MCP9700 (10mV/°C or 0.01V/°C)
VREF = 3.3  # Reference voltage from the system (Raspberry Pi Pico W) (3.3V)
MAX_ADC_VALUE = 65535  # Maximum value for a 16-bit ADC


# Menu - continues until valid input is received from user
while True: 
    print("--- Hello and welcome to the Climate Meter ---")
    print("Please choose which plant you want to monitor the health with: ")
    print("Press 1 for orchid, 2 for moss, and 3 for cactus")
    choice = input("Enter your choice:")

    if choice == "1" or choice == "2" or choice == "3": 
        break
    else: 
        print("Sorry, the input was not valid, please choose between 1, 2 or 3")


# Function for evaluating the humidity of the environment around the plant. Prints out an evaluation based on the values received from the DHT11 sensor
def humidityEvaluation(name, humidity, min_humidity, max_humidity, humidityLED):
    if min_humidity < humidity < max_humidity:
        humidityLED[0] = 0
        print("Humidity is " + str(humidity) + " which is good for a/an " + name)
    elif min_humidity * 0.9 < humidity < min_humidity:
        humidityLED[0] = 1
        print("Humidity is " + str(humidity) + " which is a little low for a/an " + name)
    elif humidity < min_humidity * 0.9:
        humidityLED[0] = 2
        print("Humidity is " + str(humidity) + " which is very low for a/an " + name)
    elif max_humidity < humidity < max_humidity * 1.1:
        humidityLED[0] = 1
        print("Humidity is " + str(humidity) + " which is a little high for a/an " + name)
    elif humidity > max_humidity * 1.1:
        humidityLED[0] = 2
        print("Humidity is " + str(humidity) + " which is very high for a/an " + name)


# Function for evaluating the darkness of the environment around the plant. Prints out an evaluation based on the values received from the LDR sensor    
def lightEvaluation(name, darkness, min_darkness, max_darkness, lightLED):
    if min_darkness < darkness < max_darkness:
        lightLED[0] = 0
        print("Darkness is " + str(darkness) + " which is good for a/an " + name)
    elif min_darkness * 0.9 < darkness < min_darkness:
        lightLED[0] = 1
        print("Darkness is " + str(darkness) + " which is not enough for a/an " + name)
    elif darkness < min_darkness * 0.9:
        lightLED[0] = 2
        print("Darkness is " + str(darkness) + " which is way too little for a/an " + name)
    elif max_darkness < darkness < max_darkness * 1.1:
        lightLED[0] = 1
        print("Darkness is " + str(darkness) + " which is a little much for a/an " + name)
    elif darkness > max_darkness * 1.1:
        lightLED[0] = 2
        print("Darkness is " + str(darkness) + " which is way too much for a/an " + name)


# Function for evaluating the temperature of the environment around the plant. Prints out an evaluation based on the values received from the MCP9700 sensor    
def temperatureEvaluation(name, temperature, min_temperature, max_temperature, temperatureLED):
    if min_temperature < temperature < max_temperature:
        temperatureLED[0] = 0
        print("Temperature is " + str(temperature) + " which is good for a/an " + name)
    elif min_temperature * 0.9 < temperature < min_temperature:
        temperatureLED[0] = 1
        print("Temperature is " + str(temperature) + " which is a little cold for a/an " + name)
    elif temperature < min_temperature * 0.9:
        temperatureLED[0] = 2
        print("Temperature is " + str(temperature) + " which is way too cold for a/an " + name)
    elif max_temperature < temperature < max_temperature * 1.1:
        temperatureLED[0] = 1
        print("Temperature is " + str(temperature) + " which is a little warm for a/an " + name)
    elif temperature > max_temperature * 1.1:
        temperatureLED[0] = 2
        print("Temperature is " + str(temperature) + " which is way too warm for a/an " + name)

# Function for lighting the LEDs based on the values from the evaluations above. Green lights up if all values are good, 
# yellow lights up if one or more values are a bit bad, red lights up if one or more values are really bad 
def ledEvaluation(humidityLED, lightLED, temperatureLED):
    if humidityLED[0] == 0 and lightLED[0] == 0 and temperatureLED[0] == 0:
        leds[0].toggle()
    elif (humidityLED[0] == 1 or lightLED[0] == 1 or temperatureLED[0] == 1) and (
            humidityLED[0] != 2 and lightLED[0] != 2 and temperatureLED[0] != 2):
        leds[1].toggle()
    elif humidityLED[0] == 2 or lightLED[0] == 2 or temperatureLED[0] == 2:
        leds[2].toggle()



# Main functionality of the program
humidityLED = [0]
lightLED = [0]
temperatureLED = [0]

min_humidity, max_humidity, name, min_darkness, max_darkness, min_temperature, max_temperature = 0, 0, "", 0, 0, 0, 0
global humidity, temperature, darkness  # Make sure these variables are declared as global



if choice == "1":
    min_humidity = 55
    max_humidity = 75
    name = "orchid"
    min_darkness = 40
    max_darkness = 50
    min_temperature = 20
    max_temperature = 32
elif choice == "2":
    min_humidity = 70
    max_humidity = 80
    name = "moss"
    min_darkness = 25
    max_darkness = 45
    min_temperature = 16
    max_temperature = 27
elif choice == "3":
    min_humidity = 40
    max_humidity = 60
    name = "cactus"
    min_darkness = 0
    max_darkness = 30
    min_temperature = 21
    max_temperature = 32


def send_values():
    print("Publishing data to Adafruit IO...")
    # Initialize MQTT client
    client = MQTTClient(keys.AIO_USER, keys.AIO_KEY, keys.AIO_SERVER)
    client.connect()

    try:
        client.publish(topic=keys.AIO_TEMPERATURES_FEED, msg=str(temperature))
        client.publish(topic=keys.AIO_HUMIDITIES_FEED, msg=str(humidity))
        client.publish(topic=keys.AIO_DARKNESS_FEED, msg=str(darkness))
        print("Data published successfully.")
    except Exception as e:
        print("Failed to publish data: ", e)
    finally:
        client.disconnect()


while True:
    try:
        # DHT11
        dht11.measure()
        humidity = dht11.humidity()
        humidityEvaluation(name, humidity, min_humidity, max_humidity, humidityLED)

        # LDR
        light = ldr.read_u16()
        darkness = round(light / 65535 * 100, 2)
        lightEvaluation(name, darkness, min_darkness, max_darkness, lightLED)

        # MCP9700
        temperature = round((mcp9700.read_u16() * VREF / MAX_ADC_VALUE - V0C) / TCS, 2)
        temperatureEvaluation(name, temperature, min_temperature, max_temperature, temperatureLED)

        ledEvaluation(humidityLED, lightLED, temperatureLED)

        time.sleep(5)
        send_values()

    except Exception as e:
        print(e)
 

