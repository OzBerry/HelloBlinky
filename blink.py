#!/usr/bin/env python

import RPi.GPIO as GPIO
import time

# The pin number used for output
pin = 12 

# set the pin number mode
GPIO.setmode(GPIO.BOARD)

# set our pin to output mode
GPIO.setup(pin, GPIO.OUT)

# blinking function
def blink(pin):
        GPIO.output(pin,GPIO.HIGH)
        time.sleep(1)
        GPIO.output(pin,GPIO.LOW)
        time.sleep(1)
        return

# blink!
for i in range(0,20):
        blink(pin)
        print ("blink! " + time.strftime("%H:%M:%S"))
GPIO.cleanup() 
