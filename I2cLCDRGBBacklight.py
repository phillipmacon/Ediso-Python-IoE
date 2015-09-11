#Python mraa I2c LCD with RGB background led 
#tested with seeedstudio Grove LCD RGB Backlight and Intel Edison
#Willem-Jan Derks 2015 

#!/usr/bin/python
import mraa,time

#LCD Instructions
#0x01 Clear display and return to the home position
#0x02 Returns cursor and shift home, screen not cleared
#0x08 + 0x04 Display on
#0x08 + 0x02 Cursor on
#0x08 + 0x01 Cursor Blink on
#0x10 + 0x08 Shift display left
#0x10 + 0x0c Shift display right
#0x10 + 0x00 Shift cursor left
#0x10 + 0x04 Shift cursor right
#0x80 + Address line1 0x00-0x27 line2 0x28-0x4F
def LCDInstruction(instruction):
        LCD.writeReg(0x80,instruction)
        time.sleep(0.05)
        return

def I2cLCDInit():
        LCD = mraa.I2c(0)
        LCD.address(0x3e)
        LCD.writeReg(0x80,0x38) #8Bit, 2lines, 5x7
        time.sleep(0.05)
        LCD.writeReg(0x80,0x08+0x07) #display on, cursor on, blink on
        time.sleep(0.05)
        LCD.writeReg(0x80,0x01) #clear display, cursor 1st line, 1st character
        return(LCD)

def I2cLCDLEDInit():
        LCDLED = mraa.I2c(0)
        LCDLED.address(0x62)
        LCDLED.writeReg(0,0)
        LCDLED.writeReg(1,0)
        LCDLED.writeReg(0x08,0xaa)
        return(LCDLED)

def LCDPrint(text):
        for letter in text:
                LCD.writeReg(0x40,ord(letter))
        return

def LEDColor(R,G,B):
        LCDLED.writeReg(4,R)
        LCDLED.writeReg(3,G)
        LCDLED.writeReg(2,B)
        return

LCD = I2cLCDInit()
LCDLED = I2cLCDLEDInit()

LEDColor(255,255,255) #RGB
LCDPrint("Hello World!")
LCDInstruction(0x80+0x28)
LCDPrint("Line2")

#cycle through RGB
while True:
        for i in range(0, 255):
                LEDColor(i,0,255-i)
                time.sleep(0.005)
        for i in range(0, 255):
                LEDColor(255-i,i,0)
                time.sleep(0.005)
        for i in range(0, 255):
                LEDColor(0,255-i,i)
                time.sleep(0.005)
