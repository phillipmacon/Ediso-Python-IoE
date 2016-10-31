#From the library, import the main class
#Note, it would need to be in the same folder or in the python PATH

#import the LCD class
from I2cLCDRGBBacklight import I2CLCDDisplay

#import the TH02 temperature and humidity sensor class
from TH02 import TH02

#Import time from the core python library
import time

#Setup thingspeak cloudplatform
import thingspeak #If thingspeak not found please goover the thingspeak power point to install this on your edison

channel_id  = "" # PUT CHANNEL ID HERE
write_key   = "" # PUT YOUR WRITE KEY HERE
thingspeak.Channel(id=channel_id,write_key=write_key)

#Create an instance of I2CLCDDisplay and call it LCDDisplay
LCDDisplay = I2CLCDDisplay()
#available functions
# LCDDisplay.LEDColor(255,255,255)         #RGB Set the background LCD color with values from 0-255 per color
# LCDDisplay.LCDPrint("Hello World!!!")    #Print text to the display
# LCDDisplay.LCDInstruction(0x80 + 0x00)   #Set the cursor to the start of the first line
# LCDDisplay.LCDInstruction(0x80 + 0x28)   #Set the cursor to the start of the second line

#Create an instance of TH02 and call it TH02 sensor
TH02Sensor = TH02()
# TH02Sensor.getTemperature()             # Return the temperature
# str(TH02Sensor.getTemperature())        # Use str() to convert to a string value so it can be used for the LCD

#Declare Digital inputs
#(Create the code here)
#(Declare button variable and direction)

#Declare Analog inputs
#(create the code here)
#(declare UV sensor variable and port)
#(declare Soil humidity sensor variable and port)
#(declare light sensor variable and port)

#Print your name and date 
#(Use the LCD functions to print your name)
#Display this for a few seconds

#Loop that runs through different sensor values
i=1 #this variable is used to cycle through the different sensors when the button is pressed this will be increased by 1
while True:
    #This code is used to increment i with 1
    if(button.read() == 1): #This will be true if the button is pressed
      i+=1                  #Increment i with 1 to continue to the next sensor
    
    while(i==1):
        #(Display the value of the UV sensor here)
        
        #(Copy the code to register when the button is pressed to progress to the next sensor readout)
        
    while(i==2):
        #(Display the value of the Light sensor here)
        
        #(Copy the code to register when the button is pressed to progress to the next sensor readout)
        
    while(i==3):
        #(Display the value of the Soil Humidity sensor here)
        
        #(Copy the code to register when the button is pressed to progress to the next sensor readout)
        
    while(i==4):
        #(Display the temperature and humidity here using the TH02 functions)
        
        #(Copy the code to register when the button is pressed to progress to the next sensor readout)    

    
     while(i==5):
        #(Upload the data to thingspeak)
        #(Display uploading to thingspeak)
        
        #(put the temperature in a variable)
        # Field1 = variable 
        #(put the humidity in a variable)
        # Field2 = variable
        #(put the UV sensor value in a variable)
        # Field3 = variable
        #(put the soil humidity sensor value in a variable)
        # Field4 = variable
        #(put the light sensor value in a variable)
        # Field5 = variable
        
        #This will update thingspeak
        channel.update({1:Field1, 2:Field2,  3:Field3,  4:Field4,  5:Field5})

        #When the button is pressed i will be 1 and it will start cycling through the first sensor again
        if(button.read() == 1): #
			      i = 1

        







