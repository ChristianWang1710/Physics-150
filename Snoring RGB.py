"""This example lights up and makes LEDs 0,4,5,and 9 snore."""
import time
from adafruit_circuitplayground import cp

cp.pixels.brightness = 0.15
#cp.pixels.fill((0,0,50))

i=0;
while True:
    while (i<255):
        cp.pixels[0] = (i,0,i)
        cp.pixels[4] = (i,0,20)
        cp.pixels[5] = (i,0,0)
        cp.pixels[9] = (i,i,0)
        i+=5
        time.sleep(0.01)
    while (i>0):
        cp.pixels[0] = (i,0,i)
        cp.pixels[4] = (i,0,20)
        cp.pixels[5] = (i,0,0)
        cp.pixels[9] = (i,i,0)
        #cp.pixels[7] = (0,i,0)
        #cp.pixels[2] = (0,i,0)
        i-=5
        time.sleep(0.001)