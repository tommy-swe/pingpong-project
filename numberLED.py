# from machine import Pin
import time

import RPi.GPIO as GPIO

# pin_D1 = Pin(6, Pin.OUT)
# pin_D2 = Pin(7, Pin.OUT)
# pin_D3 = Pin(8, Pin.OUT)
# pin_D4 = Pin(9, Pin.OUT)
# pin_A = Pin(10, Pin.OUT)
# pin_B = Pin(11, Pin.OUT)
# pin_C = Pin(12, Pin.OUT)
# pin_D = Pin(13, Pin.OUT)
# pin_E = Pin(14, Pin.OUT)
# pin_F = Pin(15, Pin.OUT)
# pin_G = Pin(16, Pin.OUT)
# pin_DP = Pin(17, Pin.OUT)

GPIO.setmode(GPIO.BCM)
Pins = {
    "pin_D1" : 18, 
    "pin_D2" : 25,
    "pin_D3" : 8,
    "pin_D4" : 11,
    "pin_A" : 23, 
    "pin_B" : 7,
    "pin_C" : 10, 
    "pin_D" : 27,
    "pin_E" : 17,
    "pin_F" : 24,
    "pin_G" : 9,
    "pin_DP" : 22

}
for pin in Pins:

    GPIO.setup(Pins[pin],GPIO.OUT)
    GPIO.output(Pins[pin],1)



# sensors_temp = machine.ADC(4)
conversion_factor = 3.3 / (65535)

timetoread = 1000
digit = [0,1,2,3]

try:
    while(True):
        tempstr_list = input("input four number")
        for di in digit:
            if tempstr_list[di] == "0":
                
                GPIO.output(Pins["pin_A"],1)   
                GPIO.output(Pins["pin_B"],1)
                GPIO.output(Pins["pin_C"],1)
                GPIO.output(Pins["pin_D"],1)
                GPIO.output(Pins["pin_E"],1)
                GPIO.output(Pins["pin_F"],1)
                GPIO.output(Pins["pin_G"],0)
                if di ==0:
                    GPIO.output(Pins["pin_D1"],1)
                if di ==1:
                    GPIO.output(Pins["pin_D2"],1)
                if di == 2:
                    GPIO.output(Pins["pin_D3"],1)
                if di == 3:
                    GPIO.output(Pins["pin_D4"],1)

            if tempstr_list[di] == "1":
                
                GPIO.output(Pins["pin_A"],0)   
                GPIO.output(Pins["pin_B"],1)
                GPIO.output(Pins["pin_C"],1)
                GPIO.output(Pins["pin_D"],0)
                GPIO.output(Pins["pin_E"],0)
                GPIO.output(Pins["pin_F"],0)
                GPIO.output(Pins["pin_G"],0)
                if di ==0:
                    GPIO.output(Pins["pin_D1"],1)
                if di ==1:
                    GPIO.output(Pins["pin_D2"],1)
                if di == 2:
                    GPIO.output(Pins["pin_D3"],1)
                if di == 3:
                    GPIO.output(Pins["pin_D4"],1)

            if tempstr_list[di] == "2":
                
                GPIO.output(Pins["pin_A"],0)   
                GPIO.output(Pins["pin_B"],0)
                GPIO.output(Pins["pin_C"],1)
                GPIO.output(Pins["pin_D"],0)
                GPIO.output(Pins["pin_E"],0)
                GPIO.output(Pins["pin_F"],1)
                GPIO.output(Pins["pin_G"],0)
                if di ==0:
                    GPIO.output(Pins["pin_D1"],1)
                if di ==1:
                    GPIO.output(Pins["pin_D2"],1)
                if di == 2:
                    GPIO.output(Pins["pin_D3"],1)
                if di == 3:
                    GPIO.output(Pins["pin_D4"],1)

            if tempstr_list[di] == "3":
                
                GPIO.output(Pins["pin_A"],0)   
                GPIO.output(Pins["pin_B"],0)
                GPIO.output(Pins["pin_C"],0)
                GPIO.output(Pins["pin_D"],0)
                GPIO.output(Pins["pin_E"],1)
                GPIO.output(Pins["pin_F"],1)
                GPIO.output(Pins["pin_G"],0)
                if di ==0:
                    GPIO.output(Pins["pin_D1"],1)
                if di ==1:
                    GPIO.output(Pins["pin_D2"],1)
                if di == 2:
                    GPIO.output(Pins["pin_D3"],1)
                if di == 3:
                    GPIO.output(Pins["pin_D4"],1)

            if tempstr_list[di] == "4":
                
                GPIO.output(Pins["pin_A"],1)   
                GPIO.output(Pins["pin_B"],0)
                GPIO.output(Pins["pin_C"],0)
                GPIO.output(Pins["pin_D"],1)
                GPIO.output(Pins["pin_E"],1)
                GPIO.output(Pins["pin_F"],0)
                GPIO.output(Pins["pin_G"],0)
                if di ==0:
                    GPIO.output(Pins["pin_D1"],1)
                if di ==1:
                    GPIO.output(Pins["pin_D2"],1)
                if di == 2:
                    GPIO.output(Pins["pin_D3"],1)
                if di == 3:
                    GPIO.output(Pins["pin_D4"],1)

            if tempstr_list[di] == "5":
                
                GPIO.output(Pins["pin_A"],0)   
                GPIO.output(Pins["pin_B"],1)
                GPIO.output(Pins["pin_C"],0)
                GPIO.output(Pins["pin_D"],0)
                GPIO.output(Pins["pin_E"],1)
                GPIO.output(Pins["pin_F"],0)
                GPIO.output(Pins["pin_G"],0)
                if di ==0:
                    GPIO.output(Pins["pin_D1"],1)
                if di ==1:
                    GPIO.output(Pins["pin_D2"],1)
                if di == 2:
                    GPIO.output(Pins["pin_D3"],1)
                if di == 3:
                    GPIO.output(Pins["pin_D4"],1)

            if tempstr_list[di] == "6":
                
                GPIO.output(Pins["pin_A"],0)   
                GPIO.output(Pins["pin_B"],1)
                GPIO.output(Pins["pin_C"],0)
                GPIO.output(Pins["pin_D"],0)
                GPIO.output(Pins["pin_E"],0)
                GPIO.output(Pins["pin_F"],0)
                GPIO.output(Pins["pin_G"],1)
                if di ==0:
                    GPIO.output(Pins["pin_D1"],1)
                if di ==1:
                    GPIO.output(Pins["pin_D2"],1)
                if di == 2:
                    GPIO.output(Pins["pin_D3"],1)
                if di == 3:
                    GPIO.output(Pins["pin_D4"],1)

            if tempstr_list[di] == "7":
                
                GPIO.output(Pins["pin_A"],0)   
                GPIO.output(Pins["pin_B"],0)
                GPIO.output(Pins["pin_C"],0)
                GPIO.output(Pins["pin_D"],1)
                GPIO.output(Pins["pin_E"],1)
                GPIO.output(Pins["pin_F"],1)
                GPIO.output(Pins["pin_G"],1)
                if di ==0:
                    GPIO.output(Pins["pin_D1"],1)
                if di ==1:
                    GPIO.output(Pins["pin_D2"],1)
                if di == 2:
                    GPIO.output(Pins["pin_D3"],1)
                if di == 3:
                    GPIO.output(Pins["pin_D4"],1)

            if tempstr_list[di] == "8":
                
                GPIO.output(Pins["pin_A"],0)   
                GPIO.output(Pins["pin_B"],0)
                GPIO.output(Pins["pin_C"],0)
                GPIO.output(Pins["pin_D"],0)
                GPIO.output(Pins["pin_E"],0)
                GPIO.output(Pins["pin_F"],0)
                GPIO.output(Pins["pin_G"],0)
                if di ==0:
                    GPIO.output(Pins["pin_D1"],1)
                if di ==1:
                    GPIO.output(Pins["pin_D2"],1)
                if di == 2:
                    GPIO.output(Pins["pin_D3"],1)
                if di == 3:
                    GPIO.output(Pins["pin_D4"],1)

            if tempstr_list[di] == "9":
                
                GPIO.output(Pins["pin_A"],0)   
                GPIO.output(Pins["pin_B"],0)
                GPIO.output(Pins["pin_C"],0)
                GPIO.output(Pins["pin_D"],0)
                GPIO.output(Pins["pin_E"],1)
                GPIO.output(Pins["pin_F"],0)
                GPIO.output(Pins["pin_G"],0)
                if di ==0:
                    GPIO.output(Pins["pin_D1"],1)
                if di ==1:
                    GPIO.output(Pins["pin_D2"],1)
                if di == 2:
                    GPIO.output(Pins["pin_D3"],1)
                if di == 3:
                    GPIO.output(Pins["pin_D4"],1)

            if di ==0:
                GPIO.output(Pins["pin_DP"],1)
            if di ==1:
                GPIO.output(Pins["pin_DP"],0)
            if di == 2:
                GPIO.output(Pins["pin_DP"],1)
            if di == 3:
                GPIO.output(Pins["pin_DP"],1)

            # light up current led in 0.001 sec and then shut down it and mov eto next digit
            time.sleep(0.001)
            GPIO.output(Pins["pin_D1"], 0)
            GPIO.output(Pins["pin_D2"], 0)
            GPIO.output(Pins["pin_D3"], 0)
            GPIO.output(Pins["pin_D4"], 0)
            GPIO.output(Pins["pin_DP"], 1)
            timetoread += 1
except KeyboardInterrupt:
		GPIO.cleanup()