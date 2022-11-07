from motor import Motor
from machine import Pin
import time
import machine
import utime
from picographics import PicoGraphics, DISPLAY_PICO_EXPLORER

display = PicoGraphics(display=DISPLAY_PICO_EXPLORER)

WIDTH, HEIGHT = display.get_bounds()
BG = display.create_pen(255, 255, 255)
BLACK = display.create_pen(0, 0, 0)

led=Pin("LED", Pin.OUT)
# Using the on board LED for signals

sensor = machine.ADC(26)
#Create an input pin object for water level sensor

threshold = 30000
# threshold for the water level sensor

m1 = Motor((8, 9))

# Pump starts pumping water from bucket
m1.enable()
m1.speed(1.0)

def clear():
    display.set_pen(BG)
    display.clear()
    display.update()


while True:
    value=sensor.read_u16()  
    # printing out the sensor value in terminal
    print(value)

    #clear the screen to background color
    clear()
    display.set_pen(BLACK)

    # displaying Pumping Water text in the screen
    display.text("Pumping Water!",10,10,200,4)
    display.update()
    
    if value > threshold :
        led.toggle()
        display.set_pen(BG)
        display.clear()
        display.set_pen(BLACK)

        # displaying Bucket Filled text in the screen 
        display.text("Bucket Filled!", 10, 10, 200,4)
        display.update()
        
        #printing Bucket Filled text in the terminal
        print("Bucket Filled!")

        # Pump stops pumping water
        m1.disable()
        time.sleep(1)
        break
    utime.sleep_ms(200)
    time.sleep(1)
    clear()
 
# displaying Pumping off text in the screen after the pump stops   
display.set_pen(BG)
display.clear()
display.set_pen(BLACK)
display.text("Pumping OFF!", 10, 10, 200,4)
display.update()
