from TH02 import TH02
import time
from I2CLCDDisplay import I2CLCDDisplay as LCDDisplay

sensor = TH02()
display = LCDDisplay()
while True:
        display.LCDInstruction(0x80 + 0)
        display.LCDPrint("Temp: " + str(sensor.getTemperature()))
        display.LCDInstruction(0x80 + 0x28)
        display.LCDPrint("Humi: " + str(sensor.getHumidity()))
        print("Temp: "+ str(sensor.getTemperature()))
        print("Humi: "+ str(sensor.getHumidity()))
        time.sleep(1)
