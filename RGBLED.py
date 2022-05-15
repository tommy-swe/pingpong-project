import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO.setup(16,GPIO.OUT)
GPIO.output(16,1)
GPIO.setup(20,GPIO.OUT)
GPIO.output(20,1)
GPIO.setup(21,GPIO.OUT)
GPIO.output(21,1)

try:
    while(True):
        request = input("RGB-->")
        if (len(request) == 3):
            GPIO.output(16, int(request[0]))
            GPIO.output(20, int(request[1]))
            GPIO.output(21, int(request[2]))
        
except KeyboardInterrupt:
    GPIO.cleanup()