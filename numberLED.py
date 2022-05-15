from machine import Pin
import utime

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

pin_D1 = Pin(18, Pin.OUT)
pin_D2 = Pin(25, Pin.OUT)
pin_D3 = Pin(8, Pin.OUT)
pin_D4 = Pin(11, Pin.OUT)
pin_A = Pin(23, Pin.OUT)
pin_B = Pin(7, Pin.OUT)
pin_C = Pin(10, Pin.OUT)
pin_D = Pin(27, Pin.OUT)
pin_E = Pin(17, Pin.OUT)
pin_F = Pin(24, Pin.OUT)
pin_G = Pin(9, Pin.OUT)
pin_DP = Pin(22, Pin.OUT)

#Pin set to down

pin_A.value(0)
pin_B.value(0)
pin_C.value(0)
pin_D.value(0)
pin_E.value(0)
pin_F.value(0)
pin_G.value(0)
pin_DP.value(0)
pin_D1.value(0)
pin_D2.value(0)
pin_D3.value(0)
pin_D4.value(0)

sensors_temp = machine.ADC(4)
conversion_factor = 3.3 / (65535)

timetoread = 1000
digit = [0,1,2,3]

while True:
    if timetoread == 1000:
        reading = sensors_temp.read_u16()* conversion_factor
        temperature = 27 - (reading - 0.706)/0.001721
        temp = round(temperature, 2)
        timetoread = 0
    

    tempstr = str(temp)
    tempstr_list = ["0", "0", "0", "0"]
    tempstr_list[:0] = list(tempstr)
    tempstr_list.pop(2)
    tempstr_list.insert(3, "C")

    for di in digit:
        if tempstr_list[di] == "0":
            pin_A.value(0)
            pin_B.value(0)
            pin_C.value(0)
            pin_D.value(0)
            pin_E.value(0)
            pin_F.value(0)
            pin_G.value(1)
            if di ==0:
                pin_D1.value(1)
            if di ==1:
                pin_D2.value(1)
            if di == 2:
                pin_D3.value(1)
            if di == 3:
                pin_D4.value(1)
        if tempstr_list[di] == "1":
            pin_A.value(1)
            pin_B.value(0)
            pin_C.value(0)
            pin_D.value(1)
            pin_E.value(1)
            pin_F.value(1)
            pin_G.value(1)
            if di ==0:
                pin_D1.value(1)
            if di ==1:
                pin_D2.value(1)
            if di == 2:
                pin_D3.value(1)
            if di == 3:
                pin_D4.value(1)
        if tempstr_list[di] == "2":
            pin_A.value(0)
            pin_B.value(0)
            pin_C.value(1)
            pin_D.value(0)
            pin_E.value(0)
            pin_F.value(1)
            pin_G.value(0)
            if di ==0:
                pin_D1.value(1)
            if di ==1:
                pin_D2.value(1)
            if di == 2:
                pin_D3.value(1)
            if di == 3:
                pin_D4.value(1)
        if tempstr_list[di] == "3":
            pin_A.value(0)
            pin_B.value(0)
            pin_C.value(0)
            pin_D.value(0)
            pin_E.value(1)
            pin_F.value(1)
            pin_G.value(0)
            if di ==0:
                pin_D1.value(1)
            if di ==1:
                pin_D2.value(1)
            if di == 2:
                pin_D3.value(1)
            if di == 3:
                pin_D4.value(1)
        if tempstr_list[di] == "4":
            pin_A.value(1)
            pin_B.value(0)
            pin_C.value(0)
            pin_D.value(1)
            pin_E.value(1)
            pin_F.value(0)
            pin_G.value(0)
            if di ==0:
                pin_D1.value(1)
            if di ==1:
                pin_D2.value(1)
            if di == 2:
                pin_D3.value(1)
            if di == 3:
                pin_D4.value(1)
        if tempstr_list[di] == "5":
            pin_A.value(0)
            pin_B.value(1)
            pin_C.value(0)
            pin_D.value(0)
            pin_E.value(1)
            pin_F.value(0)
            pin_G.value(0)
            if di ==0:
                pin_D1.value(1)
            if di ==1:
                pin_D2.value(1)
            if di == 2:
                pin_D3.value(1)
            if di == 3:
                pin_D4.value(1)
        if tempstr_list[di] == "6":
            pin_A.value(0)
            pin_B.value(1)
            pin_C.value(0)
            pin_D.value(0)
            pin_E.value(0)
            pin_F.value(0)
            pin_G.value(1)
            if di ==0:
                pin_D1.value(1)
            if di ==1:
                pin_D2.value(1)
            if di == 2:
                pin_D3.value(1)
            if di == 3:
                pin_D4.value(1)
        if tempstr_list[di] == "7":
            pin_A.value(0)
            pin_B.value(0)
            pin_C.value(0)
            pin_D.value(1)
            pin_E.value(1)
            pin_F.value(1)
            pin_G.value(1)
            if di ==0:
                pin_D1.value(1)
            if di ==1:
                pin_D2.value(1)
            if di == 2:
                pin_D3.value(1)
            if di == 3:
                pin_D4.value(1)
        if tempstr_list[di] == "8":
            pin_A.value(0)
            pin_B.value(0)
            pin_C.value(0)
            pin_D.value(0)
            pin_E.value(0)
            pin_F.value(0)
            pin_G.value(0)
            if di ==0:
                pin_D1.value(1)
            if di ==1:
                pin_D2.value(1)
            if di == 2:
                pin_D3.value(1)
            if di == 3:
                pin_D4.value(1)
        if tempstr_list[di] == "9":
            pin_A.value(0)
            pin_B.value(0)
            pin_C.value(0)
            pin_D.value(0)
            pin_E.value(1)
            pin_F.value(0)
            pin_G.value(0)
            if di ==0:
                pin_D1.value(1)
            if di ==1:
                pin_D2.value(1)
            if di == 2:
                pin_D3.value(1)
            if di == 3:
                pin_D4.value(1)
        if tempstr_list[di] == "0":
            pin_A.value(0)
            pin_B.value(0)
            pin_C.value(0)
            pin_D.value(0)
            pin_E.value(0)
            pin_F.value(0)
            pin_G.value(1)
            if di ==0:
                pin_D1.value(1)
            if di ==1:
                pin_D2.value(1)
            if di == 2:
                pin_D3.value(1)
            if di == 3:
                pin_D4.value(1)
        if tempstr_list[di] == "C":
            pin_A.value(0)
            pin_B.value(1)
            pin_C.value(1)
            pin_D.value(0)
            pin_E.value(0)
            pin_F.value(0)
            pin_G.value(1)
            if di ==0:
                pin_D1.value(1)
            if di ==1:
                pin_D2.value(1)
            if di == 2:
                pin_D3.value(1)
            if di == 3:
                pin_D4.value(1)
        #LIGHT up dot
        if di == 0:
            pin_DP.value(1)
        if di == 1:
            pin_DP.value(0)
        if di == 2:
            pin_DP.value(1)
        if di == 3:
            pin_DP.value(1)

        # light up current led in 0.001 sec and then shut down it and mov eto next digit
        utime.sleep(0.001)
        pin_D1.value(0)
        pin_D2.value(0)
        pin_D3.value(0)
        pin_D4.value(0)
        pin_DP.value(1)
        timetoread += 1