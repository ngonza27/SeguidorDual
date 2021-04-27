# Import libraries
import RPi.GPIO as GPIO
from compass import Compass
from sun_posv3 import Sunpos
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

  def getServoAngle(self):
	global anguloBase
	return anguloBase


  def movePosAngles(self, compass, azimuth):
    while (int(compass.get_angle()) <= azimuth):
      print("azimuth: ", azimuth, "compass angle: ", int(compass.get_angle()))
      servo1.ChangeDutyCycle(6.7)
      time.sleep(0.007)
      servo1.ChangeDutyCycle(0)


  def moveNegAngles(self, compass, azimuth):
    while (int(compass.get_angle()) >= azimuth):
      print("angulo: ", int(compass.get_angle()), "anguloBASE:", anguloBase, "vuelta atras: ", vueltaAtras, " input ", input)
      servo1.ChangeDutyCycle(7.3)
      time.sleep(0.00333)
      servo1.ChangeDutyCycle(0)


  def startingPos(self):
    compass = Compass()
    if compass.get_angle() > 0:
      while(int(compass.get_angle()) >= 0)
        servo1.ChangeDutyCycle(7.3)
        time.sleep(0.00333)
        servo1.ChangeDutyCycle(0)
    return 0

  def setAngle(self):
    compass = Compass()
    sunpos = Sunpos()
    azimuth = sunpos.get_az_alt()[1]
    print("compass", compass.get_angle(), "az;", azimuth)
    global anguloBase
    if azimuth < 90:
      if anguloBase < azimuth:
        self.movePosAngles(compass, azimuth)
      else:
        self.moveNegAngles(compass, azimuth)
    else:
      azimuth = azimuth + 180
      if anguloBase < azimuth:
        self.moveNegAngles(compass, azimuth)
      else:
        self.movePosAngles(compass, azimuth)
    anguloBase = azimuth
    print("ANGULO BASE: ", self.getServoAngle())
    data = input()
    servo1.stop()
    GPIO.cleanup()
    return self.getServoAngle()
