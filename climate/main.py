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

        time.sleep(2)

    except Exception as e:
        print(e)
 


# for sending data to Adafruit via MQTT

# BEGIN SETTINGS
# These need to be change to suit your environment
VALUES_INTERVAL = 20000    # milliseconds
last_values_sent_ticks = 0  # milliseconds
led = Pin("LED", Pin.OUT)   # led pin initialization for Raspberry Pi Pico W


# Callback Function to respond to messages from Adafruit IO
def sub_cb(topic, msg):          # sub_cb means "callback subroutine"
    print((topic, msg))          # Outputs the message that was received. Debugging use.
    if msg == b"ON":             # If message says "ON" ...
        led.on()                 # ... then LED on
    elif msg == b"OFF":          # If message says "OFF" ...
        led.off()                # ... then LED off
    else:                        # If any other message is received ...
        print("Unknown message") # ... do nothing but output that it happened.

# Function to generate a random number between 0 and the upper_bound
def random_integer(upper_bound):
    return random.getrandbits(32) % upper_bound

# Function to publish random number to Adafruit IO MQTT server at fixed interval
def send_values():
    global last_values_sent_ticks
    global VALUES_INTERVAL

    print("oefoeofoefojefojerkofekrfoke" )
    if ((time.ticks_ms() - last_values_sent_ticks) < VALUES_INTERVAL):
        return; # Too soon since last one sent.

    print("Publishing: {0} to {1} ... ".format(humidity, keys.AIO_HUMIDITIES_FEED), end='')
    print("Publishing: {0} to {1} ... ".format(temperature, keys.AIO_TEMPERATURES_FEED), end='')
    print("Publishing: {0} to {1} ... ".format(darkness, keys.AIO_DARKNESS_FEED), end='')

    try:
        client.publish(topic=keys.AIO_HUMIDITIES_FEED, msg=str(humidity))
        client.publish(topic=keys.AIO_TEMPERATURES_FEED, msg=str(temperature))
        client.publish(topic=keys.AIO_DARKNESS_FEED, msg=str(darkness))
        print("DONE")
    except Exception as e:
        print("FAILED")
    finally:
        last_values_sent_ticks = time.ticks_ms()


# Try WiFi Connection
try:
    ip = wifiConnection.connect()
except KeyboardInterrupt:
    print("Keyboard interrupt")

# Use the MQTT protocol to connect to Adafruit IO
client = MQTTClient(keys.AIO_CLIENT_ID, keys.AIO_SERVER, keys.AIO_PORT, keys.AIO_USER, keys.AIO_KEY)

# Subscribed messages will be delivered to this callback
client.set_callback(sub_cb)
client.connect()
client.subscribe(keys.AIO_LIGHTS_FEED)
print("Connected to %s, subscribed to %s topic" % (keys.AIO_SERVER, keys.AIO_LIGHTS_FEED))



try:                      # Code between try: and finally: may cause an error
                          # so ensure the client disconnects the server if
                          # that happens.
    while 1:              # Repeat this loop forever
        client.check_msg()# Action a message if one is received. Non-blocking.
        send_values()     # Send a random number to Adafruit IO if it's time.
finally:                  # If an exception is thrown ...
    client.disconnect()   # ... disconnect the client and clean up.
    client = None
    wifiConnection.disconnect()
    print("Disconnected from Adafruit IO.")