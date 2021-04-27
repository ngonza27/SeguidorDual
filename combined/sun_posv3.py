from pyephem_sunpath.sunpath import sunpos
from datetime import datetime
from gps_script import GPS

class Sunpos:

	def get_az_alt(self):
		gps = GPS()
                thetime = datetime.now()
		tz = -5
		data = gps.get_data()
		print(data)
		while data is None:
			data = gps.get_data()
		lat = data[0]
		lon = data[1]
		alt, azm = sunpos(thetime, lat, lon, tz, dst=False)
		print("Altitud:", alt, ", Azimuth:", azm)
		return alt, azm


