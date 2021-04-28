import time
from w1thermsensor import W1ThermSensor

sensor = W1ThermSensor()

class Temperature():

  def get_temp(self):
    return sensor.get_temperature()
