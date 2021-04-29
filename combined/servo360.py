# Import libraries
import RPi.GPIO as GPIO
from compass import Compass
from sun_posv3 import Sunpos
import time

# Set GPIO numbering mode
GPIO.setmode(GPIO.BOARD)

# Set pin 11 as an output, and set servo1 as pin 11 as PWM
GPIO.setup(38,GPIO.OUT)
servo1 = GPIO.PWM(38,50) # Note 11 is pin, 50 = 50Hz pulse

#start PWM running, but with value of 0 (pulse off)
servo1.start(0)
anguloBase = 0

class Servo360:

  def getServoAngle(self):
	global anguloBase
	return anguloBase


  def movePosAngles(self, compass, azimuth):
    while (int(compass.get_angle()) < azimuth):
      print("azimuth: ", azimuth, "compass angle: ", int(compass.get_angle()))
      servo1.ChangeDutyCycle(6.7)
      time.sleep(0.00333)
      servo1.ChangeDutyCycle(0)


  def moveNegAngles(self, compass, azimuth):
    print("Moviendo angulos negativos!!")
    while (int(compass.get_angle()) > azimuth):
      print("angulo: ", int(compass.get_angle()), "anguloBASE:", anguloBase, "vuelta atras: ", vueltaAtras, " input ", input)
      servo1.ChangeDutyCycle(7.3)
      time.sleep(0.00333)
      servo1.ChangeDutyCycle(0)


  def startingPos(self, compass):
    angle = compass.get_angle()

    if angle > 0 and angle <= 90:
      while(int(compass.get_angle()) > 0):
        servo1.ChangeDutyCycle(7.3)
        time.sleep(0.00333)
        servo1.ChangeDutyCycle(0)
    if angle > 270 and angle <= 359:
      while(int(compass.get_angle()) > 0):
        servo1.ChangeDutyCycle(6.7)
        time.sleep(0.00333)
        servo1.ChangeDutyCycle(0)
    return 0

  def setAngle(self):
    print("Set angle")
    compass = Compass()
    #sunpos = Sunpos()
    #azimuth = sunpos.get_az_alt()[1]
    azimuth = 283
    print("compass", compass.get_angle(), "az;", azimuth)
    global anguloBase
    if azimuth =< 90 and azimuth >= 0: #Primer cuadrante (N-E)
      if anguloBase => 270 and anguloBase <= 359:
        self.startingPos(compass)
        anguloBase = 0
      if anguloBase < azimuth:
        self.movePosAngles(compass, azimuth)
      else:
        self.moveNegAngles(compass, azimuth)
    if azimuth > 90 and azimuth <= 180: #Segundo cuadrante (E-S)
      azimuth = azimuth + 180
      if anguloBase < azimuth:
        self.movePosAngles(compass, azimuth)
      else:
        self.moveNegAngles(compass, azimuth)
    if azimuth > 180 and azimuth <= 270: #Tercer cuadrante (S-O)
      azimuth = azimuth - 180
      if anguloBase < azimuth:
        self.movePosAngles(compass, azimuth)
      else:
        self.moveNegAngles(compass, azimuth)
    if azimuth > 270 and azimuth <= 359: #Cuarto cuadrante (O-N)
      if anguloBase >= 0 and angulo <= 90:
        self.startingPos(compass)
        anguloBase = 0
      if anguloBase < azimuth:
       self.movePosAngles(compass, azimuth)
      else:
       self.moveNegAngles(compass, azimuth)
    anguloBase = azimuth
    print("ANGULO BASE: ", self.getServoAngle())
    servo1.stop()
    GPIO.cleanup()
    return self.getServoAngle()


sr = Servo360()
sr.setAngle()
