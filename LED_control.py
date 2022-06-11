## Author
## Date: 

# this script is for LED control classes, including RGB and 4 digit signal


import RPi.GPIO as GPIO
import time


# Define a MAP function for mapping values.  Like from 0~255 to 0~100
def MAP(x, in_min, in_max, out_min, out_max):
	return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min


class RGBLEDcontroller:
    """
    control RGB signal
    input:
    - pins: pins number of Red, Green and Blue (default : R = 16, Green = 20, Blue = 21)
    """
    def __init__(self, pins = {'Red':16, 'Green':20, 'Blue':21}):
        self.pins = pins

        # Set up a color table in Hexadecimal
        
    
    def setup(self):
        # Set the GPIO modes to BCM Numbering
        GPIO.setmode(GPIO.BCM)
        
        # Set all LedPin's mode to output and initial level to High(3.3v)
        for i in self.pins:
            GPIO.setup(self.pins[i], GPIO.OUT, initial=GPIO.HIGH)
            
        self.p_R = GPIO.PWM(self.pins['Red'], 2000)
        self.p_G = GPIO.PWM(self.pins['Green'], 2000)
        self.p_B = GPIO.PWM(self.pins['Blue'], 2000)

        # Set all begin with value 0
        self.p_R.start(0)
        self.p_G.start(0)
        self.p_B.start(0)

    def setColor(self, color):
        # configures the three LEDs' luminance with the inputted color value . 
	    # Devide colors from 'color' veriable
        R_val = (color & 0xFF0000) >> 16
        G_val = (color & 0x00FF00) >> 8
        B_val = (color & 0x0000FF) >> 0

        # Change the colors
        self.p_R.ChangeDutyCycle(R_val)
	    # Assign the mapped duty cycle value to the corresponding PWM channel to change the luminance. 
        self.p_G.ChangeDutyCycle(G_val)
        self.p_B.ChangeDutyCycle(B_val)

    def stop(self):
        # Stop all pwm channel
        self.p_R.stop()
        self.p_G.stop()
        self.p_B.stop()
	    # Release resource
        GPIO.cleanup()
