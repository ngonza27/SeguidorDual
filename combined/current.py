from time import sleep
from ina219 import INA219

#sudo i2cdetect -y 1

class Current:

	def get_data(self):
		ina = INA219(shunt_ohms=0.1, max_expected_amps = 0.6, address=0x40)

		ina.configure(voltage_range=ina.RANGE_16V,
              		gain=ina.GAIN_AUTO,
             		bus_adc=ina.ADC_128SAMP,
              		shunt_adc=ina.ADC_128SAMP)

		try:
        		v = ina.voltage()
        		i = ina.current()
        		p = ina.power()
        		print("V: ", v, " Amps: ", i, " P: ", p)
        		sleep(1)
		except KeyboardInterrupt:
    			print ("\nCtrl-C pressed.  Program exiting...")


