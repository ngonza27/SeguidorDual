# Import libraries
import RPi.GPIO as GPIO
from compass import Compass
#from sun_posv3 import Sunpos
import time

# Set GPIO numbering mode
GPIO.setmode(GPIO.BOARD)

# Set pin 11 as an output, and set servo1 as pin 11 as PWM
GPIO.setup(40,GPIO.OUT)
servo1 = GPIO.PWM(40,50) # Note 11 is pin, 50 = 50Hz pulse

#start PWM running, but with value of 0 (pulse off)
servo1.start(0)
anguloBase = 0

class Servo360:

  def movePosAngles(self, compass, input):
    spa, spb = input, 0
    while (compass.get_angle() < input):
      print("moviendos")
      servo1.ChangeDutyCycle(6.3)
      time.sleep(0.007)
      servo1.ChangeDutyCycle(0)
    vuelta = False


servo = Servo360()
#sunpos = Sunpos()
azimuth = 50
compass = Compass()
servo.movePosAngles(compass, azimuth)

