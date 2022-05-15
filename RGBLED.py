import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

GPIO.setup(11,GPIO.OUT)
GPIO.output(11,1)
GPIO.setup(13,GPIO.OUT)
GPIO.output(13,1)
GPIO.setup(15,GPIO.OUT)
GPIO.output(15,1)

try:
    while(True):
        request = input("RGB-->")
        
except KeyboardInterrupt:
    GPIO.cleanup()