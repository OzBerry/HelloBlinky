import RPi.GPIO as GPIO
import time

# The pin number for output
pin = 12 

# to use Raspberry Pi board pin numbers
GPIO.setmode(GPIO.BOARD)

# set up GPIO output channel 18 (12)
GPIO.setup(pin, GPIO.OUT)

# blinking function
def blink(pin):
        GPIO.output(pin,GPIO.HIGH)
        time.sleep(1)
        GPIO.output(pin,GPIO.LOW)
        time.sleep(1)
        return

# blink!
for i in range(0,50):
        blink(pin)
GPIO.cleanup() 
