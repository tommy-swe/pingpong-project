from random import randint
from secrets import choice
import RPi.GPIO as GPIO
import random

GPIO.setmode(GPIO.BCM)

pin_LED = [17, 27, 22, 10, 9, 11, 18, 23, 24, 25, 8, 7]
for pin in pin_LED:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, 1)


try:
    while(True):
        rand_idx = random.choice(pin_LED)
        GPIO.output(rand_idx, 0)
        
except KeyboardInterrupt:
    GPIO.cleanup()