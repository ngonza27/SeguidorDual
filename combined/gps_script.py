import serial
import time
import string
import pynmea2

class GPS:

	def get_data(self):
		port="/dev/ttyS0"
		ser=serial.Serial(port, baudrate=9600, timeout=0.5)
		dataout = pynmea2.NMEAStreamReader()
		newdata=ser.readline()
		lat, lng = 0,0
		while lat == 0:
			if newdata[0:6] == "$GPRMC":
				newmsg=pynmea2.parse(newdata)
				lat=newmsg.latitude
				lng=newmsg.longitude
				gps = "Latitude=" + str(lat) + " and Longitude=" + str(lng)
				print(gps)
		return lat, lng
