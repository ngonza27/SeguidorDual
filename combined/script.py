from compass import Compass
from current import Current
from time import sleep

current = Current()
compass = Compass()

while True:
	current.get_data()
	sleep(0.25)
	compass.get_angle()
	sleep(0.25)
