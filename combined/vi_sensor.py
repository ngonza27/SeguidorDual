#!/usr/bin/env python
from ina219 import INA219
from ina219 import DeviceRangeError
from time import sleep


class Sensorvi():

  def getVI(self):
    SHUNT_OHMS = 0.1
    ina = INA219(SHUNT_OHMS)
    ina.configure()
    try:
        voltage = ina.shunt_voltage()
        current = ina.current()
        if(voltage < 0):
          voltage = 0
        if(current < 0):
          current = 0
        print("Bus Current: %.3f mA" % voltage)
        print("Shunt voltage: %.3f mV" % current)
        return ina.shunt_voltage(), ina.current()
    except DeviceRangeError as e:
        print(e)
