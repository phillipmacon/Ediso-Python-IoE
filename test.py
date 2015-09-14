#From the library, import the main class
#Note, it would need to be in the same folder or in the python PATH
from I2CLCDDisplay import I2CLCDDisplay
#From the library, import the main class
import time

#Create an instance of I2CLCDDisplay and call it LCDDisplay
LCDDisplay = I2CLCDDisplay()
#Set the background colour to white
LCDDisplay.LEDColor(255,255,255) #RGB
#Write "Hello World!!!" to the screen
LCDDisplay.LCDPrint("Hello World!!!")
#Set the cursor to position 0x28 (start of second line)
LCDDisplay.LCDInstruction(0x80 + 0x28)
#Write "Line 2" to the screen
LCDDisplay.LCDPrint("Line 2")
#Wait 3 seconds
time.sleep(3)
#Set the background colour to Red
LCDDisplay.LEDColor(255,0,0)
time.sleep(3)
#Set the background colour to Green
LCDDisplay.LEDColor(0,255,0)
time.sleep(3)
#Set the background colour to Blue
LCDDisplay.LEDColor(0,0,255)
