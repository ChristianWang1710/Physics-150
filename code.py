# from adafruit
# https://learn.adafruit.com/welcome-to-circuitpython/creating-and-editing-code
#
import board
import digitalio
import time

led = digitalio.DigitalInOut(board.D13)
led.direction = digitalio.Direction.OUTPUT

while True:
    print("SOS")
    led.value = True
    time.sleep(.1)
    led.value = False
    time.sleep(.25)
    led.value = True
    time.sleep(.1)
    led.value = False
    time.sleep(.25)
    led.value = True
    time.sleep(.1)
    led.value = False
    time.sleep(.25)
    led.value = True
    time.sleep(.5)
    led.value = False
    time.sleep(.25)
    led.value = True
    time.sleep(.5)
    led.value = False
    time.sleep(.25)
    led.value = True
    time.sleep(.5)
    led.value = False
    time.sleep(.25)
    led.value = True
    time.sleep(.1)
    led.value = False
    time.sleep(.25)
    led.value = True
    time.sleep(.1)
    led.value = False
    time.sleep(.25)
    led.value = True
    time.sleep(.1)
    led.value = False
    time.sleep(2)

# Tasks:
# - Try an on-off cycle of 2:1, 0.2:0.1, 0.002:0.001 etc
# what is the shortest on-off cycle you can still see (seizure risk)
# if you want the LED to be at solid 20% brightness, what would the code look like?
# Code SOS in Morse

# loops? Blink out an SOS pattern with a foreach loop that specifies duration