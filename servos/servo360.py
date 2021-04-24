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

  def movePosAngles(self, compass, input):
    spa, spb = input, 0
    vuelta = False
    if input > 359:
      spa = 360
      spb = input - 360
    global anguloBase
    while (compass.get_angle() <= spb and vuelta == True) or (compass.get_angle() <= spa and vuelta == False):
      compAngle = compass.get_angle()
      if compAngle != 0:
        anguloBase = compAngle
      if anguloBase != 0 and int(compAngle) == 0:
        vuelta = True
      print("angulo actual: ", compAngle, " SPB: ", spb, " SPA: ", spa, "ya dio vuelta? ", vuelta, " anuglo base:", anguloBase)
      servo1.ChangeDutyCycle(6.7)
      time.sleep(0.007)
      servo1.ChangeDutyCycle(0)
    vuelta = False


  def moveNegAngles(self, compass, input):
    vueltaAtras = False
    global anguloBase
    #anguloBase = 500
    if anguloBase > 359 and input < 360:
      vueltaAtras = True
    if anguloBase > 360 and input >= 360:
      input = input - 360
    while (int(compass.get_angle()) > input) or  vueltaAtras == True:
      compAngle = compass.get_angle()
      if int(compAngle) == 359 and vueltaAtras == True:
        vueltaAtras = False
      print("angulo: ", int(compass.get_angle()), "anguloBASE:", anguloBase, "vuelta atras: ", vueltaAtras, " input ", input)
      servo1.ChangeDutyCycle(7.3)
      time.sleep(0.00333)
      servo1.ChangeDutyCycle(0)
    vueltaAtras = False

  def setAngle(self, ina):
    compass = Compass()
    print("Inserte un angulo: ")
    global anguloBase
    if anguloBase < ina:
      self.movePosAngles(compass, ina)
    else:
      self.moveNegAngles(compass, ina)
    anguloBase = ina
    print("ANGULO BASE: ", self.getServoAngle())
    servo1.stop()
    GPIO.cleanup()


servo = Servo360()
sunpos = Sunpos()
azimuth = sunpos.get_az_alt()[1]
servo.setAngle(azimuth)

