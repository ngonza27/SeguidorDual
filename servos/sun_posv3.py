from pyephem_sunpath.sunpath import sunpos
from datetime import datetime
from gps_script import GPS

class Sunpos:

	def get_az_alt(self):
		gps = GPS()
                thetime = datetime.now()
		tz = -5
		data = gps.get_data()
		if data != None:
			#print(data)
			lat = data[0]
			lon = data[1]
			alt, azm = sunpos(thetime, lat, lon, tz, dst=False)
			print("Altitud:", alt, ", Azimuth:", azm)
			return alt, azm

sun = Sunpos()
while True:
	sun.get_az_alt()
