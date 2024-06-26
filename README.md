# Linneaus University Internet of Things Project

+ **Climate Measurer**
+ **Olivia Svensson - os222ui**
+ **Climate meter - measuring temperature, light, and humidity.**
+ **Approximate time taken to do this project: approximately 25hrs**


## Objective
Describe why you have chosen to build this specific device. What purpose does it serve? What do you want to do with the data, and what new insights do you think it will give?
### Why you chose the project
I chose this project because of a desire to create a device with multiple sensors as well as actuators. I came to the conclusion that a device which can measure the climate and give insights as to the metrics would be highly useful for several purposes. 
### What purpose does it serve
The project serves the purpose of gaining data from the current environment surrounding the microcontroller (as well as the sensors and actuators) in order to get valuable insights about the current climate. This device will alert the user if the humidity, light, or temperature goes above or below an unhealthy level. The user is alerted by LEDs which signal every second depending on the sensor data. The values can be adjusted depending on what you would like to monitor (it could be different kinds of plants, yourself, or a bird for example).
### What insights you think it will give
The project will give me a better insight into how microcontrollers work. It will broaden my understanding of communication protocols, and how microcontrollers can communicate with sensors and actuators. Using the device will allow the user to gain insights as to their environment. This is often something which is ignored, so the Climate Measurer will likely provide new insights as to how the environment around you is. 

## Material 
The material list is provided below. All of the components used for the project are linked here with an image, as well as their price, the amount needed, and the link for purchasing. 
### List of material
| Amount | Component | Price | Available at | Image |
| ------------- | ------------- | ------------- | ------------- | ------------- |
| 1x | Raspberry Pi Pico WH | 109kr | https://www.electrokit.com/raspberry-pi-pico-wh | <img src="https://www.electrokit.com/cache/ba/700x700-product_41019_41019114_PICO-WH-HERO.jpg" alt="Raspberry Pi Pico WH" width="100" height="100"/> |
| 1x | Breadboard | 69kr | https://www.electrokit.com/kopplingsdack-840-anslutningar | <img src="https://www.electrokit.com/upload/product/10160/10160840/10160840.jpg" alt="Breadboard" width="100" height="100"/> |
| 1x | USB cable A male - micro B male 1.8m | 39kr | https://www.electrokit.com/usb-kabel-a-hane-micro-b-5p-hane-1.8m | <img src="https://www.electrokit.com/cache/ad/700x700-quick_54_1f_9382_41003290.png" alt="USB Cable A" width="100" height="100"/> |
| 1x (used 17 out of 20) | Lab cable 40-pin 30cm male/male | 49kr | https://www.electrokit.com/labbsladd-40-pin-30cm-hane/hane | <img src="https://www.electrokit.com/cache/24/700x700-product_41012_41012684_41012684.jpg" alt="Lab Cables" width="100" height="100"/> |
| 1x | LED 5mm red diffuse 1500mcd | 5kr | https://www.electrokit.com/led-5mm-rod-diffus-1500mcd | <img src="https://www.electrokit.com/upload/product/40307/40307020/40300051.jpg" alt="Red LED" width="100" height="100"/> |
| 1x | LED 5mm yellow diffuse 1500mcd | 5kr | https://www.electrokit.com/led-5mm-gul-diffus-1500mcd | <img src="https://www.electrokit.com/upload/product/40307/40307021/40300053.jpg" alt="Yellow LED" width="100" height="100"/> |
| 1x | LED 5mm green diffuse 1500mcd | 5kr | https://www.electrokit.com/led-5mm-gron-diffus-80mcd | <img src="https://www.electrokit.com/upload/product/40307/40307023/40300054.jpg" alt="Green LED" width="100" height="100"/> |
| 1x | Photoresistor CdS 4-7 kohm | 8kr | https://www.electrokit.com/fotomotstand-cds-4-7-kohm | <img src="https://www.electrokit.com/upload/product/40850/40850001/40850001.jpg" alt="Photoresistor" width="100" height="100"/> |
| 1x | MCP9700 TO-92 Temperature Sensor | 12kr | https://www.electrokit.com/mcp9700-to-92-temperaturgivare | <img src="https://www.electrokit.com/upload/product/41011/41011628/41010569.jpg" alt="Temperature Sensor" width="100" height="100"/> |
| 1x | Digital temperature and humidity sensor DHT11 | 49kr | https://www.electrokit.com/digital-temperatur-och-fuktsensor-dht11 | <img src="https://www.electrokit.com/upload/product/41015/41015728/41015728.jpg" alt="Digital Temperature and Humidity Sensor" width="100" height="100"/> |
| 1x | Resistor carbon film 0.25W 470ohm (470R) | 1kr | https://www.electrokit.com/cache/82/700x700-product_40810_40810247_40810247.png | <img src="https://www.electrokit.com/cache/82/700x700-product_40810_40810247_40810247.png" alt="Resistor 470ohm" width="100" height="100"/> |
+ All of these materials can be found within the starterkit which Electrokit provides for 399kr https://www.electrokit.com/lnu-starter.

### What the different things (sensors, wires, controllers) do - short specifications
The Raspberry Pi Pico W is a microcontroller which essentially is a small computer. The microcontroller is the so called master, controlling all of the other components (slaves), acting as the brain. The breadboard makes it easier for me to connect all of the actuators and sensors with the microcontroller, as it provides slots for the different devices to be inserted into, and makes the task of connecting the devices together with wires less messy. The wires are used for connecting the components to the microcontroller (both to the different pins, the ground, and the power source). The DHT11 is used for measuring the humidity in this project, but can also be used for measuring the temperature. The MCP9700 is a temperature sensor used for measuring the temperature. The LCD is used for measuring the light. The resistor is used to control the current which flows through to the LCD. The resistor lessens the amount of current, and protects the device (LCD) from being damaged by the current. 

## Computer Setup 
I am creating this project running the Windows 11 operating system. This is for personal preference, you can use your preferred OS. 
In order to flash the Pico WH, you need to connect the USB cable to the Pico WH. Then you need to press the BOOTSEL button on the Pico which is an oval white button, and hold it. Plug in the USB cable into your computer while still holding down the BOOTSEL button. Open up the device. Go to this page: https://micropython.org/download/RPI_PICO_W/ and download the latest firmware. Drag the downloaded file into the device. The window should automatically close. After this, you have successfully installed the firmware! 
### Chosen IDE
The IDE I chose is Visual Studio Code. Visual Studio Code, or VSCode is one of the most popular IDEs for software development. I chose it because I am comfortable with the IDE as I have previous experience programming in it. You can download VSCode here: https://code.visualstudio.com/download 

### How the code is uploaded
### Steps that you needed to do for your computer. Installation of Node.js, extra drivers, etc.
Node.js can be downloaded here: https://nodejs.org/en/download/package-manager
In VSCode, go to extensions and then search for "Pymakr", then click install. Pymakr is what we will be using when running the code in VSCode. Create a new Pymakr project by pressing the new icon for Pymakr which appeared, and then press "Create project". Create a new folder to hold the project. Enter the name for the project in the window at the top, click empty (as this is a new project). Select your Pico W device. It is possible that it shows up as some other name than that under "Device". Once you have done this, you are ready to start programming.

## Putting Everything Together
How is all the electronics connected? Describe all the wiring, good if you can show a circuit diagram. Be specific on how to connect everything, and what to think of in terms of resistors, current and voltage. Is this only for a development setup or could it be used in production?
<img src="https://github.com/teolivan/LNU_IoT_project/blob/main/circuit_diagram/lnu_iot.png?raw=true" alt="wiring for the project"> 
![image](https://github.com/teolivan/LNU_IoT_project/assets/74550333/9c38ebdc-695e-4d12-8d54-0cf4df0716f5)
![image](https://github.com/teolivan/LNU_IoT_project/blob/main/images/unnamed%20(6).jpg?raw=true) 
### Circuit diagram
<img src="https://github.com/teolivan/LNU_IoT_project/blob/main/circuit_diagram/lnu_iot_schematic.png?raw=true" alt="schematic for the project"> 

### *Electrical calculations

## Platform
Describe your choice of platform. If you have tried different platforms it can be good to provide a comparison.
### Describe platform in terms of functionality
### *Explain and elaborate what made you choose this platform

## The code
Import core functions of your code here, and don't forget to explain what you have done! Do not put too much code here, focus on the core functionalities. Have you done a specific function that does a calculation, or are you using clever function for sending data on two networks? Or, are you checking if the value is reasonable etc. Explain what you have done, including the setup of the network, wireless, libraries and all that is needed to understand.\

![image](https://github.com/teolivan/LNU_IoT_project/blob/main/images/main%20functionality.png?raw=true) 

## Transmitting the Data / Connectivity
How is the data transmitted to the internet or local server? Describe the package format. All the different steps that are needed in getting the data to your end-point. Explain both the code and choice of wireless protocols.
![image](https://github.com/teolivan/LNU_IoT_project/blob/main/images/connect.png?raw=true)
![image](https://github.com/teolivan/LNU_IoT_project/blob/main/images/senddata.png?raw=true)
### How often is the data sent?
### Which wireless protocols did you use (WiFi, LoRa, etc …)?
### Which transport protocols were used (MQTT, webhook, etc …)
### *Elaborate on the design choices regarding data transmission and wireless protocols. That is how your choices affect the device range and battery consumption.

## Presenting the Data
This part covers the visualization of the data. 
### Provide visual examples on how the dashboard looks. Pictures needed.
![image](https://github.com/teolivan/LNU_IoT_project/blob/main/images/dashboard.png?raw=true) 
The dashboard has three feeds. One for humidity, one for temperature, and one for the levels of light. All three feeds are presented as linear graphs as this helps visualize the data. 
### How often is data saved in the database.
The data is saved every five seconds to the database. Due to the limits of transmitting data to the feeds put in place by Adafruit IO, and as I had three feeds, I could not publish to all three feeds at the same time. In order to tackle this issue, I put a two second timer between each publishing of the data to the client. Adafruit IO keeps the values in the database for 30 days, and then eventually deletes it. 
### *Explain your choice of database.
I chose to go with Adafruit IO. I am storing the data in feeds. The data can easily be downloaded if needed. I chose Adafruit IO as I initally tried a TIG stack solution where I was supposed to use an InfluxDB database. I had issues however with connecting the database with Grafana, which I could not manage to resolve, so I settled for an easier solution. Adafruit IO is very user friendly, and much easier to set up. This was the reason for the choice of database.
### *Automation/triggers of the data.
![image](https://github.com/teolivan/LNU_IoT_project/blob/main/images/discordpic.png?raw=true)
I activated a webhook link on the temperature values. If the value exceeds 30 degrees celsius, the value will be forwarded to the Discord server I set up. This will be done once every 20 minutes. 

## Finalizing the Design
Show the final results of your project. Give your final thoughts on how you think the project went. What could have been done in an other way, or even better? Pictures are nice!
### Show final results of the project
### Pictures
![image](https://github.com/teolivan/LNU_IoT_project/blob/main/images/unnamed%20(8).jpg?raw=true)
### *Video presentation
Below is a link to a presentation of the system with an explanation and live demo showing how it works. 
[![YouTube](http://i.ytimg.com/vi/HP2NcklRaZ4/hqdefault.jpg)](https://www.youtube.com/watch?v=HP2NcklRaZ4)
